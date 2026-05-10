---
chapter: 14
title: "The Motivation Layer: Why Architectures Exist"
---

Every major architecture was invented to solve a specific failure mode of its
predecessor. Knowing the problem is as important as knowing the solution.

| Architecture | Problem It Solved | Design Response |
|---|---|---|
| MLP | No function approximator for fixed-size inputs | Stack linear layers with nonlinearities |
| CNN | MLPs on images were quadratically expensive; ignored spatial structure | Shared local kernels exploiting translation equivalence |
| RNN | Variable-length sequences; MLPs need fixed-size inputs | Carry hidden state forward through time |
| LSTM / GRU | Vanilla RNNs could not preserve long-range information | Learned gates control what to keep, forget, or expose |
| Transformer | RNNs sequential; could not parallelise; still struggled long-range | Replace recurrence with direct pairwise attention over all positions |
| ViT | Test whether attention alone suffices for vision given scale | Treat image patches as tokens; apply a standard transformer |
| Diffusion | GANs unstable to train; VAEs blurry | Learn to reverse corruption; generate via iterative denoising |
| MoE | Scaling a single dense model expensive per token | Route each token to a sparse subset of expert modules |

> [PRACTICE] When reading a new paper, find the sentence that says 'previous methods
> suffer from X.' That sentence is the motivation. The rest is an engineering response.
> If you understand X, you can evaluate whether the response actually solves it.
