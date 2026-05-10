---
chapter: 23
title: "The Pre-Training Paradigm"
---

The dominant modern workflow is not training a model from scratch for each task. It is
pre-training a large model on broad data, then adapting it.

## The Three-Stage Workflow

- **Pre-training:** Train on a massive broad dataset using self-supervised objectives.
  The model learns general representations. This is the expensive stage.
- **Supervised fine-tuning (SFT):** Continue training on curated instruction-response
  pairs. The model learns to follow instructions in the format users expect.
- **Alignment (RLHF):** Human raters compare model outputs; a reward model is trained
  on those preferences; the language model is then optimised against the reward model
  using reinforcement learning.

## Why Representations Transfer

Features useful for predicting the next word — grammar, facts, discourse structure,
reasoning patterns, world knowledge — are also useful for downstream tasks. Pre-training
implicitly learns broadly transferable representations. Fine-tuning teaches the model
how to deploy those representations for a specific purpose.

> [KEY] Pre-trained representations are not task-specific. They are general descriptions
> of the input in high-dimensional space. Fine-tuning teaches the model how to use those
> descriptions for a specific purpose.

| Approach | Weight Updates? | Data Required | Cost | When to Use |
|---|---|---|---|---|
| Training from scratch | All weights | Very large dataset | Very high | Genuinely novel domain with no relevant pre-trained model |
| Fine-tuning | All or some weights | Moderate task-specific dataset | Medium | Task differs substantially from the base model's training distribution |
| Prompting / ICL | None | A few examples in context | Very low | Task is close to the model's pre-training distribution |

## In-Context Learning

Decoder-only models can learn from examples in their context window without weight
updates. Provide three examples of a task in the prompt; the model generalises to new
instances. This is qualitatively different from training: no parameters change.

> [USED] Every interaction with ChatGPT, Claude, or Gemini involves a model that was
> pre-trained on broad text, fine-tuned on instruction examples, and aligned with human
> preferences. The capability you experience is the product of all three stages.
