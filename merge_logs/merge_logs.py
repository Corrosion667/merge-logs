#!/usr/bin/env python3
"""This is a module for merging JSONLs."""

import argparse
import json
import os
import pathlib
import time
from heapq import merge
from operator import itemgetter

DEFAULT_FILENAME = 'merged.jsonl'
default_folder = os.getcwd()
default_path = os.path.join(default_folder, DEFAULT_FILENAME)


def parse_args() -> argparse.Namespace:
    """Create CLI.

    Returns:
        arguments for script.
    """
    parser = argparse.ArgumentParser(description='Tool to merge log files.')

    parser.add_argument(
        'first_file',
        type=str,
        help='path to first log file',
    )

    parser.add_argument(
        'second_file',
        type=str,
        help='path to second log file',
    )

    parser.add_argument(
        '-o',
        '--output',
        type=str,
        default=default_path,
        help='desired path to merged log file',
    )

    return parser.parse_args()


def read_in_lines(file_object):
    """Lazy function (generator) to read large file line by line.

    Args:
        file_object: opened file.

    Yields:
        Line of the log file.
    """
    while True:
        line = file_object.readline()
        if not line:
            break
        yield json.loads(line)


def open_jsonl(path: str) -> None:
    """Open file with logs and check it.

    Args:
        path: path to file.

    Raises:
        ValueError: if extension of file is unsupported.
        FileNotFoundError: if file path is invalid.
        PermissionError: if user don't have access.

    """
    file_extension = os.path.splitext(path)[-1].lower()
    if file_extension != '.jsonl':
        raise ValueError('Unsupported extension of file: {0}'.format(path))
    try:
        open(path)
    except FileNotFoundError:
        raise FileNotFoundError(
            'Please make sure that the {0} is correct path'.format(path),
        )
    except PermissionError:
        raise PermissionError(
            "You don't have permission to read that file: {0}".format(path),
        )
    except OSError:
        raise OSError('Unknow error acquired.')


def merge_logs(path1: str, path2: str, path_merged: str = default_path) -> None:
    """Create a merged log file in a specified directory from two files.

    Args:
        path1: path to the first file.
        path2: path to the second file.
        path_merged: path to the merged fie.

    Raises:
        PermissionError: if user don't have access.
    """
    pathlib.Path(os.path.dirname(path_merged)).mkdir(
        parents=True, exist_ok=True,
    )
    first_file, second_file = open(path1), open(path2)
    first_logs = read_in_lines(first_file)
    second_logs = read_in_lines(second_file)
    merged_logs = merge(
        first_logs,
        second_logs,
        key=itemgetter('timestamp'),
    )
    try:
        with open(path_merged, 'w') as merged_file:
            for log in merged_logs:
                merged_file.write('{0}\n'.format(json.dumps(log)))
            first_file.close()
            second_file.close()
    except PermissionError:
        first_file.close()
        second_file.close()
        raise PermissionError(
            "You don't have to access this folder: {0}".format(
                os.path.dirname(path_merged),
            ),
        )
    except OSError:
        first_file.close()
        second_file.close()
        raise OSError('Unknow error acquired.')


def main() -> None:
    """Execute the script."""
    args = parse_args()
    t0 = time.time()
    path1, path2, path_merged = args.first_file, args.second_file, args.output
    try:
        merge_logs(path1, path2, path_merged)
        print(f'Merging finished in {time.time() - t0:0f} sec')  # noqa: WPS237, WPS305, E501
    except Exception as exc:
        print(str(exc))


if __name__ == '__main__':
    main()
