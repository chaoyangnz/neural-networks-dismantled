---
chapter: 8
title: "Training: Loss, Gradients, and Optimization"
---

## Loss

The loss function is the signal that judges outputs and creates training pressure.
The model is not told to learn concepts — it is told to reduce a number. Useful
internal structure emerges because it helps reduce that number.

> [KEY] Loss defines the pressure. Architecture defines the structure within which the
> model responds. Data defines what patterns are available to learn. All three
> determine the representations that emerge.

| Task | Typical Loss | Representational Pressure |
|---|---|---|
| Language modeling | Next-token cross-entropy | Compress context into representations that predict the next word |
| Classification | Cross-entropy | Separate class clusters in latent space |
| Regression | Mean squared error | Produce scalar outputs near targets |
| Contrastive | Similarity loss | Pull related pairs together; push unrelated apart |
| Diffusion | Denoising loss | Learn to reverse a corruption process |

## Gradients and Optimization

A **gradient** tells how a small change in a parameter would change the loss.
The **Adam optimizer**, the standard choice, maintains adaptive per-parameter estimates
of gradient magnitude, making training robust across many different problem scales and
architectures.

## Generalization

The goal is not to memorize training examples but to learn transformations that work on
unseen examples from the same distribution. Generalization depends on data diversity,
architecture inductive bias, objective design, scale, and regularization.
