
# Advanced Neural Network Architectures – Lecture Notes


These notes give a high‑level yet practical tour of modern neural‑network architectures, highlighting *why* each design choice matters. Where possible, intuitive explanations are backed by key papers and pithy code / math snippets so that an engineer coming from classic ML can get up to speed quickly.

---

## 1 Optimization, Inductive Bias & the IID Assumption

### 1.1 Why Optimizers Matter in Non‑Convex Landscapes
Gradient‑based optimizers don’t merely *find* minima – they *shape* what is reachable. Choice of learning‑rate schedule, momentum, adaptive steps, etc. nudges solutions toward particular basins (inductive bias).  
Mathematically, for weight $W_{ij}$:  

\[
\frac{\partial \mathcal{L}}{\partial W_{ij}}
\;=\;
\lim_{\epsilon\to0}\;
\frac{\mathcal{L}(W_{ij}) - \mathcal{L}(W_{ij}+\epsilon)}{\epsilon}
\]

*Take‑away:* in non‑convex settings the optimizer *qualitatively* alters solutions – not just their speed of convergence.

### 1.2 Data‑Centric AI & Inductive Bias from the Dataset  
Andrew Ng’s **data‑centric AI** mantra flips the usual *model‑centric* loop: first curate & balance data, then adjust the model only as needed. Clean labels and balanced distributions embed domain bias directly into the training signal, often trumping clever architectures.

### 1.3 Continual Learning & Task Interference  
Parallel tasks that share parameters can interfere, effectively turning “parallel” learning into **sequential** learning (cf. Saxe et al. 2013). Catastrophic interference explains wasted compute on tasks that never truly co‑train.

---

## 2 Language Modelling: From Feed‑Forward N‑grams to RNNs

### 2.1 N‑th‑Order Markov Assumption  
Classic feed‑forward language models assume a fixed context window – an N‑gram on steroids. This hard cut‑off limits long‑range dependencies and pushes researchers toward recurrent or attention mechanisms.

### 2.2 Recurrent Neural Networks  
**Pros**: naturally compact, $\mathcal{O}(1)$ inference, explicit recurrence.  
**Cons**: exploding / vanishing gradients, sequential training bottleneck, expressivity limits.

> *Practical tip:* always start with gradient‑clipping and gated cells (GRU / LSTM) before blaming your data.

---

## 3 Attention & Transformers

### 3.1 Scaled Dot‑Product Attention  
\[
\text{Attention}(Q,K,V)=
\operatorname{softmax}\bigl(
\tfrac{QK^{\mathsf{T}}}{\sqrt{d_k}}
\bigr)V
\]

### 3.2 Transformer Block Anatomy  
1. **Temporal Mixing** – multi‑head attention + residual + normalization  
2. **Feature Mixing** – position‑wise MLP (often GeLU / SwiGLU / Gated Linear Unit)  
3. Final linear + softmax for token prediction.

> **At scale, the MLP dominates FLOPs** (Wei et al. 2024) – an often overlooked fact.

### 3.3 Positional Encoding  
* Sinusoidal (absolute)  
* Learned vectors  
* **Rotary Positional Embeddings (RoPE)** – rotate queries & keys in complex space; preserves relative offsets and extends sequence length seamlessly.

---

## 4 Scaling & Efficiency

* **Megatron‑LM** shows how tensor + pipeline sharding lets a single model grow to billions of parameters without blowing GPU memory.  
* **LoRA** freezes base weights and trains tiny low‑rank adapters – slash trainable parameters by 10,000× while matching full fine‑tuning performance.  
* **gMLP / gated MLPs** prove that with clever gating, pure MLPs can rival attention on many tasks.

---

## 5 Limitations: Over‑Squashing, Over‑Smoothing & Softmax Collapse

Even Transformers struggle when long‑range signals must pass through a fixed‑width channel (over‑squashing). Temperature in softmax further drives representation collapse; tuning it can trade compression vs. generalization.

---

## 6 Beyond Standard Transformers

**RWKV** and other *time‑mix / channel‑mix* hybrids marry RNN‑like inference with Transformer‑like training parallelism, aiming for linear‑time decoding without key‑value caches.

---

## 7 Recommended Papers & Further Reading

* Saxe *et al.* 2013 — *Exact solutions to the nonlinear dynamics of learning in deep linear neural networks*  
* Pascanu *et al.* 2013 — *On the difficulty of training RNNs*  
* Vaswani *et al.* 2017 — *Attention Is All You Need*  
* Su *et al.* 2021 — *RoFormer / RoPE*  
* Shoeybi *et al.* 2019 — *Megatron‑LM*  
* Hu *et al.* 2021 — *LoRA*  
* Liu *et al.* 2021 — *Pay Attention to MLPs / gMLP*  
* Wei *et al.* 2024 — *Building on Efficient Foundations*  
* Barbero *et al.* 2024 — *Transformers need glasses!*  
* Masarczyk *et al.* 2025 — *Unpacking Softmax*  
* RWKV paper (Peng *et al.* 2023)  

---

## 8 Cheat‑Sheet

| Topic | One‑Liner |
|-------|-----------|
| **Optimizer choice** | Acts as inductive bias in non‑convex loss landscapes |
| **Data‑centric AI** | Clean data >> exotic architecture tweaks |
| **RNN bottlenecks** | Sequential back‑prop, gradient issues |
| **Transformer magic** | Attention = dynamic, content‑addressable routeing |
| **MLP cost** | At >1 B params, FFN FLOPs > attention FLOPs |
| **LoRA** | Fine‑tune 0.1 % of weights with rank‑$r$ adapters |
| **Positional info** | RoPE = complex‑valued rotation, enables extrapolation |
| **Over‑squashing** | Long dependencies crushed into fixed width |
| **RWKV** | Attention‑free, linear‑time RNN‑Transformer hybrid |

---

*End of notes – happy hacking!*  


Optimizer qualitatively alter solutions

Choose one optimizer or another (Non convex scenario)

Reachable h - there is an inductive bias to everything you do
data centric view is becoming more mainstream
inductive biases may be introduced either from data or from optimizer

Continual learning - some

The IID asumption in gradient descent

dL/ dWij = lim e -> 0 (L(Wij) - L(Wij + e))/e

interferance in learning tasks, if they work together to create an environment, one task takes parameters one way, the other takes parameters another way

Because of the interferance, what generally happens is that tasks started in parallel, they often become sequential Andrew Saxe et al 2013
There is a lot of waste in computing because of tasks that you are not actually learning (due to interferance)

This is why we should do architectures

Autoregressive Language Modelling

- Sometimes n-th order markov assumption made which has an impact on architecture design

p (x1, x2, ...xT) = prod from t=1 to T p(x1|x,...x -1)

Issues with feedforward neural networks for language modelling

Assumes the nr order Markov assumption seemed as a necessity for NNs:

Pascanu et al 2014

RNNs

Positives / Negatives

Positives

natural and compact choice
fast inference O(1)
Observable expressivity

Negatives

training stability
training scalability
expressivity bottlenecks
 compression
 optimization


Attention based decoding


Attention (K,Q,V) = softmax (QK^T) / 

Transformer block

Attention works because it is wrapped in a transformer block

A key reason for transformer success

Feature mixing

RMSNorm -> Feed Forward -> Dropout


Temporal Mixing

RMSNorm -> Attention Layer -> Dropout 


(Temporal Mixing -> Feature Mixing) -> Linear -> Softmax

Feature mixing is an MLP

Gated MLP


MLPs bring the expressivity


Megatron sharding governs block design

Attention sharding Megatron LM  Training Multi Billion parameter Language Model using model parallelism

At scale - it is actually the MLP block that dominates compute (Building on Efficient Foundations, Wei et all 2024)

Finetune @ scale: LoRA

Augment a linear projection by a low rank term, reduces the memory used in training LoRA paper.

Semantic attention? 

How do transfoerms track sequential order 

Answer: Positional Encoding

Rotary positional embeddings (RoPE)

RoPE does not always decay with distance

Semantic attention with RoPE cannot be robust

The lowest frequencies in RoPE spin so slowly that they are able to carry semantics

Transformers need glasses! Information over squashing in language tasks, Barbero et all

Over - Squashing / Over - Smoothing ~ Vanishing Signals

Transformers are a form of Graph Neural Networks

Learnability issues (not expressivity)

Unpacking Softmax: How temperature drives representational collapse, compression and generalization, Masarczyk et al

Thomas Griffiths - The profile of human intelligence is due to its limitations

AlphaGo unnatural moves are potentially due to lack of decomposition of the problem into tracktable subproblems (humans explicitly sacrifice performance for efficiency)

ML systems have limitations (including computational)
