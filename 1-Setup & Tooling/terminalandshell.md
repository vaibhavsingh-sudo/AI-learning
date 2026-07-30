Terminal & Shell
The terminal is where AI engineers live. Get comfortable here.
Type: Learn

Languages: --

Prerequisites: Phase 0, Lesson 01

Time: ~35 minutes

🎯 Learning Objectives
Use piping, redirects, and grep to filter and process training logs from the command line
Create persistent tmux sessions with multiple panes for concurrent training and GPU monitoring
Monitor system and GPU resources with htop, nvtop, and nvidia-smi
Transfer files between local and remote machines using SSH, scp, and rsync
The Problem
You will spend more time in the terminal than in any editor. Training runs, GPU monitoring, log tailing, remote SSH sessions, environment management. Every AI workflow touches the shell. If you're slow here, you're slow everywhere.

This lesson covers the terminal skills that matter for AI work. No history of Unix. No deep-dive into Bash scripting. Just what you need.

✅ Pre-Lesson Check
1. What does the pipe operator '|' do in a shell command?
✗
Runs two commands in parallel
✓
Sends the standard output of one command as standard input to the next
Saves the output of a command to a file
Combines two files into one
The pipe operator connects commands in a pipeline. For example, 'cat log.txt | grep error' sends the contents of log.txt as input to grep, which filters for lines containing 'error'.
2. What happens to a running process when you close the terminal that started it?
The process continues running in the background
✓
The process receives a hangup signal (SIGHUP) and typically terminates
The process pauses until you open a new terminal
The process automatically migrates to a system service
Closing the terminal sends SIGHUP to child processes, which causes them to terminate by default. Tools like tmux, nohup, or screen prevent this.
1/2 correct
The Concept
Expand
tmux session: training

Top row

Pane 1: Training run
python train.py
Epoch 12/100 ...

Pane 2: GPU monitor
watch -n1 nvidia-smi
GPU: 78% | Mem: 14/24G

Pane 3: Logs + experiments
tail -f logs/train.log | grep loss

Three things running at once. One terminal. You can detach, go home, SSH back in, and reattach. The training keeps running.

Build It
Step 1: Know your shell
Check which shell you're running:

bashCopy
echo $SHELL
Most systems use bash or zsh. Both work fine. The commands in this course work in either.

Key things to know:

bashCopy
# Move around
cd ~/projects/ai-engineering-from-scratch
pwd
ls -la

# History search (most useful shortcut you'll learn)
# Ctrl+R then type part of a previous command
# Press Ctrl+R again to cycle through matches

# Clear terminal
clear   # or Ctrl+L

# Cancel a running command
# Ctrl+C

# Suspend a running command (resume with fg)
# Ctrl+Z
Step 2: Piping and redirects
Piping connects commands together. This is how you process logs, filter output, and chain tools. You will use this constantly.

bashCopy
# Count how many times "loss" appears in a log
cat train.log | grep "loss" | wc -l

# Extract just the loss values from training output
grep "loss:" train.log | awk '{print $NF}' > losses.txt

# Watch a log file update in real time, filtering for errors
tail -f train.log | grep --line-buffered "ERROR"

# Sort experiments by final accuracy
grep "final_accuracy" results/*.log | sort -t= -k2 -n -r

# Redirect stdout and stderr to separate files
python train.py > output.log 2> errors.log

# Redirect both to the same file
python train.py > train_full.log 2>&1
The three redirects you need:

Symbol	What it does
>	Write stdout to file (overwrite)
>>	Append stdout to file
2>	Write stderr to file
2>&1	Send stderr to same place as stdout
|	Send stdout of one command as stdin to the next
Step 3: Background processes
Training runs take hours. You don't want to keep your terminal open the whole time.

bashCopy
# Run in background (output still goes to terminal)
python train.py &

# Run in background, immune to hangup (closing terminal won't kill it)
nohup python train.py > train.log 2>&1 &

# Check what's running in background
jobs
ps aux | grep train.py

# Bring a background job to foreground
fg %1

# Kill a background process
kill %1
# or find its PID and kill that
kill $(pgrep -f "train.py")
The difference between &, nohup, and screen/tmux:

Method	Survives terminal close?	Can reattach?
command &	No	No
nohup command &	Yes	No (check log file)
screen / tmux	Yes	Yes
For anything longer than a few minutes, use tmux.

Step 4: tmux
tmux lets you create persistent terminal sessions with multiple panes. This is the single most useful tool for managing training runs.

bashCopy
# Install
# macOS
brew install tmux
# Ubuntu
sudo apt install tmux

# Start a named session
tmux new -s training

# Split horizontally
# Ctrl+B then "

# Split vertically
# Ctrl+B then %

# Navigate between panes
# Ctrl+B then arrow keys

# Detach (session keeps running)
# Ctrl+B then d

# Reattach
tmux attach -t training

# List sessions
tmux ls

# Kill a session
tmux kill-session -t training
A typical AI workflow session:

bashCopy
tmux new -s train

# Pane 1: start training
python train.py --epochs 100 --lr 1e-4

# Ctrl+B, " to split, then run GPU monitor
watch -n1 nvidia-smi

# Ctrl+B, % to split vertically, tail the logs
tail -f logs/experiment.log

# Now detach with Ctrl+B, d
# SSH out, go get coffee, come back
# tmux attach -t train
Step 5: Monitoring with htop and nvtop
bashCopy
# System processes (better than top)
htop

# GPU processes (if you have NVIDIA GPU)
# Install: sudo apt install nvtop (Ubuntu) or brew install nvtop (macOS)
nvtop

# Quick GPU check without nvtop
nvidia-smi

# Watch GPU usage update every second
watch -n1 nvidia-smi

# See which processes are using the GPU
nvidia-smi --query-compute-apps=pid,name,used_memory --format=csv
htop keybindings you'll use:

F6 or > to sort by column (sort by memory to find memory leaks)
F5 to toggle tree view (see child processes)
F9 to kill a process
/ to search for a process name
Step 6: SSH for remote GPU boxes
When you rent a cloud GPU (Lambda, RunPod, Vast.ai), you connect via SSH.

bashCopy
# Basic connection
ssh user@gpu-box-ip

# With a specific key
ssh -i ~/.ssh/my_gpu_key user@gpu-box-ip

# Copy files to remote
scp model.pt user@gpu-box-ip:~/models/

# Copy files from remote
scp user@gpu-box-ip:~/results/metrics.json ./

# Sync a whole directory (faster for many files)
rsync -avz ./data/ user@gpu-box-ip:~/data/

# Port forward (access remote Jupyter/TensorBoard locally)
ssh -L 8888:localhost:8888 user@gpu-box-ip
# Now open localhost:8888 in your browser

# SSH config for convenience
# Add to ~/.ssh/config:
# Host gpu
#     HostName 192.168.1.100
#     User ubuntu
#     IdentityFile ~/.ssh/gpu_key
#
# Then just:
# ssh gpu
Step 7: Useful aliases for AI work
Add these to your ~/.bashrc or ~/.zshrc:

bashCopy
source phases/00-setup-and-tooling/10-terminal-and-shell/code/shell_aliases.sh
Or copy the ones you want. The key aliases:

bashCopy
# GPU status at a glance
alias gpu='nvidia-smi --query-gpu=index,name,utilization.gpu,memory.used,memory.total,temperature.gpu --format=csv,noheader'

# Kill all Python training processes
alias killtraining='pkill -f "python.*train"'

# Quick virtual environment activate
alias ae='source .venv/bin/activate'

# Watch training loss
alias watchloss='tail -f logs/*.log | grep --line-buffered "loss"'
See code/shell_aliases.sh for the full set.

Step 8: Common AI terminal patterns
These come up repeatedly in practice:

bashCopy
# Run training, log everything, notify when done
python train.py 2>&1 | tee train.log; echo "DONE" | mail -s "Training complete" you@email.com

# Compare two experiment logs side by side
diff <(grep "accuracy" exp1.log) <(grep "accuracy" exp2.log)

# Find the largest model files (clean up disk space)
find . -name "*.pt" -o -name "*.safetensors" | xargs du -h | sort -rh | head -20

# Download a model from Hugging Face
wget https://huggingface.co/model/resolve/main/model.safetensors

# Untar a dataset
tar xzf dataset.tar.gz -C ./data/

# Count lines in all Python files (see how big your project is)
find . -name "*.py" | xargs wc -l | tail -1

# Check disk space (training data fills disks fast)
df -h
du -sh ./data/*

# Environment variable check before training
env | grep -i cuda
env | grep -i torch
Use It
Here's when each tool comes into play during this course:

Tool	When you use it
tmux	Every training run (Phases 3+)
tail -f + grep	Monitoring training logs
nohup / &	Quick background tasks
htop / nvtop	Debugging slow training, OOM errors
SSH + rsync	Working on cloud GPUs
Piping + redirects	Processing experiment results
Aliases	Saving time on repetitive commands
Exercises
Install tmux, create a session with three panes, and run htop in one, watch -n1 date in another, and a Python script in the third. Detach and reattach.
Add the aliases from code/shell_aliases.sh to your shell config and reload with source ~/.zshrc (or ~/.bashrc).
Create a fake training log with for i in $(seq 1 100); do echo "epoch $i loss: $(echo "scale=4; 1/$i" | bc)"; sleep 0.1; done > fake_train.log and then use grep, tail, and awk to extract just the loss values.
Set up an SSH config entry for a server you have access to (or use localhost to practice the syntax).
✅ Post-Lesson Quiz
1. What is the key advantage of tmux over using 'nohup command &' for long-running training jobs?
tmux uses less CPU than nohup
tmux lets you detach, reattach, and see live output with multiple panes
tmux automatically restarts failed processes
tmux compresses the process output to save disk space
2. What does 'python train.py > output.log 2>&1' accomplish?
Runs train.py and saves only errors to output.log
Runs train.py and redirects both standard output and standard error to output.log
Runs train.py twice and logs the second run
Runs train.py with double the memory allocation
3. Which command lets you access a remote Jupyter notebook running on port 8888 of a GPU box from your local browser?
scp -P 8888 user@gpu-box:~/notebook.ipynb
ssh -L 8888:localhost:8888 user@gpu-box
rsync -avz user@gpu-box:8888 localhost:8888
ssh user@gpu-box --forward-port 8888
Key Terms
Term	What people say	What it actually means
Shell	"The terminal"	The program that interprets your commands (bash, zsh, fish)
tmux	"Terminal multiplexer"	A program that lets you run multiple terminal sessions inside one window, and detach/reattach
Pipe	"The bar thing"	The | operator that sends one command's output as input to another
PID	"Process ID"	A unique number assigned to every running process, used to monitor or kill it
nohup	"No hangup"	Runs a command immune to the hangup signal, so closing the terminal won't kill it
SSH	"Connecting to the server"	Secure Shell, an encrypted protocol for running commands on a remote machine