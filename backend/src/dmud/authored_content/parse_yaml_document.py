import yaml

from dmud.authored_content.content_issue import ContentIssue
from dmud.authored_content.format_field_path import format_field_path
from dmud.authored_content.strict_yaml_loader import DuplicateYamlKey, StrictYamlLoader


def parse_yaml_document(path: str, text: str) -> object | ContentIssue:
    """Parse one YAML document, rejecting duplicate keys, without echoing its body.

    Returns the parsed value or a ContentIssue so expected failures stay data. For
    example, parse_yaml_document("npcs/mara.yaml", "kind: npc\\n").
    """
    try:
        return yaml.load(text, Loader=StrictYamlLoader)
    except DuplicateYamlKey as error:
        return ContentIssue(
            code="duplicate_key", file=path, field=format_field_path((error.key,))
        )
    except yaml.YAMLError, ValueError, RecursionError:
        return ContentIssue(code="invalid_yaml", file=path, field="")
