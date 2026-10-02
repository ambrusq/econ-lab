### Notes
### Class 1: What Is a Simulation?

**Model** - a deliberately simplified representation of some aspect of reality
**Abstraction** - deciding what matters for the question and ignoring the rest
**Assumptions** - should be clearly stated, even if they are implicit
**Model** - a structured (math notation) representation of a system
**Variable** - part of the model that can change
**Parameter** - quantity in the model, which is usually held fixed for a simulation, e.g. growth rate
- the distinction between these two isn't fixed and can change from model to model
**State** variable - the information necessary to describe a system at a certain point in time; carries the system forward by varying from period to period
- a model can be called a state-transition system because we can move its state through time
**Transition rule** - how we get from one state to another; basically the formula of the model
**Initial condition** - variable/state at time 0
**Simulation** - the execution of a model over time to generate possible outcomes
**Simulation trajectory** - the whole sequence of variable over time
**Deterministic system** - no randomness, the outcome is always the same given same conditions and parameters
**Stochastic system** - randomness included, more akin to reality; defines a set of possible trajectories
**Randomness** - uncertainty is represented with a probabilistic model
**Time discretization** - a form of abstraction, 1 min time steps may be too complicated, 1 year time steps may miss short-term fluctuation.
**Feedback** - in its simplest it's when current state influences future state; there can be more feedback loops in a model which makes them more complicated but simulation helps understand the relationship, e.g.: Dt+1​=Dt​(1+r)+PD

Most important part is comparison with reality:
**Calibration**
Choose parameters so the model reproduces known empirical characteristics.
**Validation**
Test whether the model reproduces observations that weren't directly used to construct it.
**Sensitivity analysis**
What happens if we change the assumptions or parameters?
**Robustness**
Does the conclusion survive reasonable alternative specifications?

State_t+1​=f(State_t​,Parameters,Randomness)​

Adding complexity doesn't mean the results will be better. Less is more.

**Empirical probability** - the likelihood of outcomes coming from within the model (not accounting for the model's accuracy)

2 layers of uncertainty: 
- Within-model uncertainty - what outcomes occur according to the accepted model? 
- Model uncertainty - how confident are we that the model reflects reality?

**Mode** - most likely outcome
**Expected value** - probability-weighted average of outcomes

### Class 2: Building a Computational Model

**Transition function** - abstract representation of the model; helps by showing the state variables and parameters, e.g.: D_t+1​=f(D_t​;θ)
**Exogenous** variable - comes from outside the model; pre-specified
**Endogenous** variable - has a component from within the model; e.g. a feedback component
There are parameters within variables.

Models should be interpreted economically and not just mathematically. They carry assumptions about the system itself.

**Parameter experimentation** - changing a certain parameter while holding others constant can help answer economic questions; basic form of sensitivity analysis

Question→Mechanism→Assumptions→Mathematical model→Algorithm→Simulation​

**Simulation** - an executable representation of a set of assumptions about how a system evolves

**Structural assumptions** - about the parameters and variables
**Omissions/scope conditions** - what to leave out on purpose

### Classes 3, 4, 5

**Positive feedback** - divergence from equilibrium creates forces that increase divergence; potentially explosive

**Lambda (λ)** - rate of adjustment
**Convergence** - movement towards equilibrium
**Negative** **feedback** - divergence from equilibrium creates forces that reduce divergence; potentially stabilizing
**Oscillation** - happens when lambda is too large and the model overshoots the equilibrium; if it's moderately large, convergence may still happen, but if it's too large, the system can oscillate increasingly further form equilibrium

### 3 questions for computational models:
"Can the model reproduce the data (historical patterns)?"
**Empirical fit.**
"Does the model's mechanism make economic sense?"
**Structural plausibility.**
"Does the model continue to work on observations it wasn't fitted to?"
**Predictive/out-of-sample performance.**
⬇️
Always evaluate: **Complexity vs. Explanatory power vs. Out-of-sample performance**