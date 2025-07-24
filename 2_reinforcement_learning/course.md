## RL

Challenges: 

1. problem of delayed rewards

2. exploration problem ( gets reward when you find the treasure, nothing without)

3. thirst for data (inefficient on samples)

4. reward hacking (good at finding issues in your system)


Deep Q Learning

Reward signal: game score provided a frequent anc contiunous reward, making the feedback much less delayed

Exploration: Constant feedback from score naturally guided the AI towards useful actions

Data Inneficiency: Solved by running the game simulator much faster than real time, playing thousands of games per hour

Convolution -> Convolution -> Fully COnnected

Other applications:

Learning dexterous skills (Robotics)

Reward Signal - carefully shaped reward provides frequent feedback (small rewards for progress)

Application 4 - Control Systems (Fusion Control) - Control nuclear fusion plasma


DeepMind AI learns to control nuclear plasma

The reward signal was a continuous signal based on how closely's plasma's current shape matched the desired target shape

Exploration: The continuous reward signal guided the AI towards promising areas of the vas controls space

Data Inefficiency: Made possible by a highly accurate, trusted simulator of the tokamak's physics, allowing for rapid, safe learning


Challenge of language: AI Assistants

Problem: LLMs are pre-trained on the internet. They know a lot, but they don't know our values

RLHF

AI Assistants: Learning to Reason

Instead of just guessing, the AI Learns ot think through a problem

Reasoning through math problems

The reward signal: The goal is a simple verifiable outcome (+1 if the final answer is correct) which avoids the ambiguity of defining a good reasoning step

Exploration: Greatly simplified by starting with a pre-trained model that already knows how to code or do math. Exploring strategies, not learning the basics

Data Inefficiency: We can autogenerate a near infinite number of math or coding problems

Reinforcement Learning: An introduction

Reward is typically a scalar feedback signal

We frame RL Markov Decision Process

=> basic way to describe an agent loop: set of states, set of of actions, transition function, reward function, discout factor

State space

- 4 unique states in this environment

s0, s1, s2, s3 (4 squares, each with a smiley face)

- action space: (Up, Down, Right, Left)

- Transition Model ( State Machine with reward function)

Markov property - the next state depends only on the previous state, and not all states that come before it

Agent's goal - max the discountet sum of future rewards


Gt = r_t + y * r_t_+_1 + y2 * r_t_+_2

Discount y specifies how much future rewards are worth compared to intermediate reward

Policy maps states to actions

a_t = 

State Value function

State value function maps states to expected rewards

maps an action in a given state to expected rewards