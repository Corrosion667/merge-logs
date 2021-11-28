"""This is a module to test script for error raising."""

import os

import pytest
from merge_logs.merge_logs import merge_logs

UNACCESSABLE_RIGHTS = 000


def test_merge_logs_wrong_formats(tmp_path):
    """Do not allow to parse unsupported formats.

    Args:
        tmp_path: temporary path for testing.
    """
    result_path = os.path.join(tmp_path, 'result.jsonl')
    with pytest.raises(ValueError):
        merge_logs(
            'tests/fixtures/unsupported_format.txt',
            'tests/fixtures/1.jsonl',
            result_path,
        )


def test_merge_logs_wrong_path(tmp_path):
    """Do not allow to pass to script non-existent paths.

    Args:
        tmp_path: temporary path for testing.
    """
    result_path = os.path.join(tmp_path, 'result.jsonl')
    with pytest.raises(FileNotFoundError):
        merge_logs(
            'tests/fixtures/3.jsonl',
            'tests/fixtures/1.jsonl',
            result_path,
        )


def test_unaccessable(tmp_path):
    """Do not allow to pass to script unaccessable files.

    Args:
        tmp_path: temporary path for testing.
    """
    unaccessable_path = os.path.join(tmp_path, 'check.jsonl')
    with open(unaccessable_path, 'w') as test_file:
        test_file.write('Hello, world!\n')
    os.chmod(unaccessable_path, UNACCESSABLE_RIGHTS)
    result_path = os.path.join(tmp_path, 'result.jsonl')
    with pytest.raises(PermissionError):
        merge_logs(
            unaccessable_path,
            'tests/fixtures/1.jsonl',
            result_path,
        )
