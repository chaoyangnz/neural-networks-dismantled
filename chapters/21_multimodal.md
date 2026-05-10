---
chapter: 21
title: "Multimodal Systems"
---

> [KEY] A multimodal system has multiple entity types sharing a representation space,
> connected by cross-attention or projection layers. Once text tokens and image patches
> live in the same vector space, the architecture behaves like any other transformer.

## Three Fusion Patterns

| Pattern | How Modalities Connect | Trade-off |
|---|---|---|
| Early fusion | All modalities projected to shared space before any layers | Deep cross-modal interaction; more compute |
| Late fusion | Each modality encoded separately; combined before task head | Cheaper; less cross-modal interaction |
| Cross-attention | One modality queries; the other provides keys and values | Asymmetric; common in encoder-decoder systems |

> [TRACE Micro-Walkthrough: Vision-Language Forward Pass]
> Image: 224×224 pixels, split into 14×14=196 patches
> Patch projection: each 16×16×3 patch → 768-dim vector  shape [196, 768]
> Text: "What is in this image?" → 8 tokens → shape [8, 768]
> Concatenate along sequence axis: shape [204, 768]
> Transformer processes all 204 entities; text tokens can attend to patch tokens
> Readout: last text token hidden state → answer generation

> [USED] GPT-4o, Claude with images, Gemini, LLaVA, CLIP, DALL-E. When you upload a
> photo and ask an AI to describe it, patch embeddings and text token embeddings are
> being combined through one of these three fusion patterns.
