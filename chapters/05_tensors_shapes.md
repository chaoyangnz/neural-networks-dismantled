---
chapter: 5
title: "Tensors and Shapes: The Semantic Organizer"
---

A tensor is commonly taught as a multidimensional array. That is a *Where*-level
definition. At the *What* level, a tensor is a **Semantic Organizer**: its axes encode
information categories, not just dimensions.

| Level | Description |
|---|---|
| What | Axes represent semantic categories: entities, features, time, examples. |
| How | A multilinear map over a product of vector spaces. |
| Where | A contiguous typed memory block with a stride array for hardware traversal. |

## The Anatomy of Shape: [B, S, F]

A tensor of shape [32, 512, 768] carries three semantic clauses:

- **Batch (32):** 32 independent examples processed together for hardware efficiency.
  They never interact. This dimension exists for the GPU, not the model logic.
- **Sequence (512):** 512 ordered entities per example. Temporal or positional
  structure lives here.
- **Features (768):** Each entity is described by 768 numbers — the width of the
  model's representational workspace per entity.

> [KEY] Batch is for the GPU. Sequence, grid, and graph axes belong to the model.
> When reasoning about what a model does to one example, mentally remove the batch axis.

## Strides and Views

Every tensor has shape, dtype, device, and stride. **Stride** specifies the memory
jump per step along each axis. A **view** reinterprets memory without copying.
Operations like transpose and reshape are often free metadata changes, but some kernels
require contiguous memory and force a copy.

> [MENTAL] A tensor of shape [B, S, F] is transposed to [B, F, S]. Which semantic
> axis now runs fastest in memory? When would this matter for performance?
