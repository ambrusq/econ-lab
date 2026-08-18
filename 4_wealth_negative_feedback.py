import matplotlib.pyplot as plt

household_wealth = 80
income = 18
a = 15
b = 0.01

years = 30

spending_trajectory = []
wealth_trajectory = [household_wealth]
saving_trajecory = []

for year in range(years):
    spending = a + household_wealth * b
    spending_trajectory.append(spending)
    household_wealth = household_wealth + income - spending
    wealth_trajectory.append(household_wealth)
    saving_trajecory.append(income - spending)

plt.subplot(1,3,1)
plt.plot(range(years+1), wealth_trajectory)
plt.title("Wealth")

plt.subplot(1,3,2)
plt.plot(range(years), spending_trajectory)
plt.title("Spending")

plt.subplot(1,3,3)
plt.plot(range(years), saving_trajecory)
plt.title("Saving")

plt.show()