---
chapter: 11
title: "Data and Representations: What Training Data Does"
---

Architecture and objective receive most of the attention in deep learning. Data is
often treated as a given. This is a mistake. Data is the primary determinant of what
representations a model can possibly learn.

> [KEY] Architecture defines the structure within which representations are learned.
> Data defines which representations it is possible to learn. Both matter; neither
> substitutes for the other.

## Data Determines the Possible

A model can only learn patterns present and consistent in its training data. If a
concept appears rarely, its representation will be shallow. If a language appears in
1% of the training corpus, the model will be substantially weaker in that language than
in one representing 30% of the corpus. These are data problems, not architecture problems.

## Distribution Shift

A model trained on one data distribution and evaluated on a different one will fail in
proportion to how different those distributions are. A medical classifier trained on one
hospital's equipment may fail on another's. A language model trained on text from 2024
will handle post-2024 events poorly. Distribution shift is the central challenge of
deploying models reliably in the real world.

## Pre-Training Data Composition

For large models, data composition deliberately shapes representational strengths.
More code in training data produces stronger code reasoning. More scientific text
produces better scientific concept representations. These are engineering decisions
with large, measurable effects.

## Quality vs Quantity

For a fixed compute budget, smaller quantities of high-quality, diverse data often
produce better representations than larger quantities of noisy or repetitive data.
Filtering, deduplication, and curation are active engineering disciplines.

> [PRACTICE] When a model behaves unexpectedly, ask two questions before touching the
> architecture: (1) Is this behaviour explained by something in the training
> distribution? (2) Would the model have seen enough examples of this type to learn a
> reliable representation?
