---
chapter: 28
title: "How to Read Any New Architecture"
---

When you encounter a new paper or model, apply this checklist before reading the
abstract claims.

- How is raw input decomposed into entities?
- What vector or tensor represents each entity, and what is its shape?
- What structure is assumed: sequence, grid, graph, set, or mixed?
- How do entities exchange information? What is the interaction rule?
- What local transformation updates each entity's representation after interaction?
- How many interaction-update cycles are repeated?
- What output head reads the final representations?
- What loss function is used, and what representational pressure does it apply?
- What is the computational bottleneck: memory, matmul, or irregular access?
- **What problem was the previous generation failing at?**
- **Is this encoder-only, decoder-only, or encoder-decoder?**
- **Is the improvement architectural, or is it explained by scale or data?**
- **Does the paper compare against a compute-matched baseline?**

## Architecture Summary Card

| Field | Fill This In |
|---|---|
| Entities | |
| Representation shape | |
| Structure | |
| Interaction | |
| Update | |
| Readout | |
| Loss | |
| Composition | Encoder-only / Decoder-only / Encoder-decoder |
| Motivation | Previous models failed at… |
| Bottleneck | |
| Compute-matched baseline? | Yes / No / Unclear |
