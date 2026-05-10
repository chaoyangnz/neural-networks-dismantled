---
chapter: 2
title: "The Three-Layer Map: What, How, Where"
---

Every neural-network concept lives at three levels simultaneously. Confusion comes from
mixing them. The three-layer map tells you exactly which level you are at.

| Layer | Question Answered | Attention Example |
|---|---|---|
| What (Semantic) | What information is represented or moved? | A token gathers relevant information from other tokens |
| How (Mathematical) | What function or tensor implements it? | softmax(QKᵀ / √d) V |
| Where (Execution) | How does hardware physically compute it? | matmul → scale → mask → softmax → matmul |

## The Three-Sentence Exercise

> [KEY] **When any concept confuses you:** write three sentences — one at each level.
> If you cannot write all three, you have found precisely where your understanding
> breaks down. This is the primary diagnostic tool of the book.

## Example: Convolution

| Level | Description |
|---|---|
| What | A spatial location uses evidence from its local neighbourhood. |
| How | A shared weight kernel computes a weighted sum over a local patch. |
| Where | The runtime slides patches into SIMD-friendly memory access patterns. |

## Example: A Dense Layer

| Level | Description |
|---|---|
| What | A representation is projected into a new coordinate space. |
| How | y = xW + b, matrix multiplication plus bias addition. |
| Where | A BLAS GEMM call on CPU or a tensor core operation on GPU. |

> [MENTAL] Pick one concept you already know — ReLU, dropout, softmax. Write one
> sentence at each level. Which level was hardest to articulate?
