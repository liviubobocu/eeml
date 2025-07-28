Results towards reasoning 


The Globality Barrier

Can transformers learn deductive reasoning?

Cornerstone of math reasoning, planning

Appears when we have a transitive relation

We can always model the problem with a directed graph

Can the model generalize to OOD samples with the same number of nodes/edges and the distance of the query nodes ( from {2,3,4} if connected)

a different generation process (cycles)

We consider a purified case without spurious correlations

2 cycles of size n, query nodes not connected

a cycle of size 2n, query nodes at distance n

Can transformers learn the two cycles task?

Time complexity appears to scale exponentially.

Globality degree - minimum nr of tokens needed along with the tokens histogram to achieve nontrivial correlation with the output

Example:
 - the k-parity problem x1, x2, ....xk has globality min{ k, n-k}
 - the cycle task has globality > n - 1 (as n - 1 edges are uninformative)


 More explicit and relevant to Transformers than previous measures:
 SQ (statistical query) dim, cross predictability, noise sensitivity, initial alignment

 What can Transformers learn
 Conjecture. A task is efficiently weakly learnable by a regular Transformer if and only if its globality is constant


 Chain of Thought

 Can we break the globality barrier?

 x1 .... xn => y1, y2, .... ym, auto-regressively
 ym = y (final label)

 Can we reach the target by taking small steps? (learning intermediate targets)


 Auto-regressive globality:

 The smallest number of tokens such that any target token yi is at most of globality k given the previous token x1 ... xn, y1, ... y_i-1

 Goal: 

 Each step to be constant gloablity of previously generated tokens and input

 Scratchpad: sorting edges from the source query node (i. e) DFS/BFS


 Chain of Sketch

 Single frame provide final solution as target during training

 Multi-frame (inductive scratchpad):

 provide intermediate solution as target during training
 train on various intermediate frames

 Turns a hard problem into a sequence of simpler ones

 GSM Symbolic

 Ideally, an intelligent system should be able to do formal/logical reasoning

 One good test-bed: math reasoning

 GSM8k: simple grade-school math ops

 GSM8k is very popular
 - high chance of data contamination

 GSM8K benchmark is static/fixed

 Performance distribution and variations
 GSM8K - 95% - GPT-4o

 Fragility of Reasoning

 If we change "apple" for "kiwi" in a sentence we see different results


 Performance drop on GSM - NoOP

 Illusion of thinking

 Controllable puzzle environments

 new setting to avoid contamination with controllable experiments

 fine grained complexity control: for example, number of disks, checkers, etc

analysis of both solutions and reasoning traces


Low complexity; Standard LLMs > thinking ones
Medium: Reasoning models gain clear advantage
HIGH: Both models collapse to 0% accuracy

As problems get hrder, reasoning models initially think mode (good) but then start thinking less despite
having plenty of token budget left.
They give up right when they should work harder

Catastrophic failure on exact computation

even when given the exact solution algorithm, reasoning models still failed at the same complexity points
this suggests fundamental limitations in symbolic manipulation, not just problem-solving strategy

LLMs need tools to perform better on algorithm solving (seeing the algorithm, executing the code)

Augmenting LLMs reasoning by reinforcing abstract thinking

X -> Y
X~ -> Y~

2 problems X and X~, with solutions Y and Y~ with solutions Y and Y~ share the same high level knowledge or reasoning schema

A common strategy: Robustifying by Instantiation

Learning more instances of the reasoning problem to anticipate potential distribution shifts

But computational expensive

Modelling more general "abstraction" of reasoning, without scaling up the training data.

Robustifying by abstraction

1. Condition Recognition
2. Abstract Reasoning (Core Step)
3. Abstract Retrieval


Chain of abstraction paper

AbstraL model

RL for reasoning by adaptively revealing rationales

Task: verifiable, often one solution per question is available
GSM8K and MATH dataset for mathematical reasoning

Standard RL process:

We give questions 

Adaptive Backtracking (AdaBack)

p_t^(i): Sampled portion for question i at epoch t
r: the average reward for this question given by GRPO
depending on r (difficulty of the sample), we reveal more or less at next epoch

Particularly advantageous for small problems