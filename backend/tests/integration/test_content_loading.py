from pathlib import Path

import pytest

from dmud.authored_content.content_result import ContentLoaded, ContentUnavailable
from dmud.authored_content.load_content import load_content
from dmud.platform.settings import REPOSITORY_CONTENT_DIRECTORY

STALL = "worlds/brackenford/locations/maras-stall.yaml"
SQUARE = "worlds/brackenford/locations/market-square.yaml"
MARA = "worlds/brackenford/npcs/mara.yaml"
CONFLICT = "worlds/brackenford/conflicts/maras-debt.yaml"


def committed() -> ContentLoaded:
    result = load_content(REPOSITORY_CONTENT_DIRECTORY)
    assert isinstance(result, ContentLoaded)
    return result


def rejected(directory: Path) -> ContentUnavailable:
    result = load_content(directory)
    assert isinstance(result, ContentUnavailable)
    return result


def edit(directory: Path, relative: str, old: str, new: str) -> None:
    path = directory / relative
    text = path.read_text()
    assert old in text
    path.write_text(text.replace(old, new, 1))


def found(result: ContentUnavailable) -> set[tuple[str, str, str]]:
    return {(issue.code, issue.file, issue.field) for issue in result.issues}


class TestCommittedPackage:
    def test_loads_exactly_three_locations(self) -> None:
        assert len(committed().registry.locations) == 3

    def test_loads_exactly_four_named_npcs(self) -> None:
        names = {npc.name for npc in committed().registry.npcs.values()}
        assert names == {"Mara", "Oren", "Tessa", "Ivo"}

    def test_loads_one_social_conflict(self) -> None:
        assert list(committed().registry.conflicts) == [
            "conflict:brackenford:maras-debt"
        ]

    def test_loads_one_drink_priced_one_gold_stocked_five_times(self) -> None:
        registry = committed().registry
        stock = registry.starting_state.item_stock
        assert [item.price_gold for item in registry.items.values()] == [1]
        assert [(s.item_id, s.quantity) for s in stock] == [
            ("item:brackenford:drink", 5)
        ]

    def test_loads_two_routes(self) -> None:
        assert len(committed().registry.world.routes) == 2

    def test_loads_four_movement_speeds(self) -> None:
        speeds = {
            mode.name: mode.speed_mm_per_second
            for mode in committed().registry.movement.modes
        }
        assert speeds == {"walk": 1400, "jog": 2800, "sprint": 5600, "crawl": 500}

    def test_loads_one_controlled_check(self) -> None:
        checks = list(committed().registry.checks.values())
        assert [(c.attribute, c.skill, c.difficulty) for c in checks] == [
            ("presence", "persuasion", 12)
        ]

    def test_records_a_stable_content_version(self) -> None:
        version = committed().registry.version
        assert (version.package_id, version.content_schema_version) == (
            "package:brackenford-p0",
            1,
        )

    def test_registry_mappings_are_read_only(self) -> None:
        locations = committed().registry.locations
        with pytest.raises(TypeError):
            locations["location:brackenford:extra"] = next(iter(locations.values()))  # type: ignore[index]


class TestRejectedPackage:
    def test_second_check_is_rejected(self, content_copy: Path) -> None:
        source = content_copy / "worlds/brackenford/checks/payment-extension.yaml"
        (content_copy / "worlds/brackenford/checks/haggle.yaml").write_text(
            source.read_text().replace("payment-extension", "haggle")
        )
        assert (
            "unexpected_content",
            "worlds/brackenford/checks/payment-extension.yaml",
            "kind",
        ) in found(rejected(content_copy))

    def test_duplicate_yaml_key_is_rejected(self, content_copy: Path) -> None:
        edit(content_copy, MARA, "name: Mara\n", "name: Mara\nname: Marra\n")
        assert ("duplicate_key", MARA, "name") in found(rejected(content_copy))

    def test_duplicate_id_across_files_is_rejected(self, content_copy: Path) -> None:
        edit(
            content_copy,
            "worlds/brackenford/npcs/ivo.yaml",
            "npc:brackenford:ivo",
            "npc:brackenford:mara",
        )
        assert ("duplicate_id", MARA, "id") in found(rejected(content_copy))

    def test_dangling_reference_is_rejected(self, content_copy: Path) -> None:
        edit(
            content_copy,
            SQUARE,
            "to_location_id: location:brackenford:maras-stall",
            "to_location_id: location:brackenford:nowhere",
        )
        assert ("unresolved_reference", SQUARE, "exits[0].to_location_id") in found(
            rejected(content_copy)
        )

    def test_unknown_top_level_field_is_rejected(self, content_copy: Path) -> None:
        edit(
            content_copy, MARA, "role: stallholder\n", "role: stallholder\nmood: calm\n"
        )
        assert ("unknown_field", MARA, "<unknown>") in found(rejected(content_copy))

    def test_unknown_nested_field_is_rejected(self, content_copy: Path) -> None:
        edit(
            content_copy,
            CONFLICT,
            "  due_second: 115200\n",
            "  due_second: 115200\n  interest: 2\n",
        )
        assert ("unknown_field", CONFLICT, "obligation.<unknown>") in found(
            rejected(content_copy)
        )

    def test_quoted_number_is_not_coerced(self, content_copy: Path) -> None:
        edit(content_copy, CONFLICT, "outstanding_gold: 20", 'outstanding_gold: "20"')
        assert ("invalid_value", CONFLICT, "obligation.outstanding_gold") in found(
            rejected(content_copy)
        )

    def test_unsupported_content_schema_version_is_rejected(
        self, content_copy: Path
    ) -> None:
        edit(
            content_copy,
            "manifest.yaml",
            "content_schema_version: 1",
            "content_schema_version: 2",
        )
        assert (
            "unsupported_content_version",
            "manifest.yaml",
            "content_schema_version",
        ) in found(rejected(content_copy))

    def test_incompatible_package_version_is_rejected(self, content_copy: Path) -> None:
        edit(content_copy, "manifest.yaml", '"1.0.0"', '"2.0.0"')
        assert (
            "unsupported_content_version",
            "manifest.yaml",
            "package_version",
        ) in found(rejected(content_copy))

    def test_missing_manifest_is_rejected(self, content_copy: Path) -> None:
        (content_copy / "manifest.yaml").unlink()
        assert ("manifest_missing", "manifest.yaml", "") in found(
            rejected(content_copy)
        )

    def test_extra_location_is_rejected(self, content_copy: Path) -> None:
        extra = content_copy / "worlds/brackenford/locations/well.yaml"
        extra.write_text(
            (content_copy / STALL)
            .read_text()
            .replace(
                "id: location:brackenford:maras-stall", "id: location:brackenford:well"
            )
        )
        assert (
            "unexpected_content",
            "worlds/brackenford/locations/well.yaml",
            "id",
        ) in found(rejected(content_copy))

    def test_fifth_npc_is_rejected(self, content_copy: Path) -> None:
        (content_copy / "worlds/brackenford/npcs/bram.yaml").write_text(
            "kind: npc\nid: npc:brackenford:bram\nname: Bram\nrole: smith\n"
        )
        assert (
            "unexpected_content",
            "worlds/brackenford/npcs/bram.yaml",
            "id",
        ) in found(rejected(content_copy))

    def test_missing_npc_is_rejected(self, content_copy: Path) -> None:
        (content_copy / "worlds/brackenford/npcs/ivo.yaml").unlink()
        assert ("missing_content", "", "npc:brackenford:ivo") in found(
            rejected(content_copy)
        )

    def test_exit_without_matching_route_is_rejected(self, content_copy: Path) -> None:
        edit(
            content_copy,
            STALL,
            "to_location_id: location:brackenford:market-square",
            "to_location_id: location:brackenford:common-room",
        )
        assert ("exit_mismatch", STALL, "exits") in found(rejected(content_copy))

    def test_route_between_unapproved_locations_is_rejected(
        self, content_copy: Path
    ) -> None:
        edit(
            content_copy,
            "worlds/brackenford/world.yaml",
            "      - location:brackenford:market-square\n      - location:brackenford:common-room",
            "      - location:brackenford:maras-stall\n      - location:brackenford:common-room",
        )
        assert ("route_mismatch", "worlds/brackenford/world.yaml", "routes") in found(
            rejected(content_copy)
        )

    def test_short_introduction_is_rejected(self, content_copy: Path) -> None:
        path = content_copy / STALL
        lines = path.read_text().splitlines()
        start = lines.index("introduction: >-")
        end = lines.index("exits:")
        short = ["introduction: A narrow wooden booth."]
        path.write_text("\n".join(lines[:start] + short + lines[end:]) + "\n")
        assert ("introduction_length", STALL, "introduction") in found(
            rejected(content_copy)
        )

    def test_long_introduction_is_rejected(self, content_copy: Path) -> None:
        edit(
            content_copy, STALL, "a few steps away.", "a few steps away." + " word" * 40
        )
        assert ("introduction_length", STALL, "introduction") in found(
            rejected(content_copy)
        )

    def test_oren_at_the_handover_location_is_rejected(
        self, content_copy: Path
    ) -> None:
        edit(
            content_copy,
            "worlds/brackenford/start.yaml",
            "  - npc_id: npc:brackenford:oren\n    location_id: location:brackenford:common-room",
            "  - npc_id: npc:brackenford:oren\n    location_id: location:brackenford:maras-stall",
        )
        assert (
            "perception_mismatch",
            "worlds/brackenford/start.yaml",
            "handover",
        ) in found(rejected(content_copy))

    def test_pouch_other_than_ten_thousand_gold_is_rejected(
        self, content_copy: Path
    ) -> None:
        edit(content_copy, "worlds/brackenford/start.yaml", "gold: 10000", "gold: 9999")
        assert (
            "fixture_funding_mismatch",
            "worlds/brackenford/start.yaml",
            "prepared_pouch.gold",
        ) in found(rejected(content_copy))

    def test_issues_never_carry_absolute_paths(self, content_copy: Path) -> None:
        edit(
            content_copy, MARA, "role: stallholder\n", "role: stallholder\nmood: calm\n"
        )
        result = rejected(content_copy)
        assert all(not Path(issue.file).is_absolute() for issue in result.issues)
        assert str(content_copy) not in repr(result)

    def test_missing_directory_is_reported_as_data(self, tmp_path: Path) -> None:
        assert found(rejected(tmp_path / "absent")) == {
            ("content_directory_missing", "", "")
        }

    def test_rejection_leaves_the_content_files_unchanged(
        self, content_copy: Path
    ) -> None:
        edit(
            content_copy, MARA, "role: stallholder\n", "role: stallholder\nmood: calm\n"
        )
        before = {p: p.read_bytes() for p in content_copy.rglob("*.yaml")}
        rejected(content_copy)
        assert {p: p.read_bytes() for p in content_copy.rglob("*.yaml")} == before


class TestReviewRegressions:
    @pytest.mark.parametrize(
        "text",
        [
            "kind: npc\nname: 2026-99-99\n",
            "kind: npc\nloop: &loop [*loop]\n",
            "kind: npc\nloop: " + "[" * 100 + "0" + "]" * 100 + "\n",
        ],
    )
    def test_malformed_structure_returns_invalid_yaml(
        self, content_copy: Path, text: str
    ) -> None:
        (content_copy / MARA).write_text(text)

        result = rejected(content_copy)

        assert ("invalid_yaml", MARA, "") in found(result)

    def test_oversized_package_version_is_rejected(self, content_copy: Path) -> None:
        edit(content_copy, "manifest.yaml", '"1.0.0"', '"' + "1" * 4301 + '.0.0"')

        result = rejected(content_copy)

        assert any(issue.field == "package_version" for issue in result.issues)

    @pytest.mark.parametrize(
        ("path", "old", "new"),
        [
            (CONFLICT, "outstanding_gold: 20", "outstanding_gold: 21"),
            (CONFLICT, "due_second: 115200", "due_second: 0"),
            (
                "worlds/brackenford/checks/payment-extension.yaml",
                "difficulty: 12",
                "difficulty: 1",
            ),
            (
                "worlds/brackenford/checks/payment-extension.yaml",
                "extend_due_by_seconds: 86400",
                "extend_due_by_seconds: 1",
            ),
            ("worlds/brackenford/world.yaml", "length_mm: 7000", "length_mm: 1"),
            ("worlds/brackenford/world.yaml", "length_mm: 140000", "length_mm: 1"),
            *[
                (
                    "rules/movement.yaml",
                    f"speed_mm_per_second: {speed}",
                    "speed_mm_per_second: 1",
                )
                for speed in (1400, 2800, 5600, 500)
            ],
        ],
    )
    def test_changed_fixture_mechanics_are_rejected(
        self, content_copy: Path, path: str, old: str, new: str
    ) -> None:
        edit(content_copy, path, old, new)

        result = rejected(content_copy)

        assert any(issue.file == path for issue in result.issues)

    @pytest.mark.parametrize("key", ["/private/secret", "secret" * 1000])
    @pytest.mark.parametrize("duplicate", [True, False])
    def test_diagnostic_fields_do_not_echo_arbitrary_keys(
        self, content_copy: Path, key: str, duplicate: bool
    ) -> None:
        path = content_copy / MARA
        path.write_text(
            path.read_text() + f"{key}: one\n" + (f"{key}: two\n" if duplicate else "")
        )

        result = rejected(content_copy)

        assert all(
            key not in issue.field and len(issue.field) <= 256
            for issue in result.issues
        )
