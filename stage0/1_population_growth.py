import matplotlib.pyplot as plt

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


ypoints1 = scenario_history[0]
ypoints2 = scenario_history[1]
ypoints3 = scenario_history[2]

plt.plot(ypoints1, label="Scenario A")
plt.plot(ypoints2, label="Scenario B")
plt.plot(ypoints3, label="Scenario C")

plt.title("Population Change Over Time")
plt.xlabel("Years")
plt.ylabel("Population")
plt.legend()

plt.show()