# GPU & CUDA Verification with PyTorch

## Verify NVIDIA GPU

```bash
nvidia-smi
```

**Shows**
- GPU Name
- Driver Version
- CUDA Version
- GPU Utilization
- Temperature
- VRAM Usage
- Running Processes

---

## Verify CUDA in PyTorch

```python
import torch

print("=" * 60)
print("            PyTorch CUDA Verification")
print("=" * 60)

print(f"PyTorch Version : {torch.__version__}")
print(f"CUDA Available  : {torch.cuda.is_available()}")
print(f"CUDA Version    : {torch.version.cuda}")

if torch.cuda.is_available():
    print(f"GPU Device      : {torch.cuda.get_device_name(0)}")
    print(f"GPU Count       : {torch.cuda.device_count()}")

    print("\nGPU Memory")
    print("-" * 60)
    print(f"Allocated       : {torch.cuda.memory_allocated(0)/1024**2:.2f} MB")
    print(f"Reserved        : {torch.cuda.memory_reserved(0)/1024**2:.2f} MB")

print("=" * 60)
print("Verification Complete")
print("=" * 60)
```

---

## CPU vs GPU Benchmark

```python
import torch
import time

size = 4096

cpu_a = torch.randn(size, size)
cpu_b = torch.randn(size, size)

start = time.time()
cpu_c = cpu_a @ cpu_b
cpu_time = time.time() - start

if torch.cuda.is_available():
    gpu_a = cpu_a.cuda()
    gpu_b = cpu_b.cuda()

    start = time.time()
    gpu_c = gpu_a @ gpu_b

    # Wait until GPU finishes computation
    torch.cuda.synchronize()

    gpu_time = time.time() - start

    print(f"CPU Time : {cpu_time:.4f} sec")
    print(f"GPU Time : {gpu_time:.4f} sec")
    print(f"Speedup  : {cpu_time / gpu_time:.2f}x")
```

---

# Post-Lesson Quiz

### 1. What command verifies that your NVIDIA GPU is detected and shows its current status?


**Explanation**

`nvidia-smi` (NVIDIA System Management Interface) displays GPU utilization, memory usage, temperature, driver information, CUDA version, and running processes.

---

### 2. Why must you call `torch.cuda.synchronize()` before measuring GPU execution time?


**Explanation**

GPU operations execute **asynchronously**. Python continues immediately while the GPU is still computing. `torch.cuda.synchronize()` waits until all GPU work is complete, producing accurate timing.

---

### 3. Approximately how many parameters fit in **24 GB VRAM** using **fp16**?

**Explanation**

fp16 uses **2 bytes per parameter**.

```
24 GB ÷ 2 bytes ≈ 12 Billion parameters
```

Actual capacity is lower because activations, gradients, optimizer states, and other tensors also consume VRAM.


# Key Terms

| Term | Meaning |
|------|---------|
| **CUDA** | NVIDIA's parallel computing platform for GPU programming |
| **VRAM** | GPU memory that limits model size |
| **fp16** | 16-bit floating point (half precision) using half the memory of fp32 |
| **Tensor Cores** | Specialized GPU hardware for extremely fast matrix multiplication |

---

# Quick Facts

- Verify GPU anytime with **`nvidia-smi`**
- Use **`torch.cuda.is_available()`** to detect CUDA in PyTorch.
- Always call **`torch.cuda.synchronize()`** before benchmarking GPU code.
- **24 GB VRAM ≈ 12B parameters (fp16)** *(rough estimate)*.
- GPU operations are asynchronous by default.