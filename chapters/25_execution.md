---
chapter: 25
title: "Execution: From Semantics to Kernels"
---

The execution layer turns model semantics into physical computation: tensors become
buffers, operations become kernels, graphs become schedules.

| Term | Definition |
|---|---|
| Buffer | A contiguous typed memory block on a device |
| Kernel | A compiled routine executing one operation on hardware |
| Dispatch | The act of launching a kernel |
| Device | CPU, GPU (CUDA/ROCm), Apple Silicon (Metal), or TPU |
| Stride | Memory jumps per step along each tensor axis |
| Fusion | Combining multiple ops into one kernel to reduce memory traffic |
| Fallback | Using a slower generic path when an optimised kernel is unavailable |

## End-to-End Trace: What Happens When You Call matmul

> [TRACE Execution Trace: out = torch.matmul(A, B)]
> 1. Python dispatcher receives the call
> 2. Operator resolution: identifies matmul and its registered implementations
> 3. Device check: A and B are on CUDA; routes to CUDA backend
> 4. Shape and dtype validation: [M, K] × [K, N] → output [M, N]
> 5. Memory allocation: output buffer of shape [M, N] on device
> 6. Kernel selection: cuBLAS GEMM selected based on shapes and dtype
> 7. Kernel launch: CUDA kernel executes on GPU streaming multiprocessors
> 8. Result in output buffer; Python object wraps buffer with shape/stride metadata
> 9. If autograd enabled: backward node registered recording how to compute dA and dB

## Why Memory Dominates

Many NN operations are memory-bandwidth-limited, not compute-limited. Moving data
between high-bandwidth memory (HBM) and compute units is the bottleneck. Fusing
operations into one kernel reduces how many times the same large tensor is read from
and written to HBM. FlashAttention is the canonical example: it tiles attention to fit
in fast on-chip SRAM, dramatically reducing HBM traffic without changing total arithmetic.
