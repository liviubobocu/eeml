Gradient Descent

The problem with gradient descent visualized:

Large learning rate: 

Small learning rate:

2nd order methods

Approximate h(theta) by its 2nd order Taylor series around current theta:

Trust regions and damping

If we take R = { d: ||d||2 <= r }
argmin (h(theta) + delta h (theta)^T + 1/2 dT)

A better global approximation 

A more conservative approximation

The most popular alternative curvature matrices / preconditioners are:

Generalized Gauss - Newton matrix (GGN)

Fisher information matrix

Empirical Fisher

Nice properties:

always positive semi-definite (i.e. no negative curvature)

give parametrization invariant updates in small learning rate limit (unlike Newton's method)

Diagonal approximations:

The simplest approximation: include only the diagonal entries of curvature matrix (setting the rest to zero)

Properties:
 - inversion and storage cost: O(n)
 - computational costs depends on form of original matrix (ranges from easy to hard)
 - unlikely to be accurate, but can compensate

 Kronecker - product approximation

Block - diagonal approximation of GGN / Fisher where blocks correspond to network layers
Approximate - each block as Kronecker product of two small matrices

Storage and computation cost: O(n)*

Cost to apply inverse: O(b^0.5n)


Stochastic methods:

Stochastic Gradient Descent

SGD replaces h(theta) with its mini-batch estimate delta_h(theta), giving:

theta_k+1 = theta_k - alpha_k * delta_h(theta_k)

To ensure convergence, needs to do one of the following:
- decay learning rate
- use polyak averaging

Stochastic 2nd-order and momentum methods

Mini-batch gradient estimates can be used with 2nd order methods too, giving the preconditioned gradient update

Brief history

1990s SGD, R-prop
basic diagonal Hessian approximations

2000s second AI winter, all but a few groups abandoned neural nets
natural gradient methods developed, but remain impractical for deep net training

natural gradient methods being developed, but remain impractical for deep net training

Current state of affairs

RMSProp / Adam, over 10 years old

Convergence bound for the NQM

Different cases for the NQM have been analyzed by the literature

Constant learning case

Denoting theta_k = 1/ (k+1)
and choosing the maximum allowable learning rate alpha = 1\gamma(B^-1H*)
which is optimal here, assuming a constant learning rate (LR), we have

