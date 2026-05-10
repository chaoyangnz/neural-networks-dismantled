---
chapter: 4
title: "Tokenization: How Raw Text Becomes Entities"
---

Tokens are the entities of language models. Every subsequent chapter that discusses
language assumes you understand what a token is and why tokenization is non-trivial.
This chapter fills that gap.

## The Problem: Computers Operate on Numbers

A language model cannot process the string "cat" directly. It needs an integer it can
use to look up a vector in a learned table. Tokenization is the procedure that converts
raw text into a sequence of such integers. The design of this procedure has significant
downstream effects on what the model can and cannot do.

## Three Approaches, Increasing Sophistication

| Approach | Unit | Vocabulary Size | Problem |
|---|---|---|---|
| Character-level | Each character | ~100 | Very long sequences; no morphological sharing |
| Word-level | Each word | 50,000–500,000 | Unknown words; vocabulary explosion across languages |
| Subword (BPE) | Frequent character groups | 30,000–64,000 | Balances sequence length against coverage |

## Byte Pair Encoding (BPE)

BPE is the most widely used subword method. It starts with individual characters and
iteratively merges the most frequent adjacent pair into a new token. After enough
merges, common words like 'the' become single tokens, while rare words like
'unbelievableness' are split into subword pieces: [un][believ][able][ness]. The
vocabulary — the set of all valid tokens — is fixed at training time.

## Why This Matters: Surprising Consequences

- **LLMs count letters badly.** Ask a model how many r's are in 'strawberry.' It may
  fail because 'strawberry' might be a single token, making character-level
  introspection unreliable.
- **Numbers are fragile.** "9.11" and "9.9" may tokenize to different numbers of
  tokens, making numeric comparison awkward for a model that learned from token
  sequences rather than numeric values.
- **Multilingual models are unequal.** The same sentence in English might be 10 tokens
  while an equivalent in another language is 40, costing 4x the context window and compute.
- **Vocabulary size is a hyperparameter.** Larger vocabularies reduce sequence length
  but increase embedding table size.

> [TRACE Tensor Trace: Text to Token IDs] Input string: "The cat sat"
> Tokenizer splits: ['The', ' cat', ' sat']
> Vocabulary lookup: [464, 3797, 3031]
> Shape entering the model: [S=3] — one integer per token
> After batch dimension: [B=1, S=3]
> This integer sequence is the input to the embedding layer.

> [FAILURE] Because vocabulary is fixed at training time, any token outside the
> vocabulary must be split into subword fallbacks or handled with an unknown token.
> This is why models can behave erratically on novel technical terms, non-standard
> spellings, or newly coined proper nouns.

> [MENTAL] If a model's vocabulary contains 'ing' as a token, and you ask it to
> process 'running,' what are the possible tokenizations? Why might different
> tokenizations of the same word cause problems for the model?
