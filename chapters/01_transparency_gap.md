---
chapter: 1
title: "The Transparency Gap"
---

## A Concrete Starting Point

You open an app and type: *Explain black holes in simple terms.* In the next few
seconds, something specific happens. Your text is split into fragments called
**tokens**. Each token is converted to an integer. That integer indexes into a learned
table, retrieving a vector of several thousand decimal values — its **embedding**.
Those vectors flow through dozens of identical processing stages. In each stage,
every token consults every other token and updates its own representation. After the
final stage, one transformation produces a probability distribution across the model's
entire vocabulary. The highest-probability token is chosen, appended, and the process
repeats until the response is complete.

Almost every phrase in that description — tokens, embeddings, attention,
representations, vocabulary distribution — you will understand precisely by the last
page. The gap between that description and your current understanding is the
**Transparency Gap**: the distance between code we write, ideas we intend, and
physical computation that executes.

## Why the Gap Exists

Neural-network terminology grew historically, not systematically. The same object —
a vector representation of a data unit — is called a hidden state in an RNN, a feature
map in a CNN, a node embedding in a GNN, and an activation in a runtime trace. These
are not different things. They are different names for the same idea, coined by
different communities for different problems, and never reconciled.

> [KEY] Our goal is **disentanglement**: separating the **What** (information being
> represented), the **How** (math implementing it), and the **Where** (hardware
> executing it). When these three are tangled, the field feels like a fog.
> Separated, its underlying simplicity emerges.

## Four Misconceptions to Clear Now

> [MYTH] **Neurons are like brain neurons.** They are not. The analogy is historical,
> useful in 1943, not functionally accurate today. A neural network neuron is a
> weighted sum followed by a nonlinear function. Releasing the brain metaphor makes
> the math dramatically clearer.

> [MYTH] **The model "understands" things.** The model's internal mechanisms are
> statistical and representational rather than human-cognitive. It has learned
> regularities in a high-dimensional space that produce useful outputs. This is
> remarkable. It is not the same as understanding, and conflating them causes
> confusion when models fail in unexpected ways.

> [MYTH] **Training is programming.** Programming tells a system exactly what to do.
> Training applies pressure through a loss function; useful structure emerges from
> that pressure. The resulting behaviour is encoded in billions of numeric parameters,
> not in readable logic.

> [MYTH] **Attention means the model pays attention like a human.** Attention in
> neural networks is weighted aggregation: each entity computes a weighted sum over
> others' values, where weights are learned to be useful. The word is a suggestive
> metaphor, not a cognitive description.

## The Disentanglement Discipline

For any concept, answer three questions, each in one sentence:
**What** information is being represented or moved?
**How** does a mathematical function or tensor implement it?
**Where** does hardware physically execute the computation?
The next chapter makes each question precise.
