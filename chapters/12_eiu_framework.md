---
chapter: 12
title: "The Entity-Interaction-Update Framework"
---

This is the hinge of the book. Three questions decode any layer in any architecture.

| Term | Definition | Examples |
|---|---|---|
| Entity | The unit being represented | Token, patch, graph node, pixel region, timestep |
| Representation | The vector or tensor state of that entity | Hidden vector, channel vector, node embedding |
| Structure | Which entities can interact, and how constrained | Sequence, grid, graph, set, memory |
| Interaction | How information moves between entities | Attention, convolution, message passing, recurrence |
| Update | How representation changes after interaction | MLP, activation, normalization, residual addition |
| Readout | How the output is extracted | Classifier head, logit projection, pooling |
| Objective | What training pressure is applied | Cross-entropy, denoising loss, contrastive loss |

> [KEY] **One-sentence architecture test:** If you cannot state what the entities are
> and how they interact, you do not yet understand the architecture. Everything else is
> detail layered on top of this.

## EIU Applied

Using EIU: a **transformer** has entities = tokens, interaction = each token attends
to all others weighted by learned relevance, update = per-token MLP with residual.
A **CNN** has entities = spatial locations, interaction = local convolution with shared
weights, update = nonlinearity and normalization. A **GNN** has entities = nodes,
interaction = message passing from neighbors, update = node MLP.

> [MENTAL] Apply EIU to an LSTM. What is the entity? What is the interaction? What is
> the update? How does your answer change if you consider the gating mechanism specifically?
