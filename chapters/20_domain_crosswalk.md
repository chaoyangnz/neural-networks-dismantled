---
chapter: 20
title: "Domain Crosswalk: Language, Vision, and Graphs"
---

The EIU framework applies identically across all three major domains. Seeing them
side by side makes the universality visible in one place.

| Field | Language (Decoder) | Vision (CNN) | Vision (ViT) | Graph (GNN) |
|---|---|---|---|---|
| Entity | Token | Spatial location | Image patch | Node |
| Representation | Hidden state | Channel vector | Patch embedding | Node embedding |
| Structure | Sequence + causal mask | 2D grid | Set + position encoding | Explicit edges |
| Interaction | Causal self-attention | Local convolution | Full self-attention | Message passing |
| Update | MLP + residual | Nonlinearity + norm | MLP + residual | Node MLP |
| Readout | Logit projection | Pooling + classifier | CLS token + head | Node or graph head |
| Training | Next-token loss | Classification loss | Classification/contrastive | Task-specific |

## What Each Domain Gets Uniquely Right

### Language

Causal next-token prediction is a natural self-supervised objective that requires the
model to compress everything knowable about context. The causal mask enforces an
information constraint that mirrors how language is produced and consumed.

### Vision with CNNs

Spatial locality is a reliable prior for natural images. Nearby pixels are almost
always more related than distant ones. CNNs exploit this with shared local kernels,
making them highly data-efficient relative to vision transformers.

### Graphs

Explicit edge structure makes GNNs natural when relational structure is known:
molecules (atoms and bonds), knowledge graphs (entities and relations), road networks
(intersections and roads). Aggregation must be permutation-invariant because node
orderings are arbitrary.

> [USED] Language: every text AI. Vision CNNs: photo apps, medical imaging.
> Vision ViT: DALL-E, Stable Diffusion, modern classifiers.
> Graphs: drug discovery, recommendation systems, fraud detection.
