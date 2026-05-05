"""Small observability helpers for request metadata."""

from collections.abc import Mapping


def scrub_metadata(metadata: Mapping[str, str]) -> dict[str, str]:
    """Return metadata safe for logging or prompt context."""

    sensitive_markers = ("key", "secret", "token", "password")
    cleaned: dict[str, str] = {}
    for name, value in metadata.items():
        if any(marker in name.lower() for marker in sensitive_markers):
            cleaned[name] = "[redacted]"
        else:
            cleaned[name] = value
    return cleaned
