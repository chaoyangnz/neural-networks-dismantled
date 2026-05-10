---
chapter: 13
title: "The Structure Spectrum: From Dense to Explicit"
---

Interaction rules form a continuous spectrum. Seeing them this way makes hybrid and
novel architectures immediately interpretable.

| Structure | Who Communicates | Interaction Style | Example |
|---|---|---|---|
| No structure (set) | Everyone to everyone | Dense / fully learned | Bidirectional attention |
| Sequence (causal) | Each position to earlier positions | Causal masking | Autoregressive LM |
| Local sequence | Position to nearby neighbours | Windowed | 1D CNN, sliding window attention |
| Grid | Location to spatial neighbours | Fixed local kernel | 2D CNN |
| Explicit graph | Node to connected neighbours | Edge-defined | GNN |
| Hierarchical | Fine entities then pooled | Coarsening | U-Net, pooling layers |
| Cross-modal | Two pools attend to each other | Cross-attention | Encoder-decoder |

## Inductive Bias as a Position on the Spectrum

An **inductive bias** is a structural assumption that makes some patterns easier to
learn than others. CNNs have a strong bias toward translation equivariance. Transformers
have weak spatial bias and must learn spatial structure from data. When data is
plentiful, weak inductive bias often wins. When data is scarce, strong inductive bias
often wins.

> [KEY] Apparent novelties are recognisable variants on the spectrum. Sparse attention
> is dense attention with most edge weights zeroed. Graph attention is message passing
> with learned aggregation weights. Each is a trade-off between expressiveness and
> compute cost.
