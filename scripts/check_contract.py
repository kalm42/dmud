"""Regenerate the OpenAPI boundary and fail when committed artifacts drift."""

import os
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "contracts" / "openapi.json"
GENERATED = ROOT / "frontend" / "src" / "api" / "generated"


def snapshot() -> dict[str, bytes]:
    """Read tracked contract bytes; for example, snapshot() before regeneration."""
    paths = [CONTRACT, *GENERATED.rglob("*")]
    return {str(path.relative_to(ROOT)): path.read_bytes() for path in paths if path.is_file()}


def main() -> None:
    """Check generated output deterministically; for example, python3 scripts/check_contract.py."""
    before = snapshot()
    environment = os.environ.copy()
    environment["PYTHONPATH"] = "src"
    subprocess.run(
        ["uv", "run", "python", "scripts/export_openapi.py"],
        cwd=ROOT / "backend",
        env=environment,
        check=True,
    )
    subprocess.run(["npm", "run", "generate:api"], cwd=ROOT / "frontend", check=True)
    if snapshot() != before:
        raise SystemExit("Generated API contract drift detected")


if __name__ == "__main__":
    main()
