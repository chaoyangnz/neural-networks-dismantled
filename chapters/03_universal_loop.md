---
chapter: 3
title: "The Universal Neural-Network Loop"
---

Every architecture follows the same repeating cycle. Understanding the loop means every
specific architecture you encounter is a specialisation of something already known.

```
raw input
  → encode into initial representations
  → repeated blocks of: interact + update
  → task-specific readout
  → loss or output
```

## The Generic Formula

```
H_0 = Encode(input)
for l in 0..L-1:
    M_l   = Interact(H_l, structure)
    H_l+1 = Update(H_l, M_l)
Output = Readout(H_L)
```

This is a template. Transformers, CNNs, RNNs, and GNNs all fit it if you choose the
right definitions of Encode, Interact, Update, and Readout.

## The Five Primitive Questions

- What are the entities?
- What vector or tensor represents each entity?
- What structure constrains interaction: sequence, grid, graph, set, or none?
- How do entities exchange information?
- How is the final output extracted and how is the system trained?

> [KEY] We do not calculate an answer directly. We evolve a signal through stages of
> refinement until it is in the right form for the task. Architecture choice is
> primarily a choice about how to structure that refinement.
