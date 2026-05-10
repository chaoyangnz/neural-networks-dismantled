---
chapter: 10
title: "Training vs Inference: Two Operating Regimes"
---

The same model behaves very differently during training and inference. Conflating them
is one of the most persistent sources of beginner confusion.

| Property | Training | Inference |
|---|---|---|
| Input visibility | Full sequence, processed in parallel | One token at a time (autoregressive) or full input (encoder) |
| Computation | Forward + backward pass | Forward pass only |
| Gradients | Tracked | Not computed |
| Memory | Activations + gradients + optimizer state | Activations only |
| Parallelism | High — all positions at once | Limited for generation |
| KV cache | Not used | Used — caches prior keys and values |
| Batch size | Large | Variable, often 1 |

## The KV Cache

Each transformer layer computes keys and values from its input. During generation,
prior tokens' keys and values are stable — they will not change. The **KV cache**
stores them so the model computes only the query for the new token and attends over
the cache. Without it, each generation step costs O(n) in the number of prior tokens,
because everything would be recomputed from scratch.

> [USED] When a language model generates a response and you see tokens stream out at
> roughly constant speed, that's the KV cache at work. The first token takes slightly
> longer (full forward pass); subsequent tokens are faster (one cached step each).

> [FAILURE] At long context lengths, the KV cache itself becomes the memory bottleneck.
> For a model with 32 layers, 32 heads, and a 128k token context, the KV cache can
> exceed the memory cost of the model weights themselves. This is why long-context
> inference is an active engineering problem.
