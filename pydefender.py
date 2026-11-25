"""Read-only local security utilities."""
import argparse
import hashlib
import hmac
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


def fingerprint(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def summarize(path):
    counts = Counter()
    invalid = 0
    with path.open(encoding="utf-8") as stream:
        for line in stream:
            if not line.strip():
                continue
            try:
                event = json.loads(line)
                if not isinstance(event, dict):
                    raise ValueError("Expected object")
                level = str(event.get("level", "unknown")).lower()
                counts[level if level in {"debug", "info", "warning", "error", "critical"} else "unknown"] += 1
            except ValueError:
                invalid += 1
    return {"levels": dict(sorted(counts.items())), "invalid_lines": invalid}


def inventory(path):
    if not path.is_dir():
        raise ValueError("Expected a directory")
    results = []
    for item in sorted(path.iterdir()):
        if item.is_symlink() or not item.is_file():
            continue
        stat = item.stat()
        results.append({"name": item.name, "size_bytes": stat.st_size,
                        "modified_utc": datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat()})
    return results


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("hash", "verify", "log-summary", "inventory"):
        sub = commands.add_parser(name)
        sub.add_argument("path", type=Path)
        if name == "verify":
            sub.add_argument("expected")
    args = parser.parse_args(argv)
    try:
        if args.command == "hash":
            print(fingerprint(args.path))
        elif args.command == "verify":
            if not re.fullmatch(r"[0-9a-fA-F]{64}", args.expected):
                raise ValueError("Expected a 64-character SHA-256")
            matches = hmac.compare_digest(fingerprint(args.path), args.expected.lower())
            print("MATCH" if matches else "MISMATCH")
            return 0 if matches else 1
        else:
            result = summarize(args.path) if args.command == "log-summary" else inventory(args.path)
            print(json.dumps(result, indent=2, ensure_ascii=False))
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
