import json
from pathlib import Path

from dmud.main import create_app


def main() -> None:
    """Export the backend contract deterministically; for example, uv run python scripts/export_openapi.py."""
    destination = Path(__file__).resolve().parents[2] / "contracts" / "openapi.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(create_app().openapi(), indent=2) + "\n")


if __name__ == "__main__":
    main()
