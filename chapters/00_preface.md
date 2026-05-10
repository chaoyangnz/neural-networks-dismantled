---
chapter: 0
title: "Preface: Scope, Assumptions, and What This Book Is Not"
---

This book is an orientation layer. It builds the bridge between a machine-learning
textbook, a linear algebra course, and a GPU programming manual — without trying to
replace any of them.

It covers supervised and self-supervised deep learning: how architectures are designed,
why they are designed that way, and how they execute on hardware. It does not cover
reinforcement learning in depth, generative adversarial networks, probabilistic graphical
models, classical machine learning, or the pre-deep-learning era. Each deserves its
own book.

The assumed reader knows what a function is and has seen a matrix. No calculus or
coding experience is required, though both help you go further afterward.

## What This Edition Adds

- **Micro-walkthroughs** in every major architecture chapter: concrete symbol traces
  showing representations evolving step by step.
- **Tensor Trace boxes**: shape evolution through a full forward pass.
- **Tokenization** as a dedicated chapter: the gap between raw text and model input.
- **Sampling and decoding**: how logits become generated text.
- **Failure Mode callouts**: what breaks, and why, in each architecture.
- **Test Your Mental Model prompts**: reflection questions after dense sections.
- Precision fixes throughout: normalization, distance-similarity, attention-head claims.
