---
chapter: 15
title: "Composition Patterns: Encoders, Decoders, and Bottlenecks"
---

We separate **patterns** (the shape of the model) from **mechanisms** (the logic inside
each block). The same attention mechanism appears in all three patterns; what differs
is information flow direction.

| Pattern | Semantic Role | Mechanism | Examples |
|---|---|---|---|
| Encoder | Understanding and representing input | Bidirectional attention — every entity sees every other | BERT, RoBERTa, DINOv2 |
| Decoder | Generating output token by token | Causal (masked) attention — each entity sees only prior entities | GPT, LLaMA, Mistral |
| Bottleneck | Filtering and compressing a representation | Linear down-projection, optionally followed by up-projection | Adapter layers, cross-modal projections |

## The Three Assembled Configurations

- **Encoder-only:** Full bidirectional attention. Rich input representations. Used for
  understanding and classification, not generation.
- **Decoder-only:** Causal attention throughout. Generates one token at a time. Used
  for all forms of language generation and in-context learning.
- **Encoder-decoder:** Encoder builds bidirectional input representation; decoder
  generates output while cross-attending to encoder states. Used when input and output
  are both structured sequences.

> [KEY] Diagnostic: does the task require reading the full input before producing any
> output, or producing output token-by-token conditioned on a structured input?
> Encoder-only for understanding. Decoder-only for generation.
> Encoder-decoder for structured input-to-output.
