# Terminal & Shell for AI Engineering

## Know Your Shell

```bash
echo $SHELL
```

Common shells:
- bash
- zsh

---

## Basic Navigation

```bash
cd ~/projects/ai-engineering-from-scratch
pwd
ls -la
```

Useful Shortcuts

- `Ctrl + R` → Search command history
- `Ctrl + L` → Clear terminal
- `Ctrl + C` → Stop current command
- `Ctrl + Z` → Suspend command (`fg` to resume)

---

## Piping & Redirects

### Count occurrences

```bash
cat train.log | grep "loss" | wc -l
```

### Extract loss values

```bash
grep "loss:" train.log | awk '{print $NF}' > losses.txt
```

### Monitor errors in real time

```bash
tail -f train.log | grep --line-buffered "ERROR"
```

### Sort experiments

```bash
grep "final_accuracy" results/*.log | sort -t= -k2 -n -r
```

### Redirect Output

```bash
python train.py > output.log 2> errors.log
```

### Redirect Everything

```bash
python train.py > train.log 2>&1
```

---

## Redirect Symbols

| Symbol | Meaning |
|--------|---------|
| `>` | Overwrite output |
| `>>` | Append output |
| `2>` | Redirect errors |
| `2>&1` | Merge stdout & stderr |
| `|` | Pipe output |

---

## Background Processes

### Run in background

```bash
python train.py &
```

### Survive terminal close

```bash
nohup python train.py > train.log 2>&1 &
```

### Running jobs

```bash
jobs
ps aux | grep train.py
```

### Resume

```bash
fg %1
```

### Kill process

```bash
kill %1
```

or

```bash
kill $(pgrep -f "train.py")
```

---

## Background Methods

| Method | Terminal Safe | Reattach |
|---------|---------------|----------|
| `command &` | ❌ | ❌ |
| `nohup command &` | ✅ | ❌ |
| `tmux` | ✅ | ✅ |

---

# tmux

### Install

```bash
# Ubuntu
sudo apt install tmux

# macOS
brew install tmux
```

### Commands

```bash
tmux new -s training
tmux attach -t training
tmux ls
tmux kill-session -t training
```

### Shortcuts

- `Ctrl+B` `"` → Horizontal split
- `Ctrl+B` `%` → Vertical split
- `Ctrl+B` `Arrow` → Switch pane
- `Ctrl+B` `d` → Detach session

---

## AI Workflow Example

```bash
tmux new -s train

python train.py --epochs 100 --lr 1e-4

watch -n1 nvidia-smi

tail -f logs/experiment.log
```

Detach with:

```
Ctrl+B then d
```

Reattach:

```bash
tmux attach -t train
```

---

# Monitoring

### CPU

```bash
htop
```

### GPU

```bash
nvtop
```

### NVIDIA Status

```bash
nvidia-smi
```

### Live GPU Monitor

```bash
watch -n1 nvidia-smi
```

### GPU Processes

```bash
nvidia-smi --query-compute-apps=pid,name,used_memory --format=csv
```

---

## htop Shortcuts

- `F6` → Sort
- `F5` → Tree view
- `F9` → Kill process
- `/` → Search process

---

# SSH

### Connect

```bash
ssh user@gpu-box
```

### With SSH Key

```bash
ssh -i ~/.ssh/my_gpu_key user@gpu-box
```

### Upload File

```bash
scp model.pt user@gpu-box:~/models/
```

### Download File

```bash
scp user@gpu-box:~/results/metrics.json ./
```

### Sync Folder

```bash
rsync -avz ./data/ user@gpu-box:~/data/
```

### Port Forward

```bash
ssh -L 8888:localhost:8888 user@gpu-box
```

Open:

```
http://localhost:8888
```

---

# Useful Aliases

```bash
alias gpu='nvidia-smi --query-gpu=index,name,utilization.gpu,memory.used,memory.total,temperature.gpu --format=csv,noheader'

alias killtraining='pkill -f "python.*train"'

alias ae='source .venv/bin/activate'

alias watchloss='tail -f logs/*.log | grep --line-buffered "loss"'
```

---

# Common AI Commands

### Log Everything

```bash
python train.py 2>&1 | tee train.log
```

### Compare Logs

```bash
diff <(grep "accuracy" exp1.log) <(grep "accuracy" exp2.log)
```

### Largest Model Files

```bash
find . -name "*.pt" -o -name "*.safetensors" | xargs du -h | sort -rh | head -20
```

### Download Model

```bash
wget https://huggingface.co/model/resolve/main/model.safetensors
```

### Extract Dataset

```bash
tar xzf dataset.tar.gz -C ./data/
```

### Count Python Lines

```bash
find . -name "*.py" | xargs wc -l | tail -1
```

### Disk Usage

```bash
df -h
du -sh ./data/*
```

### Environment Variables

```bash
env | grep -i cuda
env | grep -i torch
```

---

# Tool Usage

| Tool | Purpose |
|------|---------|
| tmux | Persistent training sessions |
| tail + grep | Monitor logs |
| nohup | Background jobs |
| htop | CPU monitoring |
| nvtop | GPU monitoring |
| SSH | Remote GPU access |
| rsync | Sync files |
| Pipe & Redirects | Process logs |
| Aliases | Faster workflow |

---

# Post-Lesson Quiz

### 1. What is the biggest advantage of `tmux`?

- Uses less CPU
- ✅ Detach & reattach with live multiple panes
- Restarts failed processes
- Compresses output

**Explanation**

`tmux` keeps terminal sessions alive after disconnecting and allows multiple panes in one window.

---

### 2. What does this command do?

```bash
python train.py > output.log 2>&1
```

- Errors only
- ✅ Redirects both output and errors to `output.log`
- Runs twice
- Uses more memory

**Explanation**

`2>&1` sends **stderr** to the same destination as **stdout**.

---

### 3. How do you access a remote Jupyter Notebook locally?

- `scp`
- ✅ `ssh -L 8888:localhost:8888 user@gpu-box`
- `rsync`
- `ssh --forward-port`

**Explanation**

SSH port forwarding maps the remote notebook to your local browser.

---

# Quiz Score

✅ **3 / 3 Correct**

---

# Key Terms

| Term | Meaning |
|------|---------|
| Shell | Command interpreter (bash, zsh) |
| tmux | Persistent terminal multiplexer |
| Pipe (`|`) | Send output to another command |
| PID | Process ID |
| nohup | Ignore hangup signal |
| SSH | Secure remote shell |

---

# Quick Facts

- Use **`Ctrl+R`** to search command history.
- Use **`tmux`** for long-running AI training.
- Monitor GPUs with **`nvidia-smi`** or **`nvtop`**.
- **`tail -f`** watches logs in real time.
- **`nohup`** keeps jobs alive after terminal closes.
- **`2>&1`** combines stdout and stderr.
- **SSH + rsync** are essential for cloud GPU workflows.
```
