#!/usr/bin/env python3
"""JSON array → JSONL (як объект дар як хат)."""
import json
import sys
from pathlib import Path

def main():
    if len(sys.argv) < 3:
        print("Usage: to_jsonl.py input.json output.jsonl")
        sys.exit(1)
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        for e in data:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")
    print(f"{len(data)} lines → {sys.argv[2]}")

if __name__ == "__main__":
    main()
