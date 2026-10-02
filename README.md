# 🇹🇯 Tajik Instruction Dataset

**English** | [Тоҷикӣ](#-тоҷикӣ)

High-quality **Tajik-language instruction-tuning dataset** for training and fine-tuning large language models (LLMs).

> Expanding Tajik vocabulary and conversational resources for AI · NLP · low-resource language research.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Language: Tajik](https://img.shields.io/badge/Language-Tajik%20(tg)-green.svg)](#)
[![Format: JSON](https://img.shields.io/badge/Format-JSON-orange.svg)](#)
[![Version](https://img.shields.io/badge/version-1.2.27-brightgreen.svg)](CHANGELOG.md)

---

## Why this dataset?

Tajik is a **low-resource language** in modern NLP. This project builds a clean, versioned, instruction-style corpus so developers and researchers can:

- Fine-tune chat / QA models in Tajik
- Build educational and civic-tech applications
- Study Central Asian language processing

**License:** MIT — free for commercial and research use.

---

## Quick start

```bash
git clone https://github.com/SharifzodaIbrohim/Database.git
cd Database

# Stats
python scripts/stats.py v.1.2.27/*.json

# Quality check
python scripts/quality_check.py v.1.2.27/seed_law.json

# Merge all seed files
python scripts/merge.py v.1.2.27/seed_all.json v.1.2.27/seed_*.json

# Train / val / test split (90/5/5)
python scripts/split.py v.1.2.27/seed_all.json

# Export to JSONL (for many training frameworks)
python scripts/to_jsonl.py v.1.2.27/seed_all.json data.jsonl
```

---

## Data format (v1.2.27+)

```json
{
  "id": "v127-0001",
  "instruction": "Question or task in Tajik",
  "input": "",
  "output": "Natural answer in Tajik",
  "category": "law",
  "difficulty": "easy",
  "quality_score": 5
}
```

| Field | Description |
|-------|-------------|
| `id` | Unique ID (e.g. `v127-0001`) |
| `instruction` | User question / task |
| `input` | Optional context or document |
| `output` | Model target answer |
| `category` | Topic label |
| `difficulty` | `easy` \| `medium` \| `hard` |
| `quality_score` | 1–5 (target ≥ 4) |

**Priority categories:** `law` · `finance` · `science` · `culture` · `health` · `language`

Older versions (`v.1.2.23`–`v.1.2.26`) use a simpler `{instruction, input, output}` schema and are kept for history.

Details: [docs/DATA_FORMAT.md](docs/DATA_FORMAT.md)

---

## Repository structure

```
Database/
├── README.md · LICENSE · METADATA.md · CHANGELOG.md · CONTENT_POLICY.md
├── DATASET_CARD.md          # Hugging Face dataset card draft
├── docs/DATA_FORMAT.md
├── scripts/                 # stats, dedup, merge, split, to_jsonl, quality_check
├── v.1.2.23 … v.1.2.26      # legacy schema (~2,925 examples)
└── v.1.2.27/                # current schema (80+ seed examples)
    ├── seed_law.json
    ├── seed_finance.json
    ├── seed_science.json
    ├── seed_culture.json
    ├── seed_health.json
    └── seed_language.json
```

**Total (approx.): ~3,000 examples** and growing.

---

## Content policy

**Allowed:** civic documents, finance, science & programming, culture (Navruz, Mehrgon, proverbs), health advice, language (definitions, synonyms, idioms).

**Not allowed:** religion, adult content, anti-state material, hate speech.

See [CONTENT_POLICY.md](CONTENT_POLICY.md).

---

## Roadmap

| Horizon | Target |
|---------|--------|
| Short-term | **5,000** high-quality examples |
| Medium-term | 15,000–20,000 |
| Long-term | 50,000+ + clean text corpus |

---

## Citation

```bibtex
@misc{tajik-instruction-dataset,
  author = {Sharifzoda, Ibrohim},
  title  = {Tajik Instruction Dataset},
  year   = {2026},
  url    = {https://github.com/SharifzodaIbrohim/Database}
}
```

---

## Contributing

1. Follow the schema in `docs/DATA_FORMAT.md`
2. Respect `CONTENT_POLICY.md`
3. Run `python scripts/quality_check.py your_file.json` before opening a PR
4. Prefer `quality_score` ≥ 4

---

## Author

**Sharifzoda Ibrohim** — [GitHub](https://github.com/SharifzodaIbrohim)

MIT License · Built to strengthen Tajik in the age of AI 🇹🇯

---

# 🇹🇯 Тоҷикӣ

**Датасети instruction-tuning забони тоҷикӣ** барои омӯзиш ва танзими моделҳои ҳуши маснӯӣ (LLM).

> Васеъкунии калимаҳо ва захираҳои гуфтугӯии тоҷикӣ барои AI · NLP · забонҳои камзахира.

## Чаро ин лоиҳа?

Тоҷикӣ дар NLP забони **камзахира** аст. Ин репозиторий корпуси тоза ва версиябандишуда месозад, то барномасозон ва муҳаққиқон:

- Моделҳои чат / саволу ҷавобро бо тоҷикӣ омӯзонанд
- Барномаҳои таълимӣ ва шаҳрвандӣ созанд
- Коркарди забонҳои Осиёи Марказиро омӯзанд

**Иҷозатнома:** MIT — ройгон барои тиҷорат ва таҳқиқот.

## Оғози зуд

```bash
git clone https://github.com/SharifzodaIbrohim/Database.git
cd Database
python scripts/stats.py v.1.2.27/*.json
python scripts/quality_check.py v.1.2.27/seed_law.json
python scripts/merge.py v.1.2.27/seed_all.json v.1.2.27/seed_*.json
python scripts/split.py v.1.2.27/seed_all.json
python scripts/to_jsonl.py v.1.2.27/seed_all.json data.jsonl
```

## Формат (v.1.2.27+)

```json
{
  "id": "v127-0001",
  "instruction": "Савол ё вазифа",
  "input": "",
  "output": "Ҷавоби табиӣ",
  "category": "law",
  "difficulty": "easy",
  "quality_score": 5
}
```

**Категорияҳои афзалият:** қонун · молия · илм · фарҳанг · саломатӣ · забон

**Манъ:** дин, порн, хиёнат ба давлат, гапҳои нолозим — нигаред ба [CONTENT_POLICY.md](CONTENT_POLICY.md)

## Ҳадафҳо

| Мӯҳлат | Ҳадаф |
|--------|--------|
| Кӯтоҳ | **5 000** мисоли сифатнок |
| Миёна | 15–20 ҳазор |
| Дароз | 50 ҳазор+ + корпуси матнӣ |

## Муаллиф

**Шарифзода Иброҳим** — [GitHub](https://github.com/SharifzodaIbrohim)

MIT License · Барои ғанӣ кардани забони тоҷикӣ дар ҷаҳони AI 🇹🇯
