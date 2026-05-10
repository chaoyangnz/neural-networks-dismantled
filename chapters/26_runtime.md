---
chapter: 26
title: "Runtime Architecture: Eager, Graph, IR, Backend"
---

## Eager Mode

Operations execute immediately as called. Values exist after every line. Standard Python
debugging works. PyTorch popularised this for research ergonomics.

## Graph Mode

Computation is captured before execution. The runtime can then optimise, fuse,
schedule, and lower the full graph. This is compiler-like and enables optimisations
invisible to eager execution — cross-operation fusion, memory planning, device scheduling.

## IR and Backend Lowering

An **IR (intermediate representation)** is the runtime's internal canonical form:
a description of operations, shapes, dtypes, and dependencies that is simpler than the
user API and backend-independent. **Lowering** converts IR into backend-specific plans:
BLAS for CPU, cuBLAS and custom kernels for CUDA, Metal shaders for Apple Silicon.

> [KEY] High-level semantics should be normalised before backend execution. Backends
> should not need to understand every frontend convenience.
