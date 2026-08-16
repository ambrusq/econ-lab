birth_rates = [0.01,0.02,0.03]
death_rate = 0.015

scenario_history = []

counter = 0

while counter < 3:
    population = 1000
    population_history = [population]
    for year in range(100):
        population = population * (1 + birth_rates[counter] - death_rate)
        population_history.append(population)
    scenario_history.append(population_history)
    counter += 1

print("Scenario A:")
print(scenario_history[0][100])

print("Scenario B:")
print(scenario_history[1][100])

print("Scenario C:")
print(scenario_history[2][100])

# Task 2 — Plot the trajectories

# Use matplotlib to create a single graph containing the three trajectories.
