---
chapter: 17
title: "CNNs: Local Message Passing on Grids"
---

A CNN is local message passing over a regular grid: 1D for audio or time series,
2D for images, 3D for video or volumetric data.

## EIU View

- **Entity:** Spatial positions. Each carries a vector of channels.
- **Structure:** A regular grid; positions interact only with their local neighbourhood.
- **Interaction:** A shared weight kernel slides across all positions. The same detector
  applies everywhere — translation equivariance.
- **Update:** Nonlinearity applied to the convolution output.

| Term | Definition |
|---|---|
| Kernel | Small shared weight pattern applied at each position |
| Stride | Step size when sliding the kernel |
| Channel | Feature dimension at each spatial location |
| Feature map | Grid of channel vectors at one layer |
| Receptive field | Input region that can influence one output value |

> [TRACE Micro-Walkthrough: One Conv Layer] Input feature map: shape [H=8, W=8, C_in=3]
> Kernel: shape [3, 3, C_in=3, C_out=16]
> For each of 8×8=64 positions: dot product of local 3×3×3 patch with kernel weights
> Output feature map: shape [H=8, W=8, C_out=16]
> After 4 such layers: 11×11 receptive field. After 8 layers: 23×23.
> Hierarchy emerges from composition of local operations.

> [USED] Face unlock, object detection in self-driving cars, photo enhancement, medical
> imaging, satellite analysis. CNNs remain dominant wherever spatial locality is a
> reliable prior.

> [FAILURE] CNNs trained on natural images can fail dramatically on images with unusual
> textures or backgrounds not present in training. The translation equivariance prior
> helps within-distribution but can become a brittle assumption out-of-distribution.
