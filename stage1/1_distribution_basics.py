import numpy as np
import matplotlib.pyplot as plt

mean = 0.08
sd = 0.30
observations = [10, 100, 1000, 10000, 100000]

distributions = []

counter = 0

while counter < len(observations):
    data = np.random.normal(mean, sd, observations[counter])
    distributions.append(data)
    counter += 1

print("N = 10")
print(np.mean(distributions[0]))
print(np.std(distributions[0]))

print("N = 100")
print(np.mean(distributions[1]))
print(np.std(distributions[1]))

print("N = 1000")
print(np.mean(distributions[2]))
print(np.std(distributions[2]))

print("N = 10000")
print(np.mean(distributions[3]))
print(np.std(distributions[3]))

print("N = 100000")
print(np.mean(distributions[4]))
print(np.std(distributions[4]))

plt.hist(distributions[4])
plt.xlabel("Annual Return")
plt.ylabel("Observations")
plt.title("Probability Distribution of Annual Investment Returns ")
plt.show()