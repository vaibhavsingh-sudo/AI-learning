# Jupyter Notebooks

## Overview

Jupyter Notebooks are interactive documents that combine:

- Executable Python code
- Markdown documentation
- Visualizations
- Tables
- Images
- Outputs

They are the standard environment for AI research, data science, and machine learning experimentation.

---

## Why Use Jupyter Notebooks?

- Rapid experimentation
- Inline visualization
- Interactive debugging
- Mix code with explanations
- Easy sharing
- Great for AI research and Kaggle competitions

---

# Notebook Structure

A notebook consists of multiple cells.

```
Notebook
│
├── Markdown Cell
├── Code Cell
├── Code Cell
├── Markdown Cell
└── Output
```

Each cell is independent but shares the same Python kernel.

---

# The Kernel

The kernel is a background Python process that:

- Executes code
- Stores variables in memory
- Handles imports
- Returns outputs

All notebook cells share the same kernel.

Restarting the kernel clears all variables from memory.

---

# Installing Jupyter

## JupyterLab

```bash
pip install jupyterlab
jupyter lab
```

Recommended for most AI workflows.

---

## Jupyter Notebook

```bash
pip install notebook
jupyter notebook
```

Lightweight interface.

---

## VS Code

Install the **Jupyter Extension** from the VS Code Marketplace.

Ideal if VS Code is your primary editor.

---

# Keyboard Shortcuts

## Command Mode (Esc)

| Shortcut | Action |
|----------|--------|
| Shift + Enter | Run current cell |
| A | Insert cell above |
| B | Insert cell below |
| DD | Delete cell |
| M | Convert to Markdown |
| Y | Convert to Code |
| Z | Undo deleted cell |
| Ctrl + Shift + H | Show all shortcuts |

---

## Edit Mode (Enter)

| Shortcut | Action |
|----------|--------|
| Tab | Autocomplete |
| Shift + Tab | Function signature |
| Ctrl + / | Toggle comment |

---

# Cell Types

## Code Cell

Runs Python code.

Example:

```python
import numpy as np

data = np.random.randn(1000)

data.mean()
```

---

## Markdown Cell

Used for documentation.

Supports:

- Headers
- Bold
- Italic
- Tables
- Images
- Lists
- LaTeX equations

Example:

```markdown
# Model Training

This notebook trains a neural network.
```

---

# Magic Commands

Magic commands begin with:

```
%
```

or

```
%%
```

They are specific to Jupyter.

---

## %timeit

Runs a statement many times and reports the average execution time.

Example:

```python
%timeit np.random.randn(10000)
```

Use for:

- Benchmarking small code snippets
- Comparing implementations

---

## %%time

Measures the execution time of an entire cell.

Example:

```python
%%time

model.fit(...)
```

Use for:

- Training models
- Long-running computations

---

## %matplotlib inline

```python
%matplotlib inline
```

Displays Matplotlib plots directly below the cell.

---

## !pip install

Runs shell commands.

Example:

```python
!pip install scikit-learn
```

---

## %env

Displays environment variables.

Example:

```python
%env CUDA_VISIBLE_DEVICES
```

---

# Displaying Data

Jupyter automatically displays the last object in a cell.

Example:

```python
import pandas as pd

df = pd.DataFrame(...)
df
```

Instead of plain text, Jupyter renders a formatted HTML table.

---

# Inline Plots

Example:

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(8,4))
plt.plot([1,2,3,4],[1,4,2,3])
plt.title("Inline Plot")
plt.show()
```

The graph appears directly below the cell.

---

# Displaying Images

```python
from IPython.display import Image, display

display(Image(filename="architecture.png"))
```

Useful for:

- Model architectures
- Dataset samples
- Visual explanations

---

# Google Colab

Google Colab is a cloud-hosted Jupyter Notebook.

Benefits:

- Free GPU
- Free TPU
- Pre-installed ML libraries
- Google Drive integration

Common limitations:

- Sessions expire
- Files are temporary unless saved
- Limited free GPU usage

---

# Notebooks vs Scripts

| Use Notebooks | Use Scripts |
|--------------|-------------|
| Data exploration | Production code |
| Model prototyping | Reusable utilities |
| Visualizations | Training pipelines |
| Experiments | Packages |
| Reports | Scheduled tasks |

Rule:

> Explore in notebooks. Ship in scripts.

---

# Common Notebook Problems

## Out-of-Order Execution

Running cells in random order creates hidden dependencies.

Solution:

```
Kernel → Restart & Run All
```

---

## Hidden State

Variables remain in memory after deleting cells.

Solution:

Restart the kernel regularly.

---

## Memory Leaks

Large datasets remain allocated.

Solution:

```python
del variable
```

or restart the kernel.

---

# Exercises

### Exercise 1

Install JupyterLab and launch it.

---

### Exercise 2

Create a notebook containing:

- Markdown
- Python code
- A DataFrame
- A Matplotlib graph

---

### Exercise 3

Use:

```python
%timeit
```

to compare:

- List comprehension
- NumPy array generation

---

### Exercise 4

Upload the notebook to Google Colab and execute it using a free GPU.

---

# Post-Lesson Quiz

### 1. What does the Jupyter kernel do?

**Explanation**

The kernel is a separate Python process that executes notebook cells and stores variables in memory.

---

### 2. What is the difference between `%timeit` and `%%time`?

**Explanation**

- `%timeit` executes many times and reports an average.
- `%%time` executes once and reports total execution time.

---

### 3. Why should you run **Restart & Run All** before sharing a notebook?

**Explanation**

It verifies that every cell executes successfully from top to bottom without relying on hidden state.

---

### 4. When should code be moved into a `.py` script?

**Explanation**

Reusable utilities, production code, and training pipelines should be moved into Python scripts.

---

# Key Terms

| Term | Meaning |
|------|---------|
| Kernel | Background Python process executing notebook cells |
| Cell | Individual executable or markdown block |
| Markdown | Formatted documentation inside notebooks |
| Magic Command | Special Jupyter command beginning with `%` or `%%` |
| `.ipynb` | Notebook file format |

---

# Quick Facts

- Jupyter is the standard environment for AI experimentation.
- All notebook cells share one kernel.
- `%timeit` benchmarks code.
- `%%time` measures an entire cell.
- `%matplotlib inline` displays graphs below cells.
- Restart the kernel frequently to avoid hidden state.
- Explore in notebooks, ship in scripts.

---

# Files Used

```
notebook_tips.py
outputs/prompt-notebook-helper.md
```

---

# Summary

In this lesson you learned:

- How Jupyter Notebooks work.
- The role of the kernel.
- Code vs Markdown cells.
- Magic commands.
- Inline plotting.
- Google Colab.
- Notebook best practices.
- Common pitfalls.
- When to use notebooks versus Python scripts.