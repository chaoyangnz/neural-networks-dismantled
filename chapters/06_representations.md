---
chapter: 6
title: "Representations, Embeddings, and Latent Spaces"
---

## Representation Learning: The Unifying Idea

All architectures in this book are doing the same thing at the deepest level:
**representation learning**. They learn to map inputs into geometric spaces where the
task becomes computationally easy. This is why pre-trained representations transfer
to new tasks, why scale helps, and why architecture choice matters — different
structures induce different geometric biases.

## Embedding vs Representation vs Hidden State

| Term | Definition | Example |
|---|---|---|
| Embedding | Initial vector for a raw object, before context processing | Token id 464 → 768-dim vector |
| Representation | Any internal vector at any processing stage | Layer 12 hidden state |
| Activation | A computed value during the forward pass | Output of a GELU function |
| Latent space | The coordinate system in which representations live | Semantic geometry of hidden states |

## Geometric Proximity and Semantic Similarity

In a well-trained latent space, geometric proximity **often correlates with** semantic
similarity. Representations of related concepts tend to cluster; unrelated concepts
tend to be distant. This geometry is not programmed — it emerges from training
pressure. However, embedding spaces are anisotropic and metric-sensitive: the
relationship between distance and similarity is useful and approximate, not universal.

> [USED] Every semantic search engine, content recommendation system, and document
> retrieval pipeline uses embeddings. Your query becomes a vector; items nearby in
> that space are returned. The geometry of the latent space is the product.

## Context Changes Representations

The token 'bank' in 'the bank approved the loan' and in 'the river overflowed the bank'
begins with the same embedding. After attention layers, its hidden state diverges: one
representation has moved toward financial concepts; the other toward geographic
concepts. The embedding represents identity; the hidden state represents meaning in
context.
