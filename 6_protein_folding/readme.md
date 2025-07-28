
# AlphaFold 3 — A Walkthrough


## 0) Why this matters (Eroom’s Law vs. smarter computation)

**Eroom’s Law**: drug discovery gets *slower* and *more expensive* over time (the opposite of Moore’s Law). The basic pipeline:

Biology → Chemistry → Execution  
Target Discovery → Target Validation → Hit ID & Hit-to-Lead → Lead Optimization → Pre-clinical → Clinical

**Where we bleed time and money (bottlenecks):**
1. **Understanding disease biology.** We often don’t know the right target or mechanism.
2. **Molecule design.** Searching the astronomical space of small molecules and biologics.
3. **Asserting compound quality.** ~90% of candidates fail somewhere en route to approval.
4. **Non-generalization across targets.** Success on one protein rarely transfers.

**TL;DR:** If we can **predict structures and interactions** cheaply and accurately, we compress the search. Computation becomes the microscope and the wind tunnel.

---

## 1) From AlphaFold 2 → Multimer → AlphaFold 3

- **AlphaFold 2 (AF2, 2021):** Input a **single protein sequence**. Use MSA + templates processed by **Evoformer** → predict 3D coordinates and confidence (e.g., pLDDT, pTM). Won CASP14.
- **AlphaFold-Multimer (2022):** Extend to **multiple protein chains** (complexes).
- **AlphaFold 3 (2024):** One model that handles **proteins, nucleic acids (DNA/RNA), ligands, ions, modified residues**. Key shift: **Evoformer → Pairformer (simplified trunk)** and **Structure module → Diffusion module** (a generative model for **continuous 3D coordinates**).

**TL;DR:** AF3 turns structure prediction into **conditional 3D generation** with a diffusion model, using a big “trunk” network (Pairformer) to digest sequences, MSAs, and templates into conditioning.

---

## 2) The pipeline (high level)

**Featurization → Trunk (Pairformer) → Diffusion module → Confidence head**

- **Featurization** (what we feed in):
  - **Sequences** (protein, DNA, RNA).
  - **Ligand molecules** (tokenized **per-atom**; small ions too).
  - **MSAs** (co-evolutionary signals).
  - **Templates** (structurally similar known entries from PDB).
  - Optional: constraints, binding-site hints, known contacts.

- **Trunk: Pairformer (≈ 48 blocks, conceptually)**  
  Think a **graph neural transformer** that keeps two representations:
    - **Single** (token-level): residues for biopolymers; **atoms** for ligands/ions.
    - **Pair** (edge-level): relations between tokens (distances, relative geometry).
  It does **triangle updates** (geometric consistency across triplets) and **attention with pair bias** (edges influence message passing).

- **Diffusion module:** predicts coordinates by **denoising** noisy atoms step-by-step.
- **Confidence head:** scores how much to trust the output (e.g., variants of pLDDT/pTM and ligand/site confidences). Also enables **inference-time scaling**: sample multiple times, pick the best by confidence.

**TL;DR:** A big context engine (Pairformer) + a generative geometry head (Diffusion) = joint, conditional 3D structure for proteins, nucleic acids, and small molecules.

---

## 3) Tokens and graphs: what’s the data layout?

- **Protein/DNA/RNA:** token = **residue** (amino acid or nucleotide). The model still resolves **all atoms** downstream.
- **Ligands/ions/modified residues:** token = **atom** (more fine-grained, crucial for chemistry).
- Build a **heterogeneous graph**: residues (biopolymer) + atoms (ligands/ions), with edges encoding covalent links and spatial priors, then run Pairformer over it.

**TL;DR:** Coarse tokens for biopolymers, fine tokens for ligands. Edges carry geometry. The trunk learns an **SE(3)-aware** sense of space even before the diffusion decoder places atoms precisely.

---

## 4) Pairformer (replacing Evoformer): core ideas

Let **S** be single features (per token) and **P** be pair features (per token pair). One block conceptually cycles through:

1. **Triangle updates** on **P** (two directions): ensure consistency across triplets *(i → k → j)*.  
2. **Triangle self-attention** around starting/ending nodes on **P**.
3. **Transition/MLP** on **P**.
4. **Single attention with pair bias** on **S** (edges influence node attention).
5. **Transition/MLP** on **S**.

This preserves the **pair field** (metric of “who relates to whom”) that was critical to AF2, while simplifying and making it friendlier for **conditional generation** downstream.

**TL;DR:** Pairformer keeps the relational geometry brain (the pair field) but trims AF2’s Evoformer complexity for a generative setting.

---

## 5) Diffusion for 3D coordinates (the decoder)

We treat all **atom coordinates** \\(X \\in \\mathbb{R}^{N\\times 3}\\) as continuous variables.

**Forward (noising) process** (variance-preserving style):
\\[
q(\\mathbf{x}_t\\mid\\mathbf{x}_0) = \\mathcal{N}\\bigl(\\alpha_t\\,\\mathbf{x}_0,\\; \\sigma_t^2\\,\\mathbf{I}\\bigr), 
\\quad \\epsilon\\sim\\mathcal{N}(0,\\mathbf{I}), \\quad 
\\mathbf{x}_t = \\alpha_t\\mathbf{x}_0 + \\sigma_t\\,\\epsilon.
\\]

**Reverse (denoising) model** parameterized by network \\(\\theta\\) with **conditioning** \\(c\\) from the Pairformer trunk (sequences, MSA, templates, masks):
\\[
p_\\theta(\\mathbf{x}_{t-1}\\mid\\mathbf{x}_t, c) \\approx 
\\mathcal{N}\\bigl(\\mu_\\theta(\\mathbf{x}_t,t,c),\\; \\Sigma_t\\bigr).
\\]

**Loss (one common choice):** predict noise or “velocity” and do MSE:
\\[
\\mathcal{L}_{\\text{diff}} 
= \\mathbb{E}_{t,\\mathbf{x}_0,\\epsilon}\\bigl[\\|\\epsilon - \\epsilon_\\theta(\\mathbf{x}_t, t, c)\\|_2^2\\bigr].
\\]

- For **ligands**, we also care about **chemistry constraints** (bond lengths/angles, chirality, planarity). These are encouraged via the training data, geometry-aware features, and post-hoc relaxation; AF3’s confidence head helps pick samples that respect local chemistry.
- **Equivariance:** The task is **SE(3)-equivariant**; naively, the score should rotate/translate with the input. In practice, AF3 gains a lot from **pair features** that are built from **relative geometry** (distances/orientations), and training sees random global rotations so the network learns this behavior.

**TL;DR:** Add Gaussian noise to coordinates, train a net to remove it, condition on sequences/MSAs/templates. Sample several times → keep the confident, chemically sane structures.

---

## 6) Permutation issues (chains, identical ligands)

Real complexes can be **symmetry-ambiguous**:
- **Chain permutation:** Homomers (A2, A3, …) where swapping chains leaves ground truth unchanged.
- **Ligand multiplicity:** Multiple identical ligands; atom indices can be permuted.

One trains and evaluates with **permutation-invariant** objectives (e.g., align predictions to the best ground-truth permutation) so the model isn’t punished for symmetries.

**TL;DR:** Where labels are ambiguous, match by the best permutation (Hungarian-style assignments are common) before computing losses like MSE/RMSD.

---

## 7) What does the confidence head do?

- Outputs **calibrated confidence** for regions, interfaces, and ligands (think AF2’s pLDDT/pTM DNA but extended to complexes/ligands).
- Drives **inference-time scaling**: run multiple diffusion samples, score them, keep the best. You trade **compute for quality**—a very Karpathy-friendly concept.

**TL;DR:** Confidence is the model’s own “critic” for selection and ranking.

---

## 8) Practical outcomes for drug discovery

- **Rational, structure-based design:** We ask: *How does a new ligand sit in the pocket?* *What if we add a methyl or swap a ring?* AF3 gives a **pose hypothesis** quickly.
- **Binding affinity proxies:** Binding free energy \\(\\Delta G \\approx -kT\\ln K_d\\). AF3 is not a free-energy calculator, but its **accurate poses + confidence** are strong priors for ML or physics-based scoring (docking rescoring, MM/GBSA, alchemical FEP).
- **ADMET-in-the-loop:** Use fast ML models to predict **Absorption, Distribution, Metabolism, Excretion, Toxicity** on generated candidates. Keep a **live Pareto front** (potency vs. ADMET vs. novelty).
- **Physics buddies:** **Molecular dynamics (MD)** and **quantum chemistry (DFT/CC)** validate and refine. ML narrows the haystack; physics checks the needles.

**TL;DR:** AF3 turbocharges *what to try next*—poses + confidence → prioritize experiments and in silico screening.

---

## 9) Agentic orchestration: from molecules → organisms

A simple “Karpathy agent stack” for end-to-end reasoning and tooling:

1. **Hypothesis agent (biology):** propose targets/mechanisms based on omics, literature, prior knowledge.
2. **Structure agent:** call AF3 to generate **complexes** with ligands (and nucleic acids, if relevant). Use **multi-sample** and rank by confidence.
3. **Scoring agent:** estimate binding/strain/solvation; run **cheap ML scorers** first, physics later.
4. **Medicinal chemistry agent:** propose edits (R-group substitutions, scaffold hops) under **synthetic accessibility** constraints.
5. **ADMET agent:** predict liabilities (hERG, CYPs, permeability, clearance).
6. **Simulation agent:** short MD for stability; quantum patches for reaction centers.
7. **Planner agent:** maintain a **multi-objective** frontier (potency × ADMET × IP novelty × tractability). Suggest the **next experimental batch**.
8. **Learning loop:** ingest assay results, **fine-tune** scorers, update priors. Iterate.

**TL;DR:** Chain a few specialized tools with feedback. Keep humans-in-the-loop for hypothesis and sanity checks.

---

## 10) Glossary-level equations and metrics

- **RMSD (root-mean-square deviation):** \\(\\text{RMSD} = \\sqrt{\\tfrac{1}{N}\\sum_i \\lVert \\hat{\\mathbf{x}}_i - \\mathbf{x}_i \\rVert^2}\\). Used to compare predicted vs. true coordinates (after alignment).
- **Interface RMSD (iRMSD):** RMSD of interface atoms only.
- **pLDDT/pTM-like scores:** model-estimated local distance errors and overall topology correctness.
- **Confidence-weighted selection:** choose sample \\(\\arg\\max_s \\text{Conf}(\\hat{X}^{(s)})\\).

**Chemistry constraints (soft):** penalize bond deviations:  
\\(\\mathcal{L}_{\\text{bond}} = \\sum_{(i,j)\\in\\mathcal{B}} w_{ij}\\bigl(\\lVert\\mathbf{x}_i-\\mathbf{x}_j\\rVert - \\ell_{ij}^{\\ast}\\bigr)^2\\).

Overall training objective (schematic):  
\\(\\mathcal{L} = \\lambda_{\\text{diff}}\\mathcal{L}_{\\text{diff}} + \\lambda_{\\text{geom}}\\mathcal{L}_{\\text{bond}} + \\lambda_{\\text{conf}}\\mathcal{L}_{\\text{conf}}\\).

---

## 11) “How to use AF3 thinking” cheat sheet

- Always do **multi-sample** + **confidence rank**.
- Treat AF3 poses as **hypotheses**. Confirm with orthogonal signals (physics, experiments).
- Lean on **MSAs/templates** when available; AF3 can operate without them but confidence will tell you when it’s shaky.
- For ligands: verify **chemistry sanity** (valence, chirality) and **strain**.
- Push promising hits into **ADMET** and **MD** quickly; discard weaklings fast.
- Track **generalization**: if every new target requires heroics, you’re back in bottleneck (4). Build libraries of **portable tactics**.

---

## 12) Reading list (starter, non-exhaustive)

- **AlphaFold 2** — Jumper et al., *Nature* (2021).  
- **AlphaFold-Multimer** — Evans et al., *bioRxiv* (2021); follow-ups in 2022.  
- **Whole-proteome AF2** — Tunyasuvunakool et al., *Nature* (2021).  
- **AlphaFold 3** — DeepMind/Isomorphic Labs (2024 preprint/article).  
- **Eroom’s Law** — Scannell et al., *Nat. Rev. Drug Discov.* (2012).  
- **E(n)-Equivariant GNNs** — Satorras et al., *ICML* (2021).  
- **Equivariant diffusion for 3D molecules** — Hoogeboom et al., *ICLR* (2022).  
- **Score-based generative modeling** — Song et al., *NeurIPS* (2019–2021 series).  
- **wwPDB** — Berman et al., *Nucleic Acids Res.* (2000); current PDB houses ~180k+ structures.

---

## 13) One mental picture to keep

**AF3 = (Big relational brain) + (Geometry denoiser).**  
The brain (Pairformer) absorbs sequences/MSAs/templates; the denoiser (Diffusion) **writes atoms into 3D**. Confidence is your flashlight. Take multiple shots, keep the sharpest one, verify with physics, and ship the next experiment.

---

*End of notes.*



Target Discovery -> Target Validation -> Hit identification & Hit to lead -> Lead optimisation -> Pre-clinical -> Clinical Trials

Bottleneck 1 
Understanding Disease Biology

Bottleneck 2
Molecule Design

Bottleneck 3

Asserting compound quality 90% of candidates fail

Bottleneck 4

Success for one biological target does not usually generalise to the next target

Rational Structure- based drug design

How will an introduced ligand interact with our target interface?

How will changes in design change the way this ligand phisically interacts?

AlphaFold 2 won the CASP 14 (Competition / Small conference)

Sequence of aminoacids (SISFY....) -> Alfafold2 (Multiple Sequence Alignment, EvoFormer) -> Predicted protein

2021
AF2 -> one single protein chain

2022
AF Multimer -> multiple protein chain


2024
AF3 - fold protein, DNA, RNA, ligans


AF3 - diffusion model

AF3 produces better results


Pairformer - model architecture (you get an embedding from it) -> Diffusion Transformer


AF3 Model overview

Featurisation               ->          Trunk       ->          Confidence Head

Template Search
Genetic Search
Conform generisation

-> Input embedder (3 blocks) -> Template Module (2 blocks)
MSA Module 4 Blocks


Pairformer 48 blocks



Diffusion Model (Diffusion Iterations)


Confidence Module (4 blocks)

Ligand Molecules / Protein Sequences -> Featurisation -> Trunk -> Diffusion Module -> Confidence Head

Conditional generative Model

COnditioning is provided by large trunk network processing
- Input biomolecules
- MSA
- Templates

EvoFormer was simplified to PairFormer

Structure Model was replaced by a Diffusion Model

A token is 

a residue for standard protein/DNA/RNA residues
a single atom for ligand, ion, modified residues

Atom x coord

Pairformer is a graph

Pair representation (n, n, c) -> triangle update using outgoing edges -> triangle update using incoming edges -> Triangle self-attention around starting node
-> triangle self attention around ending node -> transition -> single attention with pair bias -> transition


ALDEN HUNG

Permute Ground Truth

Chain Permutation

10gs, A2 Homomer
Two copies of VWW ligand

Atom permutation within molecule

Predict (0,1,2,3,4,5,6) == (4,2,3,0,1,6,5)

DIffusion Module -> Gaussian diffusion on continuous 3D atom coordinates

MSE on atom coordinates

Protein Data Bank (accessible 180k structures)

The performance is given by the confidence head
one other application - inference time scaling (you can run more and more times)

Accurately modelling Binding Affinity enables in silico hit identification

ADMET property prediction enables real-time molecular property

Absorptiopn
Distribution
Metabolism
Excretion


Molecular Dynamics and Quantum CHemistry work alongside ML for Drug DIscovery

How do you orchestrate agents and applying models to frontline science?

Moving to

Molecular, cellular, tissue, organ, whole organism