from pathlib import Path

from dmud.authored_content.build_p0_seed import build_p0_seed
from dmud.authored_content.content_registry import ContentRegistry
from dmud.authored_content.content_result import ContentLoaded, ContentUnavailable
from dmud.authored_content.extended_due_second import extended_due_second
from dmud.authored_content.load_content import load_content
from dmud.platform.settings import REPOSITORY_CONTENT_DIRECTORY

OBLIGATION = "obligation:brackenford:mara-owes-oren"
CHECK = "worlds/brackenford/checks/payment-extension.yaml"


def registry() -> ContentRegistry:
    result = load_content(REPOSITORY_CONTENT_DIRECTORY)
    assert isinstance(result, ContentLoaded)
    return result.registry


class TestSeededObligation:
    def test_seed_holds_one_obligation_from_mara_to_oren(self) -> None:
        obligations = build_p0_seed(registry()).obligations
        assert [
            (o.obligation_id, o.debtor_npc_id, o.creditor_npc_id) for o in obligations
        ] == [(OBLIGATION, "npc:brackenford:mara", "npc:brackenford:oren")]

    def test_obligation_has_twenty_gold_outstanding(self) -> None:
        (obligation,) = build_p0_seed(registry()).obligations
        assert obligation.outstanding_gold == 20

    def test_obligation_is_due_on_day_two_at_eight(self) -> None:
        (obligation,) = build_p0_seed(registry()).obligations
        assert obligation.due_second == 115_200

    def test_seed_contains_no_other_debt_record(self) -> None:
        document = build_p0_seed(registry()).model_dump_json()
        assert document.count('"obligation_id"') == 1


class TestPaymentExtension:
    def test_check_targets_the_seeded_obligation(self) -> None:
        (check,) = registry().checks.values()
        assert check.obligation_id == OBLIGATION

    def test_success_extends_the_deadline_by_one_day(self) -> None:
        loaded = registry()
        (check,) = loaded.checks.values()
        (conflict,) = loaded.conflicts.values()
        assert (
            extended_due_second(conflict.obligation, check, succeeded=True) == 201_600
        )

    def test_failure_leaves_the_deadline_unchanged(self) -> None:
        loaded = registry()
        (check,) = loaded.checks.values()
        (conflict,) = loaded.conflicts.values()
        assert (
            extended_due_second(conflict.obligation, check, succeeded=False) == 115_200
        )

    def test_check_carries_no_player_attribute_values(self) -> None:
        (check,) = registry().checks.values()
        assert set(check.model_dump()) == {
            "kind",
            "id",
            "name",
            "attribute",
            "skill",
            "difficulty",
            "obligation_id",
            "on_success",
            "on_failure",
        }

    def test_check_naming_another_obligation_is_rejected(
        self, content_copy: Path
    ) -> None:
        path = content_copy / CHECK
        path.write_text(
            path.read_text().replace(
                "obligation_id: " + OBLIGATION,
                "obligation_id: obligation:brackenford:someone-else",
            )
        )
        result = load_content(content_copy)
        assert isinstance(result, ContentUnavailable)
        assert ("unresolved_reference", CHECK, "obligation_id") in {
            (i.code, i.file, i.field) for i in result.issues
        }
