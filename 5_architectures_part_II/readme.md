State Space Models

Replace Attention with recurrence

More natural to encode sequential data

Fast at inference

Linearity is sufficient due to the block structure (the MLP)

Linearity allows to diagonalize recurrence (computational efficiency)

Linear & Diagonal helps with : 
 - direct control of the linear system (e.g. stability)


 Benefits of Linear recurrences

 linear recurrences can be diagonalized

 x = Ax_k-1 + B_uk


 they can also be parallelized

 x_k = x_k-1 + Buk, y_k = C_xk


Controlability of the system

Eigenvalues on unit circle are pure sine waves
Eigenvalues nearer origin decay quickly

You can control how easily information dissapears, you can have good memory traces

TPU Architecture - Viperlite

Diagonal RNN

h_t = Alpha_t composed with h_t-1 + xt

Program

1. Load xt, Alpha_t and ht-1 from HBM -> VMEM

Program efficiency

VPU FLOPs 2 N L DBytes to read: 2 N L D + N L D


Why is linear attention important?

Connects Linear RNN to attention (the duality of the Mamba 2 paper)

Provides Mathematical Clarity (think deep linear models)

D Chalmers The evoelution of Learning: Experiments in genetics connectionism


In-Context learning by Induction Heads

The first attention head copies information from the previous token to each token

Going beyond linear transformers with recurrent 

Gated Delta Networks: Improving Mamba2 with Delta Rule

Taking a step forward: the Mesa-Layer vonOswald et al

Mixing RNN & Attention (RAT Bridging RNN Efficiency and Attention Accuracy, Wei et al 2025)

Generalization longer contexts: Filter Equivariant FUnctions

SMM models