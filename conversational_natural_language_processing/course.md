y = f(x)
x - context 
y - next word
f_theta - diff function in theta - transformer with a softmax output layer

x0 - prompt
y0 - f0(x0)

x1 = x0*y0
y1 = f(x1)

Pretraining  

- take digital material
- minimize cross entropy loss

Supervised fine-tuning 

- next token pred designed dataset {x, y} contained in D

RL

- agent interacts with environment
- in state s_t, takes an action a_t, receives a reward r_t
- return a discounted sum


- aim is to find the best policy (most return)

the policy is differentiable - policy gradient theorem to compute the gradients
PPO (Proximal Policy Optimization)

Context is state
Next token is an action
our language model is the policy

Reward model ??

Preference optimization

{x, y, y'} contained in D

r = g(xy), where 

x is a prompt
y is a potential response
r numerical model ?? (needs more info)

r function - if the next token is the end of the sentence you get 0, otherwise you get the reward model

InstructGPT

Task Oriented Dialogue

The user has a goal in the conversation
System interfaces with an external knowledge base in order to fulfil the goal

ontology - described in terms of domains, slots and values, system actions and user interactions
goal - each dialogue is labeled with success or failure
annotations - dialogue states, system actions and user intentions

MultiWoZ
https://github.com/budzianowski/multiwoz

EmoWOZ - extension of MultiWoZ - includes emotion

ConvLab toolkit

User simulator - simulates 


Dynamic dialogue policy transformer (DDPT)

Forward transfer by encoding domain, slots and values, system actions and user intents in NL
Prevents forgetting by operating with discrete (unbouded) nr of domains, slots, values, system actions and user intentions


Simulated Environment

A challenging simulated environment for continual learning
Domains occur again

Episodic and lifetime objective

Episodic/Lifetime reward

CLEAR algorithm - RL algorithm - maximizing entropy of possible actions (allowing explorations) and regularizing towards possible behaviors 

Meta Learning - let the agent on its own when to maximize the entropy or to regularize towards past behavior


DDPT can include emotion


Agentic approach better than chat system

Train LLM on external DB, use RL for emotion - reduces hallucination



Reinforcement learning from self feedback (RLSF)

- force the model to output the "your answer is"
- tell the model to give an accuracy

We can perform topological data analysis to determine the size of the space in which a word is found

Local dimension predicts grokking