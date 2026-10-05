import pytest

from dmud.authored_content.content_result import ContentLoaded
from dmud.authored_content.load_content import load_content
from dmud.authored_content.travel_seconds import travel_seconds
from dmud.platform.settings import REPOSITORY_CONTENT_DIRECTORY

SHORT = "route:brackenford:market-square-to-maras-stall"
LONG = "route:brackenford:market-square-to-common-room"


def committed_times() -> dict[tuple[str, str], int]:
    result = load_content(REPOSITORY_CONTENT_DIRECTORY)
    assert isinstance(result, ContentLoaded)
    registry = result.registry
    return {
        (route.id, mode.name): travel_seconds(route.length_mm, mode.speed_mm_per_second)
        for route in registry.world.routes
        for mode in registry.movement.modes
    }


@pytest.mark.parametrize(
    ("route", "mode", "seconds"),
    [
        (SHORT, "walk", 5),
        (SHORT, "jog", 3),
        (SHORT, "sprint", 2),
        (SHORT, "crawl", 14),
        (LONG, "walk", 100),
        (LONG, "jog", 50),
        (LONG, "sprint", 25),
        (LONG, "crawl", 280),
    ],
)
def test_committed_route_time_is_the_exact_integer_ceiling(
    route: str, mode: str, seconds: int
) -> None:
    assert committed_times()[(route, mode)] == seconds


def test_partial_second_rounds_up() -> None:
    assert travel_seconds(7000, 5600) == 2


def test_exact_division_does_not_round_up() -> None:
    assert travel_seconds(140000, 1400) == 100
