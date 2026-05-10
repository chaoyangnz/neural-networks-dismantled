---
chapter: 24
title: "Sampling and Decoding: From Logits to Text"
---

The model produces a probability distribution over its vocabulary at each generation
step. How you convert that distribution into the next token is the **decoding strategy**.
Different strategies produce very different behaviours.

## The Starting Point: Logits

After the final transformer layer, a linear projection maps the hidden state to one
score (logit) per vocabulary item. Softmax converts logits to probabilities. Every
vocabulary item has a non-zero probability. The question is: which token do we select?

| Strategy | How It Works | Characteristic Behaviour |
|---|---|---|
| Greedy | Always select the highest-probability token | Deterministic; often repetitive or bland |
| Temperature | Divide all logits by T before softmax. T<1 sharpens; T>1 flattens | T=0 ≈ greedy; T>1 = more random and creative |
| Top-k | Sample from the k highest-probability tokens only | Prevents very unlikely tokens; k=1 is greedy |
| Top-p (nucleus) | Sample from the smallest set whose probabilities sum to p | Adapts to distribution shape; p=0.9 is common |
| Beam search | Maintain k best partial sequences; select the overall best | Better for globally coherent output; expensive |

> [TRACE Micro-Walkthrough: Token Selection with Temperature]
> Logits: {cat: 3.2, dog: 2.8, bird: 1.1, fish: 0.4}
> After softmax (T=1.0): {cat: 0.42, dog: 0.35, bird: 0.14, fish: 0.09}
> After softmax (T=0.5): {cat: 0.61, dog: 0.34, bird: 0.04, fish: 0.01}  [sharper]
> After softmax (T=2.0): {cat: 0.31, dog: 0.28, bird: 0.23, fish: 0.18}  [flatter]
> Top-p=0.9 at T=1.0: sample from {cat, dog, bird} (cumulative = 0.91)
> Greedy: always select "cat"

## Hallucination and Decoding

Hallucination — generating fluent but factually wrong content — is partly a training
problem (the model learned to be fluent more than factual) and partly a decoding problem
(high-temperature sampling may surface confident-sounding completions that were
statistically common in training even if factually unsupported).

> [FAILURE] Repetition loops are a common greedy decoding failure mode: once the model
> generates a phrase with high probability, the phrase conditions on itself, making
> repetition even more probable. Repetition penalties are a common engineering fix.

> [MENTAL] If you wanted a model to generate a creative short story, what temperature
> and top-p values would you choose? What if you wanted it to extract specific facts
> from a document? Why might the same values not work well for both?
