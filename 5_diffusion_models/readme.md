Generative Modelling Problem

Unknown data distribution p1

Given: samples x1 ~ p1

Goal: learn a sampler from this density p1


Learn: neural network with parameters theta

Generative Model

x0 ~ p0 -> Generator -> x1 ~ p1

Sampling

x0 ~ p0

Density Estimation

Autoregressive Models

GANs

VAEs

Dynamical Systems as Generative Models
The Generator will take a notion of time and a spatial variable and learn how to transform this
By transforming this, the generator learns a process

How does an individual particle change under process

x_t+1 = x_t + f(x_t, ....)*dt

Deterministic and Stochastic Dynamics

ODE

d*x_t = u_t(x_t)dt

SDE 

dx_t = f_t(x_t)*dt + g_t*dw_t

The stochastic one is not deterministic and it has irregular shape

Euler - Maruyama

Diffusion Models

dx_t = f_t(x_t)*dt + g_t*dw_t   Data -> Noise
Reverse SDE dx_t = (ft(xt) -)                   // complete formula needed

Denoising score matching

Gaussian Noising Kernel

pt(x_t) = integral of p(x_t/p)*p_data(x)d_t

Variance Exploding
Variance Preserving


Flow Matching for Generative Modelling

Building Normalizing Flows with Stochastic

Core Principle: 

Find a tractable training objective

Conditional Optimal Transport Flows

Affine conditional flow

Diffusion models have noisy trajectories because of the brownian motion


Discrete Diffusion and FLow Matching Gat et al 2024

Reverse Generative Process


Model is mean parametrization

Generative models in Science

Generative Samplers of Boltzmann densities

Molecular Dynamics - simulate the equations of motion for particles

