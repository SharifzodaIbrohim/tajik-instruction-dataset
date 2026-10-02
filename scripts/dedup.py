#!/usr/bin/env python3
"""Тоза кардани такрорҳо аз рӯи instruction (нормализатсия)."""
import json
import sys
from pathlib import Path

def norm(s):
    return " ".join(s.lower().split())

def main():
    if len(sys.argv) < 3:
        print("Usage: dedup.py input.json output.json")
        sys.exit(1)
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    seen, unique = set(), []
    for e in data:
        key = norm(e.get("instruction", ""))
        if key and key not in seen:
            seen.add(key)
            unique.append(e)
    Path(sys.argv[2]).write_text(
        json.dumps(unique, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"{len(data)} → {len(unique)} (нест шуд: {len(data)-len(unique)})")

if __name__ == "__main__":
    main()
