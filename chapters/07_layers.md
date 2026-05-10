---
chapter: 7
title: "Layers as Learned Transformations"
---

A layer is a learned transformation: it takes a representation and returns a new one.
A deep network composes these: x_0 → x_1 → … → x_L.

## Depth, Width, and Nonlinearity

- **Depth** is the number of transformation steps. Early layers detect simple patterns;
  later layers compose them into complex ones.
- **Width** is the representation dimensionality at each step. Wider networks have more
  representational capacity per entity, at greater memory and compute cost.
- **Nonlinearity** is essential. Without it, all layers collapse to a single linear map
  regardless of depth. Nonlinear activations allow conditional features: patterns
  present only when specific input conditions are met.

## Residual Connections

A residual connection computes **x + update(x)** rather than replacing x. This turns
each layer from a replacement into a refinement. Crucially, gradients can flow directly
through the additive skip, bypassing any problematic layer transformations. This is
what enables 50-, 100-, or 1000-layer networks to train.

## Normalization

Layer normalization rescales each entity's vector to approximately zero mean and unit
variance. Without it, representations in deep networks tend to explode or vanish across
layers, making gradient-based learning unstable. Normalization is primarily an
optimization and stability mechanism rather than a semantic objective. Its purpose is
not to inject new information, though rescaling can influence representational geometry
and learning dynamics.

> [FAILURE] A network without normalization in a deep architecture will often either
> diverge (exploding gradients) or stall (vanishing gradients) within the first few
> thousand training steps. This is not a data problem or a learning-rate problem — it
> is a signal that the representational scale is unconstrained.
