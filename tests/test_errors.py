"""This is a module to test script for error raising."""

import pytest
from merge_logs.merge_logs import merge_logs


def test_merge_logs_wrong_formats():
    """Do not allow to parse unsupported formats."""
    with pytest.raises(ValueError):
        merge_logs(
            'tests/fixtures/unsupported_format.txt',
            'tests/fixtures/1.jsonl',
        )


def test_merge_logs_wrong_path():
    """Do not allow to pass to script non-existent paths."""
    with pytest.raises(FileNotFoundError):
        merge_logs(
            'tests/fixtures/3.jsonl',
            'tests/fixtures/1.jsonl',
        )
