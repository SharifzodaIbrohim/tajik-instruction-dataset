#!/usr/bin/env python3
"""Санҷиши автоматии сифат: дарозӣ, такрор, майдонҳои ҳатмӣ, русӣ-зиёд."""
import json
import re
import sys
from pathlib import Path

REQUIRED = {"id", "instruction", "output", "category", "difficulty"}
VALID_CATS = {
    "law", "finance", "science", "culture", "health", "language",
    "technology", "education", "family", "food", "travel", "safety", "work", "daily"
}
VALID_DIFF = {"easy", "medium", "hard"}
RU_HINT = re.compile(r"[ыёъ]")

def check(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    errors, warnings = [], []
    seen_inst, seen_id = set(), set()
    for i, e in enumerate(data):
        loc = e.get("id", f"index-{i}")
        missing = REQUIRED - set(e.keys())
        if missing:
            errors.append(f"{loc}: майдонҳои гум: {missing}")
        if e.get("id") in seen_id:
            errors.append(f"{loc}: id такрор")
        seen_id.add(e.get("id"))
        inst = (e.get("instruction") or "").strip()
        out = (e.get("output") or "").strip()
        if not inst:
            errors.append(f"{loc}: instruction холӣ")
        if not out:
            errors.append(f"{loc}: output холӣ")
        if len(out) < 20:
            warnings.append(f"{loc}: output хеле кӯтоҳ ({len(out)})")
        if len(out) > 800:
            warnings.append(f"{loc}: output хеле дароз ({len(out)})")
        key = inst.lower()
        if key in seen_inst:
            warnings.append(f"{loc}: instruction такрор")
        seen_inst.add(key)
        if e.get("category") not in VALID_CATS:
            warnings.append(f"{loc}: category номаълум: {e.get('category')}")
        if e.get("difficulty") not in VALID_DIFF:
            errors.append(f"{loc}: difficulty нодуруст: {e.get('difficulty')}")
        qs = e.get("quality_score")
        if qs is not None and (not isinstance(qs, int) or qs < 1 or qs > 5):
            errors.append(f"{loc}: quality_score бояд 1–5 бошад")
        if RU_HINT.search(out) and out.count("ы") > 2:
            warnings.append(f"{loc}: эҳтимоли русӣ-зиёд дар output")
    print(f"Файл: {path}")
    print(f"Мисолҳо: {len(data)}")
    print(f"Хатоҳо: {len(errors)}")
    for x in errors[:20]:
        print(f"  ERROR: {x}")
    print(f"Огоҳиҳо: {len(warnings)}")
    for x in warnings[:20]:
        print(f"  WARN: {x}")
    return len(errors) == 0

if __name__ == "__main__":
    ok = True
    for p in sys.argv[1:]:
        if not check(p):
            ok = False
    sys.exit(0 if ok else 1)
