from doctest import DocTest
from pyexpat import model


# Linear model

# Generalized Linear Model

# f(x,w,b) = WQ(x) + b

# Q(x) = [x^2, x] // feature engineering


# Function composition 

# W^2*theta(W^(1) * x + b^(1)) + b^(2)

# theta - activation function, nonliniarity

# theta coordinate by coordinate no learneable parameters

# ReLU

# theta(t) = t: t>=0,
#            = 0: t<=0


# For 3 dimensions,

# w^(2) * theta(w^(1) * x + b^(1)) + b^(2)

# theta in our case being the ReLU function

# the output is a piecewise linear function

# there is some redundancy in the model with the nr of parameters defined by W1 and W2

# this is called overparametrization

#nr of segments grows in the number of hidden dimensions. O(dimensions) - width of the network

# Making the model deeper

# sawtooth function

# g(x) = 2 * |x| - 1

#f0(x) = x 

# f2(x) = g(g(x))

# f3(x) = g(g(g(x)))

# f4(x) = g(g(g(g(x))))

# fn(x) = g(g(g(g(g(...g(x))))))

# n layer ReLU

# for each individual layer, it creates a sawtooth like function with power of 2 segments

# compleexity grows exponentially with the number of layers

# homework: write a proof, write a LEAN theorem

# second homework to implement it

# implement it using pythorch / JAX

# Invariances : 

# transformations Theta 

# f(T(x)) =  T * f(x) equivariance

# the best use of this are convolutions ( a particular kind of linear operations)

# equivariant under translation of coordinates

# Differantiable computing

# if-then-else  if x > 0, then return y, else return z;

#sigma(x)* y + (1-sigma(x))*z

# sigma - logistic sigmoid function

# sigma(x) * y = 0

# (1 - sigma(x)) * z = 1

# attention mechanism has a classical analog
# python dictionaries / maps


# residual computations (Res Net)

# x -> layer -> layer

# why do we lose information from a res net?

#instead of f(g(x))

# Transformers use this kind of composition

#f(g(x) + x) + g(x) + x # different kind of composition


# Learning # stochastic gradient optimization

# L(f(*, theta), D(ata))

# D_test (test data)

#L_test(f(*, theta), D_test)

# R(theta, D) = L(f(*, theta), D) empirical risk

# Algorithm 

# 1. Theta 0 - random initialization

# theta t + 1 = theta t - eta * grad_theta L(f(*, theta t), D) | evaluated at theta t

# learning -rate or step size

# Stochastic gradients

# Dt: minibatch of data sampled from D

# tradeoff: accuracy of the gradient  and speed of computation

# new insight: gradient noise can be useful

# yoy may find different , better use for theta

#bias to avoid parameters with high minibatch gradient variance

# GOOGLE DISTILL MOMENTUM GRADIENT DESCENT



# 5. 