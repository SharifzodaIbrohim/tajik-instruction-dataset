#!/usr/bin/env python3
"""Якҷоя кардани якчанд JSON ба як файл."""
import json
import sys
from pathlib import Path

def main():
    if len(sys.argv) < 3:
        print("Usage: merge.py out.json in1.json [in2.json ...]")
        sys.exit(1)
    out, *ins = sys.argv[1:]
    merged = []
    for p in ins:
        data = json.loads(Path(p).read_text(encoding="utf-8"))
        merged.extend(data if isinstance(data, list) else [data])
    Path(out).write_text(
        json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Merged {len(ins)} files → {len(merged)} examples → {out}")

if __name__ == "__main__":
    main()
