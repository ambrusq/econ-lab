import numpy as np
import math
import matplotlib.pyplot as plt

wealth = 100000
contribution = 10000

equities_mean = 0.09
equities_std = 0.2
equities_weight = 0.7

bonds_mean = 0.04
bonds_std = 0.07
bonds_weight = 1 - equities_weight

correlation = 0.2

years = 20

observations = 100000

# Calculate the portfolio's E[R], var, and STD
p_expected_return = equities_weight * equities_mean + bonds_weight * bonds_mean
p_variance = equities_weight ** 2 * equities_std ** 2 + bonds_weight ** 2 * bonds_std ** 2 + 2 * equities_weight * bonds_weight * correlation * equities_std * bonds_std
p_std = math.sqrt(p_variance)

# print(p_expected_return)
# print(p_variance)
# print(p_std)

# Multivariate Normal Distribution
def simulate_returns(equities_mean, equities_std, equities_weight, bonds_mean, bonds_std, correlation, observations, years):
    covariance = correlation * equities_std * bonds_std
    mean = [equities_mean, bonds_mean]
    covariance_matrix = [[equities_std ** 2, covariance], [covariance, bonds_std ** 2]]
    x = np.random.multivariate_normal(mean, covariance_matrix, size=(observations,years))
    p_returns = equities_weight * x[:, :, 0] + (1 - equities_weight) * x[:, :, 1]
    return p_returns

# Base case
p_returns = simulate_returns(0.09, 0.2, 0.7, 0.04, 0.07, 0.2, 100000, 20)

# print(x.shape)
# print(x[:,:,1])
# print(p_returns.shape)

# Simulation of wealth
def simulate_wealth(wealth, contribution, p_returns):
    wealth_simulations = []
    final_wealth = []
    for e in range(p_returns.shape[0]):
        wealth_trajectory = []
        x = wealth
        for i in range(p_returns.shape[1]):
            x = x * (1 + p_returns[e, i]) + contribution
            wealth_trajectory.append(x)
        wealth_simulations.append(wealth_trajectory)
        final_wealth.append(wealth_trajectory[-1])

    return final_wealth

final_wealth = simulate_wealth(100000, 10000, p_returns)

# Test lines
# print(len(wealth_trajectory))
# print(len(wealth_simulations))
# print(len(wealth_simulations[1]))
# print(np.mean(wealth_simulations))
# print(np.std(wealth_simulations))

# Analysing the simulation results
def analyze_results(final_wealth, percentile):
    # Expected wealth at 20 years
    e_wealth = np.mean(final_wealth)

    # Sample standard deviation
    sstd = np.std(final_wealth, ddof=1)

    # Median final wealth
    median = np.median(final_wealth)

    # Probability of W_20 > 500k
    count = 0
    for i in final_wealth:
        if i > 500000:
            count += 1

    prob_500k = count / len(final_wealth)

    # Alternative solutions using boolean masks (complicated approach)
    # x = np.array(final_wealth)
    # mask = x > 500000
    # over_500 = x[mask]
    # print(len(over_500)/len(final_wealth))

    # Probability of W_20 > 750k (simpler approach)
    x = np.array(final_wealth)
    mask = x > 750000
    prob_750k = mask.sum() / len(final_wealth)

    # Probability of losing money (most simple approach)
    x = np.array(final_wealth)
    prob_0 = (x < 0).mean()

    # Plots and percentiles
    plt.hist(final_wealth)
    plt.title("Histogram of Final Wealth")
    plt.ylabel("Observations")
    plt.xlabel("Wealth")

    # NumPy could take the list of percentiles and calculate all of them at once, thus no need for this
    percentiles = {}
    for i in percentile:
        percentiles.update({i : np.percentile(final_wealth, i)})

    # Confidence intervals
    st_error = sstd / math.sqrt(len(final_wealth))

    ci_p = e_wealth + 1.96 * st_error
    ci_n = e_wealth - 1.96 * st_error
    ci = [int(round(ci_n)), int(round(ci_p))]

    return {
        "expected_wealth": e_wealth,
        "std": sstd,
        "median": median,
        "prob_500k": prob_500k,
        "prob_750k": prob_750k,
        "prob_negative": prob_0,
        "percentiles": percentiles,
        "standard_error": st_error,
        "confidence_interval": ci
    }

percentile = [5, 25, 50, 75, 95]

results = analyze_results(final_wealth, percentile)

print("Expected Final Wealth")
print(round(results["expected_wealth"], 2))
print("Median Final Wealth")

print("Probability of Final Wealth above 500k")
print(str(round(results["prob_500k"] * 100, 2)) + "%")

print("Probability of Final Wealth above 750k")
print(str(round(results["prob_750k"] * 100, 2)) + "%")

print("Probability of Final Wealth below 0")
print(str(round(results["prob_negative"] * 100, 2)) + "%")

print("Standard error")
print(results["standard_error"])
print("95% Confidence Interval")
print(results["confidence_interval"])

for x in results["percentiles"]:
    print(str(x) + "th Percentile")
    print(round(results["percentiles"][x], 2))

# plt.show()