---
chapter: 18
title: "RNNs: Sequential Message Passing"
---

```
h_t  =  update(h_{t-1},  x_t)
y_t  =  readout(h_t)
```

An RNN processes sequences by maintaining a hidden state carried forward through time.
The entity is a timestep; the interaction is recurrent state update; the structure is
a strictly ordered chain.

## LSTM and GRU: Gated State Machines

Vanilla RNNs overwrite state at every step, making long-range dependency difficult.
LSTM and GRU add learned gates — sigmoid functions that decide what fraction to keep,
forget, or expose. They significantly extend the range of dependencies the model can capture.

> [TRACE Micro-Walkthrough: RNN Hidden State Evolution] Input tokens: ["The", "bank", "by", "the", "river"]
> h_0 = zeros
> h_1 = update(h_0, embed("The"))    — state begins accumulating context
> h_2 = update(h_1, embed("bank"))   — "bank" integrated; context still ambiguous
> h_3 = update(h_2, embed("by"))     — preposition signals spatial framing
> h_4 = update(h_3, embed("the"))    — article continues spatial context
> h_5 = update(h_4, embed("river"))  — "river" disambiguates; state encodes geographic bank
> Problem: to reach h_5, "bank" meaning must survive 3 overwrite operations.

## Why Transformers Largely Replaced RNNs

RNNs have an inherent sequential dependency: step t requires step t−1. This prevents
parallelising training across timesteps, which is the dominant training cost.
Transformers process all positions simultaneously, at the cost of O(n²) attention.

> [FAILURE] RNNs forget. Information from early tokens must survive many overwrite steps
> to influence the final state. LSTM gates help substantially but do not eliminate the
> fundamental bottleneck for very long sequences.
