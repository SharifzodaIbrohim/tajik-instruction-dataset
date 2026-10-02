# Data Format / Формати маълумот

**English** | [Тоҷикӣ](#тоҷикӣ)

---

## English

### Schema (v1.2.27+)

Each JSON file is an array of objects:

```json
[
  {
    "id": "v127-0001",
    "instruction": "Question or task",
    "input": "",
    "output": "Answer",
    "category": "law",
    "difficulty": "easy",
    "quality_score": 5
  }
]
```

| Field | Description | Required |
|-------|-------------|----------|
| `id` | Unique ID (`v127-0001`) | Yes |
| `instruction` | User question / task | Yes |
| `input` | Optional context or document | No |
| `output` | Target answer | Yes |
| `category` | Topic label | Yes |
| `difficulty` | `easy` \| `medium` \| `hard` | Yes |
| `quality_score` | 1–5 (aim ≥ 4) | Recommended |

### Priority categories

| category | Topic |
|----------|--------|
| `law` | Documents, citizen rights, taxes, passport |
| `finance` | Banking, loans, business, labor market |
| `science` | Physics, chemistry, programming, AI |
| `culture` | Poetry, prose, proverbs, Navruz, Mehrgon |
| `health` | Practical health & mental health advice |
| `language` | Definitions, synonyms, antonyms, idioms |

Also used: `technology`, `education`, `family`, `food`, `travel`, `safety`, `work`, `daily`

### Legacy schema (v1.2.23 – v1.2.26)

```json
{ "instruction": "...", "input": "", "output": "..." }
```

Kept for historical versions.

### Splits

`scripts/split.py` → train 90% / validation 5% / test 5%

### Content policy

See [CONTENT_POLICY.md](../CONTENT_POLICY.md)

---

## Тоҷикӣ

### Схемаи v.1.2.27+

| Майдон | Тавсиф | Ҳатмӣ |
|--------|--------|-------|
| `id` | Рақами ягона | Ҳа |
| `instruction` | Савол / дархост | Ҳа |
| `input` | Контекст (холӣ агар нест) | Не |
| `output` | Ҷавоб | Ҳа |
| `category` | Категория | Ҳа |
| `difficulty` | easy / medium / hard | Ҳа |
| `quality_score` | 1–5 | Тавсия |

**Афзалият:** law · finance · science · culture · health · language

Версияҳои кӯҳна (`v.1.2.23`–`26`) танҳо `instruction` / `input` / `output` доранд.
