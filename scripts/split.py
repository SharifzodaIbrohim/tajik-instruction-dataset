#!/usr/bin/env python3
"""Тақсим ба train/validation/test (default 90/5/5)."""
import json
import random
import sys
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Usage: split.py input.json [train_ratio=0.9] [seed=42]")
        sys.exit(1)
    path = Path(sys.argv[1])
    ratio = float(sys.argv[2]) if len(sys.argv) > 2 else 0.9
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 42
    data = json.loads(path.read_text(encoding="utf-8"))
    random.seed(seed)
    random.shuffle(data)
    n = len(data)
    n_train = int(n * ratio)
    n_val = int(n * (1 - ratio) / 2)
    train, val, test = data[:n_train], data[n_train:n_train+n_val], data[n_train+n_val:]
    out_dir = path.parent / "splits"
    out_dir.mkdir(exist_ok=True)
    for name, part in [("train", train), ("validation", val), ("test", test)]:
        (out_dir / f"{name}.json").write_text(
            json.dumps(part, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        print(f"{name}: {len(part)}")

if __name__ == "__main__":
    main()
