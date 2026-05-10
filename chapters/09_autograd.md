---
chapter: 9
title: "Autograd and the Backward Graph"
---

Autograd is automatic differentiation. It tracks every operation in the forward pass
and automatically applies the chain rule to compute gradients for every parameter.

## A Scalar Worked Example

Consider the simplest possible model: one parameter w, one input x, one target y_true.

```python
x = 2.0,   w = 3.0,   y_true = 4.0

# Forward pass
prediction = x * w           # = 6.0
loss       = (prediction - y_true)**2  # = (6-4)^2 = 4.0

# Backward pass (chain rule)
d_loss/d_prediction = 2 * (prediction - y_true)  # = 2*(6-4) = 4.0
d_loss/dw           = d_loss/d_prediction * d_prediction/dw
                    = 4.0 * x
                    = 4.0 * 2.0 = 8.0

# Parameter update (learning rate = 0.1)
w_new = w - 0.1 * 8.0   # = 3.0 - 0.8 = 2.2

# New prediction (better)
prediction_new = x * w_new = 2.0 * 2.2 = 4.4   # closer to 4.0
```

Every gradient in a real neural network — across billions of parameters — is computed
by this same chain rule, applied automatically by the autograd system.

## Forward and Backward Graphs

```
Forward:   x, W, b  →  xW  →  xW+b  →  prediction  →  loss
Backward:  loss.grad=1  →  d(prediction)  →  dW, db, dx
```

The backward graph runs in reverse. Each operation records how to propagate gradients
through itself — this is stored during the forward pass so it is available when
backpropagation runs.

> [PRACTICE] Autograd has significant memory cost. During training, intermediate
> activations must be saved for backward. Training typically uses 2–4× the memory of
> inference on the same batch. When a training run exceeds GPU memory, reducing batch
> size or using gradient checkpointing are the standard responses.

> [MENTAL] In the scalar example above, if x were 4.0 instead of 2.0 (everything else
> the same), what would the gradient dw be? Would the parameter update be larger or
> smaller? What does this tell you about how input scale affects training?
