import matplotlib.pyplot as plt

interest_rates = [0.03, 0.05, 0.07]
contribution = 2000
years = 30

scenario = []
counter = 0

while counter < 3:
    wealth = 10000
    wealth_trajectory = [wealth]
    for year in range(years):
        wealth = wealth * (1 + interest_rates[counter]) + contribution
        wealth_trajectory.append(wealth)
    scenario.append(wealth_trajectory)
    counter += 1

print("Scenario A after 30 years:")
print(round(scenario[0][30], 2))
print("Scenario B after 30 years:")
print(round(scenario[1][30], 2))
print("Scenario C after 30 years:")
print(round(scenario[2][30], 2))

plt.plot(scenario[0], label = "Scenario A")
plt.plot(scenario[1], label = "Scenario B")
plt.plot(scenario[2], label = "Scenario C")

plt.title("Compund Interest Effects")
plt.ylabel("Wealth")
plt.xlabel("Years")
plt.legend()

plt.show()