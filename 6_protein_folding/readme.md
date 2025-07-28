AlphaFold 

Eroom's Law

Biology         ->      Chemistry       ->      Execution

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