#!/usr/bin/env python3
"""Омори датасет — шумора, категория, difficulty, quality_score."""
import json
import sys
from pathlib import Path
from collections import Counter

def load_jsons(paths):
    items = []
    for p in paths:
        data = json.loads(Path(p).read_text(encoding="utf-8"))
        if isinstance(data, list):
            items.extend(data)
        else:
            items.append(data)
    return items

def main():
    paths = sys.argv[1:] or list(Path(".").rglob("*.json"))
    items = load_jsons(paths)
    print(f"Ҷамъ: {len(items)} мисол")
    if not items:
        return
    cats = Counter(e.get("category", "?") for e in items)
    diffs = Counter(e.get("difficulty", "?") for e in items)
    scores = Counter(e.get("quality_score", "?") for e in items)
    print("\nКатегория:")
    for k, v in sorted(cats.items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")
    print("\nDifficulty:")
    for k, v in sorted(diffs.items()):
        print(f"  {k}: {v}")
    print("\nQuality score:")
    for k, v in sorted(scores.items()):
        print(f"  {k}: {v}")
    lens = [len(e.get("output", "")) for e in items]
    print(f"\nДарозии output: min={min(lens)} avg={sum(lens)//len(lens)} max={max(lens)}")

if __name__ == "__main__":
    main()
