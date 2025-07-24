Graph Representation Learning

Social Networks, Biological Networks, Transportation Networks, Molecules

Processing graph structured data

1D Signal, 2D signal, graph signal

Graph ML 

irregular domain graphs -> f(G,X) -> node classification, link prediction, graph classification, graph clustering

Predominant graph representation learning paradigms

Hand-crafted graph theoretic features
Kernel-based features
Graph Signal processing based features
Shallow embeddings

Deep embeddings: GNNs
Topological Features
Persistent Homology
Manifold learning & Topology Inferences
Graph generative models


Embeddings on graphs: Definition

Given an input graph G = (V,E,W), the goal is to convert G (or a subgraph, or a node) into a d << |V| dimensional space
in which graph properties are preserved

Graph properties can be quantified using proximity measures on the graph (e.g. K-hop neighborhood)

Graph -> feature embeddings -> tasks

Limitations

- hand crafted features are optimized embeddings, often focused on graph structure


Graph -> features/embeddings -> Traditional ML Tasks

Recap of classical Graphs

Undirected graph Of N Nodes, i e |V| = N

G= (V, E, W)

W_ij = { 
    w_ij,
    0
}

Graph Laplacian Matrix

The Combinatorial Laplacian is defined as: L = D - W

Symmetric
Of-diagonal entries non-positive
Rows sum up to 0
It is a positive semi-definite matrix

A discrete differential operator

(Lf)(i) = sum W_i,j (fi - fj)

The graph analog to the Laplace operator on continuous functions

Laplace operator can be replicated by second order derivative

Laplace approximation of the continuous operator

The Fourier Transform

- represent your data into the spectrum domain

Graph Fourier transform

The eigenvectors of the Laplacian provide a harmonic analysis of graph signals

By exploiting the orthonormality of the eigenvectors, we obtain

Graph Fourier Transform: 

Inverse Graph Fourier Transform

Towards a convolution on graphs:

A spectral viewpoint

Key Intuitition: Convolution in the vertex doamin is equivalent to multiplication in the spectral domain

We define convolution on graphs starting from the multiplication in the GFT domain

Graph Spectral Filtering

It is defined in direct analogy with classical filtering in the freq domain

Filtering a graph signal x with a spectral filter g(*) is performed in the graph
Fourier domain

Convolution on graphs is equivalent to filtering

Permutation Invariance

Permutation Equivariance

Graph structure is independent of the labelling of the nodes from how we choose to draw them

Node representations should be permutation equivariant

GNN Model: schematic overview

GNN building blocks (graph convolution, pooling, nonlinearity)

Classification layer

Is the graph convolution Localized?

Generally, no. If we consider polynomial filters, the answer is yes

The basic GGN: a spectral viewpoint

Typical GNN architectures consist of a set of graph convolutional layers, each of which is followed by element-wise nonlinearity

Towards a graph convolution: A spatial viewpoint

Key Intuition: Generalize the notion of convolution from images ( grid graph)  to networks (irregular graph)

Spatial Graph Convolution

Main issue: we cannot have variable number of weights: it requires assuming an order on the nodes

Solution: Impose same filter weights for all nodes

First GNN architectures

Original GNN

Spectral GCNN

ChebNET

GCN

GCN Architecture

Input -> hidden Layer -> RELU -> HIdden Layer - RELU -> Output

They are not very large

MPNN  - Message Passing Neural Network

Graph Isomorphism network

Graph attention networks - you give relative importance to your nodes

Graph Transformers

https://www.youtube.com/live/_wLePNLzO38