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
def simulate_wealth(wealth, contribution, p_returns=p_returns, observations=p_returns.shape[0], years=p_returns.shape[1]):
    wealth_simulations = []
    final_wealth = []
    for e in range(observations):
        wealth_trajectory = []
        x = wealth
        for i in range(years):
            x = x * (1 + p_returns[e, i]) + contribution
            wealth_trajectory.append(x)
        wealth_simulations.append(wealth_trajectory)

    for i in range(observations):
        observation = wealth_simulations[i][years - 1]
        final_wealth.append(observation)

    return wealth_simulations, final_wealth

wealth_simulations, final_wealth = simulate_wealth(100000, 10000)

# print(len(wealth_trajectory))
# print(len(wealth_simulations))
# print(len(wealth_simulations[1]))
# print(np.mean(wealth_simulations))
# print(np.std(wealth_simulations))

def analyze_results(final_wealth=final_wealth, wealth_simulations=wealth_simulations):
    # Expected wealth at 20 years
    e_wealth = round(np.mean(final_wealth), 2)
    print("Expected Final Wealth")
    print(e_wealth)

    # Sample standard deviation
    print("Sample standard deviation")
    print(round(np.std(wealth_simulations), 2))

    # Median final wealth
    print("Median Final Wealth")
    print(round(np.median(final_wealth), 2))

    # Probability of W_20 > 500k
    count = 0
    for i in final_wealth:
        if i > 500000:
            count += 1

    prob_500k = count / len(final_wealth)
    print("Probability of Final Wealth above 500k")
    print(str(round(prob_500k * 100, 2)) + "%")

    # Alternative solution using boolean mask
    x = np.array(final_wealth)
    mask = x > 500000
    result = x[mask]
    # print(len(result)/len(final_wealth))

    # Probability of W_20 > 750k
    x = np.array(final_wealth)
    mask = x > 750000
    result = x[mask]
    print("Probability of Final Wealth above 750k")
    print(len(result)/len(final_wealth))

    # Probability of losing money
    count = 0
    for i in final_wealth:
        if i < 0:
            count += 1

    prob_neg = count / len(final_wealth)
    print("Probability of Final Wealth below 0")
    print(str(round(prob_neg * 100, 2)) + "%")

    # Plots and percentiles
    plt.hist(final_wealth)
    plt.title("Histogram of Final Wealth")
    plt.xlabel("Observations")
    plt.ylabel("Wealth")
    # plt.show()

    print("5th Percentile")
    print(round(np.percentile(final_wealth, 5)))

    print("25th Percentile")
    print(round(np.percentile(final_wealth, 25)))

    print("50th Percentile")
    print(round(np.percentile(final_wealth, 50)))

    print("75th Percentile")
    print(round(np.percentile(final_wealth, 75)))

    print("95th Percentile")
    print(round(np.percentile(final_wealth, 95)))

    # Confidence intervals
    st_error = np.std(final_wealth) / math.sqrt(observations)

    print("Standard error")
    print(st_error)

    ci_p = e_wealth + 1.96 * st_error
    ci_n = e_wealth - 1.96 * st_error
    ci = [int(round(ci_n)), int(round(ci_p))]

    print("95% Confidence Interval")
    print(ci)