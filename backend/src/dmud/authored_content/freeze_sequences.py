from typing import cast


def freeze_sequences(value: object) -> object:
    """Turn parsed YAML lists into tuples, recursively, leaving scalars untouched.

    Strict Pydantic accepts only tuples for tuple fields, and immutable models need
    tuples anyway. This is structural only: "20" stays a string and is still rejected
    as an integer. For example, freeze_sequences({"ids": ["a"]}) == {"ids": ("a",)}.
    """
    if isinstance(value, list):
        return tuple(freeze_sequences(item) for item in cast(list[object], value))
    if isinstance(value, dict):
        mapping = cast(dict[object, object], value)
        return {key: freeze_sequences(item) for key, item in mapping.items()}
    return value
