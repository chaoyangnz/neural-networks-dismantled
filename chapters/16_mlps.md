---
chapter: 16
title: "MLPs: Universal Approximators"
---

```
x  →  Linear  →  Nonlinearity  →  Linear  →  …  →  output
```

The MLP applies dense transformations to a fixed-size feature vector. There is no
sub-structure: every input dimension can influence every output dimension, but there is
no structured communication between parts of the input.

## When MLPs Are the Right Tool

- Tabular data with no inherent spatial, sequential, or relational structure.
- The final task head after an encoder: classification, regression, value prediction.
- The per-entity update sublayer inside transformers, CNNs, and GNNs.

> [USED] Tabular ML for click prediction, fraud detection, and churn modelling often
> uses MLPs as the core model, sometimes combined with embeddings for categorical features.

> [TRACE Micro-Walkthrough: MLP Forward Pass] Input: feature vector x = [0.2, -0.8, 0.4]  shape [F=3]
> Layer 1: y1 = ReLU(xW1 + b1)  shape [H=8]
> Layer 2: y2 = ReLU(y1·W2 + b2)  shape [H=8]
> Output: logits = y2·W3 + b3  shape [C=2]
> Note: no entity interacts with any other entity. Each input is processed independently.
