import matplotlib.pyplot as plt
import random

fig, ax = plt.subplots()

data = [random.randint(0, 100) for _ in range(100000)]
ax.hist(data)
plt.show()