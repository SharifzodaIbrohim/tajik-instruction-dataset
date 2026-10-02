# 🇹🇯 Database — Базаи додаҳои калимаҳо ва корпуси забони тоҷикӣ

**Лоиҳаи васеъкунӣ ва омодасозии базаи додаҳои калимаҳои тоҷикӣ**

Барои омӯзиши моделҳои ҳуши маснӯӣ (instruction-tuning), NLP ва захираҳои забони тоҷикӣ.

---

## 📁 Сохтор

```
Database/
├── README.md · LICENSE · METADATA.md · CHANGELOG.md · CONTENT_POLICY.md
├── docs/DATA_FORMAT.md
├── scripts/          # stats, dedup, merge, split, to_jsonl, quality_check
├── v.1.2.23 … v.1.2.26   # схемаи кӯҳна (таърихӣ)
└── v.1.2.27/             # схемаи нав ← ОХИРИН
    ├── seed_all.json
    └── seed_{law,finance,science,culture,health,language}.json
```

---

## 🆕 v.1.2.27 — схемаи нав

```json
{
  "id": "v127-0001",
  "instruction": "...",
  "input": "",
  "output": "...",
  "category": "law",
  "difficulty": "easy",
  "quality_score": 5
}
```

**Афзалият:** қонун · молия · илм · фарҳанг · саломатӣ · забон

**Манъ:** дин, порн, хиёнат ба давлат, гапҳои нолозим дар бораи давлат

---

## 🎯 Ҳадафҳо

| Мӯҳлат | Ҳадаф |
|--------|--------|
| Кӯтоҳ | **5 000** мисоли сифатнок |
| Миёна | 15–20 ҳазор |
| Дароз | 50 ҳазор+ + корпуси матнӣ |

---

## 🛠️ Скриптҳо

```bash
python scripts/stats.py v.1.2.27/*.json
python scripts/quality_check.py v.1.2.27/seed_all.json
python scripts/dedup.py in.json out.json
python scripts/merge.py out.json a.json b.json
python scripts/split.py v.1.2.27/seed_all.json    # 90/5/5
python scripts/to_jsonl.py in.json out.jsonl
```

---

## 📊 Омор

| Версия | Схема | Мисолҳо |
|--------|-------|--------|
| v.1.2.23–26 | кӯҳна | ~2 925 |
| **v.1.2.27** | **нав** | **80+** |

Тафсилот → [METADATA.md](METADATA.md) · [CHANGELOG.md](CHANGELOG.md)

---

## 📜 Иҷозатнома

**MIT License**

**Созанда:** [Sharifzoda Ibrohim](https://github.com/SharifzodaIbrohim)  
**Мақсад:** Ғанӣ кардани забони тоҷикӣ дар ҷаҳони ҳуши маснӯӣ 🇹🇯
