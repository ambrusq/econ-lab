# STAGE 1 — Monte Carlo simulation

### Notes

**Stochastic (random) variable** - is described as a probabilistic distribution as opposed to a deterministic number
**Random draw** - a number taken from the distribution
**Discrete random variables** - countable values, usually whole numbers
**Continuous random variables** - can take any value across a range; infinite possibilities


**Uniform distribution** - each outcome is equally likely; we know the lower and upper bounds; 
- useful when little information is available about where the outcomes fall within the range
**Normal (gaussian) distribution** - center around its mean, symmetrical, most outcomes are close to the mean
- defined by mean and standard deviation
- theoretically allows unlimited values, so outcomes lower than -100% can happen, which isn't economically viable
- thus normality shouldn't be assumed just out of convenience
**Lognormal distribution** - asymmetric with a right tail
- useful in finance because it can't produce negative values - a company's value can grow extremely large, but can't be negative (I guess there is no such a thing as bankruptcy in financial modeling xD)
**Bernoulli distribution** - only two outcomes: 0 or 1
- something happens or it doesn't
**Binomial distribution** - many Bernoulli events

**Choosing a certain distribution to represent a variable is a model assumption** 

Once uncertainty around the trajectory is introduced in a model, one simulation isn't enough - thus we do Monte Carlo

**Standard deviation** - measures the typical magnitude of deviations from the mean; spread of the distribution

**Random outcome uncertainty** - while the parameters are defined, the next outcome is always uncertain
**Parameter uncertainty** - the parameters themselves could be wrong

**Correlation** - the degree to which two or more variables move together
- +1 - perfect positive linear correlation
- 0 - no linear correlation (non-linear is still possible)
- -1 - perfect negative linear correlation
- a.k.a. standardized covariance
- covariance divided by the product of two standard deviations

**Covariance** - tells us whether two variables tend to deviate from their means in the same direction 
- the basis of correlation - the units of the two variables can differ thus we need to standardize to interpret
- correlation * std_a * std_b

**Portfolio variance** - different from regular variance because the two or more variables interact with (depend on) each other based on their correlation
- A's variance + B's variance + interaction (covariance) term
$$
σP^2​=wA^2​σA^2​+wB^2​σB^2​+2 wA​ wB​ ρAB ​σA ​σB
$$
**Diversification** - the effect of reducing correlation
- a +1 correlation means potentially higher volatility (deviation from the mean)
- as we reduce it, the volatility gets reduced
- at 0 correlation, the interaction term is canceled out
- at -1 correlation the assets will cancel each others moves out, thus leading to 0 volatility
- correlation can matter more for overall volatility than individual asset standard deviations

**Uncorrelated ≠ independent**
- correlation only looks at linear relationships
- independence is stronger because it also implies that there is no other correlation besides linear, such as exponential

**Multivariate normal distribution** - formed by two or more random normal distributions

**Covariance matrix** - constructed so we can make random draws from a multivariate normal distribution


**Sensitivity analysis** - how does changing one parameter affect the results of the model
- If a small change results in a large change in the outcome, that means the model is highly sensitive to that parameter - this info should be taken into account when making conclusions
- Allows us to not need to know the parameters exactly, since we can just see how the model would fair under different estimates of the parameter
- **Local sensitivity** - small changes; "what happens if I'm slightly wrong?"
- **Global sensitivity** - explores a broad range of possible values
- **Interaction** - can happen between two or more parameters; when the effect of the change of one parameter depends on the value of the other parameter

**Robustness** - a model or conclusion is robust when it holds up across a wide reasonable range of parameters / assumptions
- Its opposite is fragile

**Scenario analysis** - changes multiple assumptions (parameters) at the same time to represent a situation
- Useful because in real life parameters rarely change in isolation

To estimate **how precise our estimate is** after a Monte Carlo simulation, we use **confidence intervals** and **standard error**

**Standard error** - uncertainty in the estimate of the mean
- sample standard deviation divided by square root of number of observations
- it's the standard deviation of the pertinent sampling distribution
- it answers: how much would the estimated mean fluctuate if I repeatedly took new samples of the same size

**Confidence interval** - gives a range describing the sampling uncertainty around the estimated mean
- E(mean) +- 1.96 * SE = 95% confidence interval
- it answers: how precise is my estimate of the expected mean (depends on the standard error)

*When coding simulations a rule of thumb is to: loop over time, vectorize across agents/simulations​*