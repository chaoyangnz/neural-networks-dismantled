---
chapter: 29
title: "Glossary, Confusion Pairs, and Terminology Crosswalk"
---

## Core Glossary

**Activation:** A computed internal value during a forward pass.

**Attention:** Weighted aggregation where each entity computes a weighted sum over
others' values, with weights from learned query-key similarity.

**Autograd:** Automatic differentiation: records a computation graph during the forward
pass and applies the chain rule to compute gradients.

**Backpropagation:** The reverse-mode pass propagating gradients from the loss back
through the computation graph.

**Batch:** Independent examples processed together for hardware efficiency. Batch items
do not interact.

**Beam search:** A decoding strategy maintaining k best partial sequences and selecting
the globally highest-probability completion.

**Bottleneck:** A linear down-projection compressing a representation to lower
dimensionality.

**BPE (Byte Pair Encoding):** Tokenisation algorithm iteratively merging the most
frequent adjacent character pairs into new vocabulary tokens.

**Channel:** Feature dimension at a spatial location in a CNN feature map.

**Context window:** The set of tokens visible to a language model during one forward
pass or generation step.

**Cross-attention:** Attention where queries come from one entity pool and keys/values
from another.

**Decoding strategy:** The procedure converting a probability distribution over
vocabulary into the next token.

**Distribution shift:** Test data comes from a different distribution than training
data, causing degraded model performance.

**Embedding:** Initial vector assigned to a raw object before context-specific
processing.

**Emergent capability:** A capability appearing above a scale threshold, absent in
smaller models.

**Entity:** The unit represented: token, patch, node, spatial location, or timestep.

**Fine-tuning:** Continued training of a pre-trained model on a smaller task-specific
dataset.

**Foundation model:** A model large enough that pre-trained representations are broadly
useful across many tasks.

**Gradient:** Local sensitivity of the loss with respect to a parameter.

**Hallucination:** Generating fluent but factually wrong content.

**Hidden state:** A context-dependent internal representation produced after one or
more layers.

**In-context learning:** Performing new tasks from examples in the context window
without weight updates.

**Inductive bias:** A structural assumption that makes some patterns easier to learn
than others.

**KV cache:** Cached key and value tensors from prior generation steps, avoiding
recomputation.

**Latent space:** Internal coordinate system in which representations live.

**Layer normalisation:** Rescales each entity's vector to zero mean and unit variance;
primarily a training stability mechanism.

**Logit:** Unnormalized score before softmax conversion to probability.

**Loss:** Scalar objective defining training pressure.

**MLP:** Multilayer perceptron: dense linear layers alternating with nonlinear
activations.

**Position encoding:** A position-specific vector added to each entity's embedding so
the model can distinguish token order.

**Pre-training:** Large-scale training on broad data using a self-supervised objective.

**RAG:** Retrieval-Augmented Generation: combines a parametric language model with a
non-parametric external index.

**Representation learning:** Learning to map inputs into geometric spaces where the task
becomes computationally easy.

**Residual connection:** Additive skip: x + update(x) instead of replacing x.

**Scaling law:** Empirical relationship: model loss decreases predictably with model
size, data, and compute.

**Temperature:** A decoding parameter dividing logits before softmax. Lower T sharpens;
higher T flattens.

**Token:** A textual unit produced by a tokenizer: word, subword, or special symbol.

**Top-k sampling:** Sample the next token from the k highest-probability vocabulary items.

**Top-p sampling:** Sample from the smallest set of tokens whose cumulative probability
exceeds p.

**Transformer:** Architecture based on attention-based entity interaction, per-entity
MLP updates, and residual connections.

## Confusion Pairs

**Embedding vs representation vs hidden state:** An *embedding* is the initial vector
for a raw object. A *representation* is any internal vector at any stage. A *hidden
state* is context-dependent after layer processing. All embeddings are representations;
not all representations are embeddings.

**Parameter vs activation:** *Parameters* are stored in the model and persist across
all inputs — they are what training adjusts. *Activations* are computed during a
forward pass and differ for every input.

**Layer vs block vs module:** A *layer* is a single learned transformation. A *block*
is a group of layers forming one repeating unit. A *module* is a software container;
any layer or block is a module.

**Temperature vs top-p vs top-k:** *Temperature* reshapes the entire probability
distribution. *Top-k* restricts sampling to k candidates. *Top-p* restricts to the
smallest set summing to p. All three are often combined.

**Pre-training vs fine-tuning vs inference:** *Pre-training* is large-scale training
from scratch. *Fine-tuning* is continued training from a pre-trained checkpoint.
*Inference* is running the model forward to produce outputs, with no parameter updates.

## Cross-Domain Vocabulary Map

| General | Language | Vision (CNN) | Vision (ViT) | Graph |
|---|---|---|---|---|
| Entity | Token | Spatial location | Patch | Node |
| Representation | Hidden state | Channel vector | Patch embedding | Node embedding |
| Interaction | Self-attention | Convolution | Self-attention | Message passing |
| Structure | Sequence | 2D grid | Set + position | Explicit edges |
| Readout | Logit head | Pooling + classifier | CLS + head | Node/graph head |
