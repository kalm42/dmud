import hashlib
import json

from dmud.operations.models import WireModel


def payload_digest(payload: WireModel, kind: str = "") -> str:
    """Compare canonical validated envelopes, including command identity; e.g. payload_digest(request)."""
    canonical = json.dumps(
        payload.model_dump(mode="json", by_alias=True),
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256((kind + canonical).encode()).hexdigest()
