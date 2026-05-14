"""Observability helper tests."""

from fastapi_langchain_service.observability import scrub_metadata


def test_scrub_metadata_redacts_sensitive_values() -> None:
    metadata = {"trace_id": "abc", "api_token": "secret"}

    assert scrub_metadata(metadata) == {"trace_id": "abc", "api_token": "[redacted]"}
