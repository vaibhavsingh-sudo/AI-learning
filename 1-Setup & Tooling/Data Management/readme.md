# Data Management with Hugging Face Datasets

## Install Required Libraries

```bash
pip install datasets huggingface_hub
```

---

## Load a Dataset

```python
from datasets import load_dataset

dataset = load_dataset("stanfordnlp/imdb")

print(dataset)
print(dataset["train"][0])
```

Downloads the dataset once and caches it locally.

---

## Stream Large Datasets

```python
from datasets import load_dataset

dataset = load_dataset(
    "wikimedia/wikipedia",
    "20220301.en",
    split="train",
    streaming=True
)

for i, example in enumerate(dataset):
    print(example["title"])
    if i >= 4:
        break
```

Streaming loads data row-by-row without downloading the entire dataset.

---

## Convert Dataset Formats

```python
from datasets import load_dataset

dataset = load_dataset("stanfordnlp/imdb", split="train")

dataset.to_csv("imdb_train.csv")
dataset.to_json("imdb_train.json")
dataset.to_parquet("imdb_train.parquet")
```

---

## Create Train / Validation / Test Split

```python
from datasets import load_dataset

dataset = load_dataset("stanfordnlp/imdb", split="train")

split = dataset.train_test_split(test_size=0.2, seed=42)
train_val = split["train"].train_test_split(test_size=0.125, seed=42)

train_ds = train_val["train"]
val_ds = train_val["test"]
test_ds = split["test"]

print(f"Train : {len(train_ds)}")
print(f"Val   : {len(val_ds)}")
print(f"Test  : {len(test_ds)}")
```

Always use a fixed **seed** for reproducible splits.

---

## Download & Cache Models

```python
from huggingface_hub import hf_hub_download, snapshot_download

model_path = hf_hub_download(
    repo_id="sentence-transformers/all-MiniLM-L6-v2",
    filename="config.json"
)

print(model_path)

model_dir = snapshot_download(
    "sentence-transformers/all-MiniLM-L6-v2"
)

print(model_dir)
```

Models are cached automatically after the first download.

---

## Ignore Large Files (.gitignore)

```gitignore
*.bin
*.safetensors
*.pt
*.onnx

data/*.parquet
data/*.csv

models/
```

---

## Git LFS

```bash
git lfs install
git lfs track "*.bin"
git lfs track "*.safetensors"
git add .gitattributes
```

---

## DVC

```bash
pip install dvc

dvc init

dvc add data/training_set.parquet

git add data/training_set.parquet.dvc data/.gitignore

git commit -m "Track training data with DVC"
```

---

## Hugging Face Cache Location

```python
import os

cache = os.path.expanduser(
    "~/.cache/huggingface/datasets/"
)

print(cache)
```

---

# Dataset Formats

| Format | Size | Speed | Best For |
|---------|------|-------|----------|
| CSV | Large | Slow | Human-readable |
| JSON | Large | Slow | APIs & nested data |
| Parquet | Small | Fast | ML datasets |
| Arrow | Small | Fastest | In-memory processing |

---

# Version Control Options

| Method | Complexity | Best For |
|---------|------------|----------|
| `.gitignore` | Low | Personal projects |
| Git LFS | Medium | Large model files |
| DVC | High | Reproducible ML experiments |

---

# Datasets Used in This Course

| Dataset | Purpose |
|---------|---------|
| IMDB | Text Classification |
| WikiText | Language Modeling |
| SQuAD | Question Answering |
| Common Crawl | Large-scale Text Processing |
| MNIST | Image Classification |
| COCO | Multimodal Learning |

---

# Post-Lesson Quiz

### 1. What advantage does Parquet have over CSV?

- Human-readable
- ✅ Smaller files & faster reads
- More data types
- Spreadsheet editing

**Explanation**

Parquet is a **columnar binary format** that compresses data efficiently and enables much faster reads than CSV.

---

### 2. What does `streaming=True` do?

- Faster downloads
- ✅ Loads data row-by-row without downloading everything
- Streams video
- Live updates

**Explanation**

Streaming creates an **IterableDataset**, keeping memory usage constant regardless of dataset size.

---

### 3. When should you use DVC?

- Small datasets
- ✅ Reproducible experiments across machines
- Personal projects only
- CSV-only projects

**Explanation**

DVC versions datasets using lightweight pointer files while storing the actual data remotely, making experiments reproducible.

---

# Quiz Score

✅ **3 / 3 Correct**

---

# Key Terms

| Term | Meaning |
|------|---------|
| Dataset Split | Train / Validation / Test subsets |
| Streaming | Process data without full download |
| Parquet | Compressed columnar storage |
| Arrow | Fast in-memory columnar format |
| Git LFS | Git extension for large files |
| DVC | Version control for datasets & models |
| Cache | Local copy of downloaded datasets |

---

# Quick Facts

- Install with **`pip install datasets huggingface_hub`**
- Datasets are cached in **`~/.cache/huggingface/`**
- Use **`streaming=True`** for huge datasets.
- **Parquet** is the preferred storage format for ML.
- **Arrow** is the in-memory format used by the `datasets` library.
- Always use a fixed **seed** for reproducible dataset splits.
- Use **.gitignore** for simple projects, **Git LFS** for large model files, and **DVC** for reproducible ML experiments.