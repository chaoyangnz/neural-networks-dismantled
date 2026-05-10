---
chapter: 19
title: "Transformers: Dynamic Message Passing"
---

The transformer is the most general canonical architecture. It is not tied to sequences,
grids, or graphs — it operates on any entity set and constructs the interaction graph
dynamically at each layer, based on entity content.

## The Transformer Block

```
For each layer:
  X_attn = Attention(X)             # entities exchange information
  X      = LayerNorm(X + X_attn)   # residual + normalize
  X_ff   = FFN(X)                  # each entity updates locally
  X      = LayerNorm(X + X_ff)     # residual + normalize
```

## Queries, Keys, and Values

| Term | Role | Computation |
|---|---|---|
| Query | What this entity is looking for | Projects entity into a 'question' space |
| Key | What this entity offers for matching | Projects entity into an 'answer' space |
| Value | What information this entity sends if selected | Projects entity into a 'content' space |

> [TRACE Micro-Walkthrough: Attention Disambiguates Context]
> Sentence A: "The bank approved the loan"
> Sentence B: "The river overflowed the bank"
>
> Both sentences: token "bank" starts with identical embedding e_bank.
>
> Sentence A, after attention layer 1:
>   "bank" query matches strongly with keys of "approved", "loan"
>   Attention weights: bank→approved=0.35, bank→loan=0.40, others<0.10
>   Hidden state h_bank_A shifts toward {financial, institutional}
>
> Sentence B, after attention layer 1:
>   "bank" query matches strongly with keys of "river", "overflowed"
>   Attention weights: bank→river=0.42, bank→overflowed=0.31, others<0.10
>   Hidden state h_bank_B shifts toward {geographic, terrain}
>
> Same input token. Same initial embedding. Diverging hidden states after one layer.

## Position Encoding: Why It Is Necessary

Attention is permutation-equivariant without positional information: shuffling the token
order changes which tokens are at each position, but no token's representation changes
based on its position alone. **Position encodings** — position-specific vectors added
to embeddings before processing — give the model access to order information.

## The Quadratic Bottleneck and Responses to It

Dense attention computes N² pairwise scores for N tokens. At N=512: manageable.
At N=32,768: expensive. At N=1,000,000: impractical.

- **Sparse attention** (Longformer, BigBird): each token attends to a local window plus
  a few global tokens — O(n) cost.
- **Linear attention**: approximates the full matrix with a kernel factorisation — O(n).
- **State space models** (Mamba, S4): replace attention with a linear recurrence that
  scales linearly and parallelises differently.
- **FlashAttention**: does not reduce asymptotic complexity but computes standard
  attention faster via IO-aware tiling — now standard in production systems.

> [TRACE Tensor Trace: Full Transformer Forward Pass]
> Input: "The cat sat"  (S=3 tokens)
> Token ids: [464, 3797, 3031]  shape [B=1, S=3]
> After embedding lookup: shape [B=1, S=3, F=768]
> After position encoding: shape [B=1, S=3, F=768]
> Q, K, V projections (H=12 heads, d_head=64): each [B=1, H=12, S=3, d=64]
> Attention scores QKᵀ: shape [B=1, H=12, S=3, S=3]
> After softmax: shape [B=1, H=12, S=3, S=3]
> After value aggregation: shape [B=1, H=12, S=3, d=64]
> After concat + projection: shape [B=1, S=3, F=768]
> After FFN: shape [B=1, S=3, F=768]
> After L=12 layers: shape [B=1, S=3, F=768]
> After logit projection: shape [B=1, S=3, V=50257]
> Next-token distribution (last position): shape [V=50257]

> [USED] Every large language model you have interacted with — ChatGPT, Claude,
> Gemini, Copilot — is built on transformer blocks. The architecture is also used for
> image generation, protein structure prediction, and audio synthesis.

> [FAILURE] Transformers hallucinate because next-token prediction rewards fluent,
> plausible text, not factually grounded text. A model can assign high probability to a
> confident-sounding false continuation if it fits the distributional pattern of the
> context, even if no training example supports the specific claim.

> [MENTAL] If you removed all attention layers from a transformer and kept only the FFN
> layers, what capability would disappear? What would remain? Could the model still be trained?
