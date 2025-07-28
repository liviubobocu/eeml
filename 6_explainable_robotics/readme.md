Explainable AI

Transparent by design systems

Post-hoc Explanation (black-box explanation)

Input Data -> Black Box System - y

Interpretability -> Transparent System


Post hoc Explanation 

Input -> AI Blackbox -> y^

Explanation subsystem -> explanation

Explainability vs Interpretability vs Mechanistic interpretability

Interpretability - how well a human (often a developer/researcher) can make sense of model's logic

Mechanistic Intepretability - subtype of interpretability focused on low level understanding of model internals

Explainability - explaining the whole interaction

Map planning for robots as MDP

or map planning as symbolic planning

Representation language eg PDDL, STRIPS

Robot has a model

Domain file(predicates and actions)

Problem file(objects, initial state and goal specification)

Then apply a PLANNER over this -> PLAN (sequence of actions)


Explainable planning, Fox et al, 2017

Why DIdn't you do something

Providing a contrastinve example by taking the suggestion 


s - planning state

g - goal state

r- alternative state

A - action

The hypothetical alternative would be a plan that is not better than the one found by the planner or a plan which is better than the original one

Interaction between humans and AI Systems (robots)

pi_H -> interaction -> pi_R


Generative contrastive explanation (CE)

Providing a contrastive example by taking suggestion of a user into account


Iterative process to explainable planning (XAIP)

https://planning.wiki/
https://github.com/fjrodl/PDDL-course/blob/main/Slides/PDDL-Session.pdf


Composition of Compilations

XAIP as a service

Producint the alternative plan XPlan


Model -> XModel Generation -> XModel -> XPlanSynthesis -> XPlan

Planner -> XPlan Synthesis

Plan -> Validate Xplan <-> XPlan

CE = <comparison, report,>


XAIP as a service


Planner performance
Plan qualities

Symbolic planning community - most planners are not optimal

https://www.youtube.com/watch?v=_NOVa4i7Us8

https://www.cs.toronto.edu/~sheila/2542/w09/A1/introtopddl2.pdf

https://fareskalaboud.github.io/LearnPDDL/

RosPLAN - robots operating system


Explanations in Robot Motion Planning

Explaining trajectory selection
Environment based justification
Deviations and failure recovery

https://arxiv.org/pdf/2002.06432

VIsual explanations of local path with GAN

Local interpretable model agnostic explanations (LIME)

https://github.com/tomsilver/pddlgym

https://github.com/Farama-Foundation/Gymnasium

https://farama.org/projects

