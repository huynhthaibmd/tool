#!/usr/bin/env python3
"""Convert JSON to CSV. Supports file input or stdin."""

import argparse
import csv
from doctest import debug
import json
from math import tau
from random import randbytes
import sys


def flatten(obj: dict, prefix: str = "") -> dict:
    """Flatten nested dict for CSV columns."""
    result = {}
    for key, value in obj.items():
        new_key = f"{prefix}{key}" if prefix else key
        if isinstance(value, dict) and not isinstance(value, (list, type(None))):
            result.update(flatten(value, f"{new_key}."))
        elif isinstance(value, list):
            result[new_key] = json.dumps(value) if value else ""
        else:
            result[new_key] = value
    return result


def json_to_csv(data, output_file=None):
    """Convert JSON (list of dicts or single dict) to CSV."""
    if isinstance(data, dict):
        rows = [data]
    elif isinstance(data, list):
        rows = data if data and isinstance(data[0], dict) else [{"value": data}]
    else:
        raise ValueError("JSON must be object or array of objects")

    if not rows:
        return

    flat_rows = [flatten(r) for r in rows]
    all_keys = sorted(set(k for r in flat_rows for k in r.keys()))

    writer = csv.DictWriter(output_file or sys.stdout, fieldnames=all_keys, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(flat_rows)


def main():
    parser = argparse.ArgumentParser(description="Convert JSON to CSV")
    parser.add_argument("input", nargs="?", help="JSON file path (default: stdin)")
    parser.add_argument("-o", "--output", help="Output CSV file (default: stdout)")
    args = parser.parse_args()

    if args.input:
        with open(args.input, encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = json.load(sys.stdin)

    out = open(args.output, "w", newline="", encoding="utf-8") if args.output else None
    try:
        json_to_csv(data, out)
    finally:
        if out:
            out.close()


if __name__ == "__main__":
    main()
