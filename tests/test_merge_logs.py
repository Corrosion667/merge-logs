"""This is a module to test merge-logs script."""
import os

from merge_logs.merge_logs import merge_logs


def test_merge_logs(tmp_path):
    """Test main script.

    Args:
        tmp_path: temporary path for testing.
    """
    with open('tests/fixtures/result.jsonl') as fixture_file:
        fixture_logs = fixture_file.read()
    result_path = os.path.join(tmp_path, 'result.jsonl')
    merge_logs('tests/fixtures/1.jsonl', 'tests/fixtures/2.jsonl', result_path)
    with open(result_path) as result_file:
        result_logs = result_file.read()
    assert fixture_logs == result_logs
