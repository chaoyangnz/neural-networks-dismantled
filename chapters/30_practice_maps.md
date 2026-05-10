---
chapter: 30
title: "Practice Maps and Closing Synthesis"
---

## Practice Map: Decoder-Only Language Model (GPT / LLaMA)

| Field | Answer |
|---|---|
| Entities | Tokens |
| Representation | [B, S, F] |
| Structure | Sequence + causal mask |
| Interaction | Causal self-attention |
| Update | Per-token MLP + residuals + layer norm |
| Readout | Linear projection to vocabulary logits |
| Loss | Next-token cross-entropy |
| Composition | Decoder-only |
| Motivation | RNNs could not parallelise; transformers process all positions at once |
| Bottleneck | O(n²) attention; KV cache size at long context |

## Practice Map: CNN Image Classifier

| Field | Answer |
|---|---|
| Entities | Spatial positions |
| Representation | [B, H, W, C] |
| Structure | 2D grid, local neighbourhoods |
| Interaction | Shared local convolution kernel |
| Update | Nonlinearity, normalisation, residual block |
| Readout | Global average pooling + classifier |
| Loss | Cross-entropy |
| Composition | Encoder + task head |
| Motivation | MLPs on images were quadratically expensive; ignored spatial structure |
| Bottleneck | Convolution kernel throughput; memory layout |

## Practice Map: Vision Transformer (ViT)

| Field | Answer |
|---|---|
| Entities | Image patches |
| Representation | [B, num_patches, F] |
| Structure | Set + learned position embeddings |
| Interaction | Full bidirectional self-attention across all patches |
| Update | Per-patch MLP + residuals + layer norm |
| Readout | CLS token + classifier |
| Loss | Classification or contrastive loss |
| Composition | Encoder-only |
| Motivation | Test whether attention alone, given scale, suffices without CNN inductive bias |
| Bottleneck | Attention scales quadratically with number of patches |

## Practice Map: Graph Neural Network

| Field | Answer |
|---|---|
| Entities | Nodes |
| Representation | [num_nodes, F] |
| Structure | Explicit edge topology |
| Interaction | Message passing: each node aggregates from neighbours |
| Update | Node MLP or gated update |
| Readout | Node-level or graph-level pooling head |
| Loss | Task-specific supervised or self-supervised |
| Composition | Encoder + task head |
| Motivation | CNNs and transformers assume fixed spatial or sequential structure |
| Bottleneck | Irregular sparse memory access |

## Practice Map: Encoder-Decoder Language Model (T5 / BART)

| Field | Answer |
|---|---|
| Entities | Source tokens (encoder) + target tokens (decoder) |
| Representation | [B, S, F] for each stack |
| Structure | Encoder: full attention; Decoder: causal + cross-attention to encoder |
| Interaction | Encoder: bidirectional; Decoder: causal + cross-attention |
| Update | MLP + residuals + layer norm in both stacks |
| Readout | Decoder next-token logits |
| Loss | Teacher-forced next-token prediction on target |
| Composition | Encoder-decoder |
| Motivation | Translation needs rich input understanding and sequential output generation |
| Bottleneck | Two full transformer stacks; cross-attention adds cost |

## Final Synthesis

The reader who has completed this book now has four lenses for any architecture:
the **What** of what information is represented, the **How** of what math implements
it, the **Where** of how hardware executes it, and the **Why** of what problem forced
this design to exist.

Most new architectures are modifications of existing choices: a new entity type, a new
interaction structure, a new objective, a new composition pattern, or a new execution
strategy. When you encounter one for the first time, the question is not 'what is this?'
but 'which choices did they change, what problem were they solving, and does the
comparison hold compute constant?'

> Neural networks learn to organise information in latent representations so that useful
> behaviour becomes easy to compute — and every architectural decision is ultimately a
> bet about which organisation of information will make a specific class of useful
> behaviour easiest to learn, given the data, compute, and hardware available.
