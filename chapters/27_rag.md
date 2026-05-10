---
chapter: 27
title: "Retrieval-Augmented Generation: A Systems Pattern"
---

RAG is a systems pattern, not an architecture. It combines a parametric model
(knowledge in weights) with a non-parametric memory (knowledge in an external index).

## How RAG Works

- A user query is embedded into a vector.
- The vector searches a pre-built index of document embeddings (approximate
  nearest-neighbour search).
- The top-k retrieved documents are inserted into the model's context.
- The model generates a response conditioned on both the query and retrieved context.

| Property | Parametric Only | RAG System |
|---|---|---|
| Knowledge update | Requires retraining | Update the index |
| Attribution | Difficult — distributed across weights | Possible — retrieved sources are explicit |
| Context | Fixed at training time | Dynamic — any indexed document retrievable |
| Per-query cost | Lower | Higher — embedding search + longer context |

> [USED] Perplexity AI, Bing Chat, and enterprise knowledge assistants all use RAG.
> When an AI response includes citations or references to specific documents, retrieval
> is almost certainly involved.

> [FAILURE] RAG fails when retrieval fails: if the relevant document is not in the
> index, or the query embedding is not close to the document embedding, the model
> receives no grounding and may hallucinate anyway.
