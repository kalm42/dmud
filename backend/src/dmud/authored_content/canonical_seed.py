import json

from dmud.authored_content.p0_starting_seed import P0StartingSeed


def canonical_seed(seed: P0StartingSeed) -> bytes:
    """Serialize a seed, excluding its digest, to deterministic canonical JSON bytes.

    Keys are sorted and separators fixed so equal seeds are byte-identical. For
    example, hashlib.sha256(canonical_seed(seed)).hexdigest().
    """
    document = seed.model_dump(mode="json", exclude={"digest"})
    return json.dumps(
        document, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode()
