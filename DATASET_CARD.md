---
language:
  - tg
  - en
license: mit
task_categories:
  - text-generation
  - question-answering
  - conversational
pretty_name: Tajik Instruction Dataset
tags:
  - tajik
  - tajikistan
  - nlp
  - instruction-tuning
  - llm
  - low-resource
  - central-asia
  - dataset
size_categories:
  - 1K<n<10K
---

# Tajik Instruction Dataset

Instruction-tuning dataset for the **Tajik language** (tg) — a low-resource language of Central Asia.

## Dataset summary

| Item | Value |
|------|--------|
| Language | Tajik (tg) |
| Task | Instruction following / QA |
| Format | JSON (`id`, `instruction`, `input`, `output`, `category`, `difficulty`, `quality_score`) |
| License | MIT |
| Size | ~3,000 examples (growing toward 5,000+) |
| Splits | train 90% / validation 5% / test 5% |

## Categories

`law` · `finance` · `science` · `culture` · `health` · `language`

## How to use

```python
import json
from pathlib import Path

data = json.loads(Path("v.1.2.27/seed_law.json").read_text(encoding="utf-8"))
for ex in data[:3]:
    print(ex["instruction"], "→", ex["output"][:80])
```

Or convert to JSONL:

```bash
python scripts/to_jsonl.py v.1.2.27/seed_law.json train.jsonl
```

## Content policy

No religion, adult content, or anti-state material. See `CONTENT_POLICY.md`.

## Citation

```bibtex
@misc{tajik-instruction-dataset,
  author = {Sharifzoda, Ibrohim},
  title  = {Tajik Instruction Dataset},
  year   = {2026},
  url    = {https://github.com/SharifzodaIbrohim/Database}
}
```

## Author

Sharifzoda Ibrohim — https://github.com/SharifzodaIbrohim
