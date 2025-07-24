
<!-- Compiled LLM Training & Dialogue Notes -->

## TL;DR

Large‑language‑model training follows a three‑stage pipeline: **cross‑entropy pre‑training**, **supervised fine‑tuning (SFT)** and **reinforcement‑learning alignment**.  Alignment treats the LLM as a **policy πθ : context → next‑token** and optimises it with **policy‑gradient methods such as PPO**, guided by a **reward model** that encodes human (or self‑) preferences.  For task‑oriented dialogue, corpora like **MultiWOZ / EmoWOZ** with toolkits such as **ConvLab‑2/3** plus continual‑learning policies (e.g. **DDPT + CLEAR**) keep agents useful across domains.  ‘Agentic’ workflows further curb hallucinations via retrieval‑augmented verification, while **intrinsic‑dimension metrics** predict grokking events during training.  

---

## 1 · From Next‑Token Prediction to Aligned Policies

### 1.1 Pre‑training  
LLMs first minimise token‑level cross‑entropy \(L_{\text{CE}}\) on trillions of tokens, producing a density model \(p_θ(y_t\,|\,x_{<t})\).  This provides general world knowledge but no steering mechanism. citeturn0news80  

### 1.2 Supervised Fine‑Tuning (SFT)  
A curated dataset \(\mathcal D_{\text{SFT}}=(x,y)\) of instruction pairs further conditions the model toward helpful responses, as shown by **InstructGPT**. citeturn0news80  

### 1.3 Reinforcement‑Learning Alignment  

* **RL fundamentals** — Agents generate trajectories \((s_t,a_t,r_t)\) and maximise the discounted return \(G_t=\sum_k \gamma^k r_{t+k}\).  The policy‑gradient theorem gives  
  \[
    \nabla_θ J(θ)=\mathbb E_{s,a\sim π_θ}[\nabla_θ \log π_θ(a|s)\,A^{π}(s,a)].
  \] citeturn0search8  

* **PPO (Proximal Policy Optimization)** adds a clipped objective to keep updates within a trust‑region, delivering stable large‑batch training for LLMs. citeturn0search0turn0search8  

* **LLM as policy** — Treat the prompt \(x\) as state and the generated token \(y_t\) as action; PPO fine‑tunes the network while constraining KL from the SFT baseline. A 2023 RLHF survey formalises this perspective. citeturn1search0  

### 1.4 Reward Modelling & Preference Optimisation  

| Method | Data format | Optimiser | Comment |
|--------|-------------|-----------|---------|
| **RLHF (PPO)** | \(x,y^{+},y^{-}\) | PPO w/ KL‑penalty | Classic pipeline |
| **DPO** | same | closed‑form logistic loss | No RL loop |  

Direct Preference Optimisation learns a reward model and derives the optimal policy analytically, eliminating sampling overhead. citeturn0search1turn0search9  

### 1.5 Reinforcement Learning from Self‑Feedback (RLSF)  
RLSF lets the model score its own intermediate ‘chain‑of‑thought’ and uses that log‑probability as a reward, removing the need for human annotation yet boosting reasoning accuracy. citeturn1search3  

---

## 2 · Task‑Oriented Dialogue & Continual Learning

### 2.1 Ontologies  
TOD systems define **domains, slots, values**, a running **dialogue state**, and **system actions**; each dialogue is labelled success/failure.

### 2.2 Datasets  

| Corpus | Size / Domains | Highlights |
|--------|----------------|------------|
| **MultiWOZ 2.x** | ≈10 k dialogues, 7 domains | De‑facto TOD benchmark citeturn0search2 |
| **EmoWOZ** | 11 k dialogues, 83 k emotion tags | Adds valence & elicitor labels citeturn0search3 |

### 2.3 Toolkits  
**ConvLab‑2/3** wrap data loaders, user simulators, and PPO trainers under a unified JSON schema for rapid experimentation. citeturn0search4  

### 2.4 Continual RL Policies  

* **DDPT** encodes domain/slot/action descriptions in NL, achieving zero‑shot transfer without parameter growth. citeturn0search6  
* **CLEAR** (Continual Learning with Experience And Replay) mixes on‑policy updates with replayed trajectories and behavioural cloning to curb catastrophic forgetting. citeturn2search1  

### 2.5 Entropy Regularisation & Emotion‑Aware Dialogue  
Maximum‑entropy RL encourages exploration, while DDPT can condition on EmoWOZ tags to adjust language style in real time. citeturn0search3  

---

## 3 · Agentic Workflows & Hallucination Mitigation  
RAG pipelines combine retrieval, generation, verification and (optionally) a human‑feedback loop to prune factual errors. Chain‑of‑Verification reduces hallucinations by prompting the same LLM to question and check its own answers. citeturn3search1turn3search5  Financial Times reports that labs now embed such agentic evaluators in production chatbots. citeturn3news10  

---

## 4 · Theory: Grokking, Intrinsic Dimension & TDA  
A drop in **local intrinsic dimension (LID)** of hidden states often precedes ‘grokking’ — the sudden generalisation phase — letting practitioners stop training early or adjust learning rates. citeturn0search7  

---

## 5 · Putting It All Together

1. **Pre‑train** on web‑scale corpora.  
2. **SFT** on curated instructions.  
3. **Align** via PPO‑based RLHF, DPO or RLSF.  
4. **Deploy TOD** agents with DDPT + CLEAR on MultiWOZ/EmoWOZ using ConvLab‑3.  
5. **Add agentic guards** (RAG + verification) to limit hallucinations. citeturn3search0  
6. **Monitor geometry** (LID) to anticipate grokking or collapse. citeturn0search7  

---
