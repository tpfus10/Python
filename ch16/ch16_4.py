from matplotlib import pyplot as plt
from random import randint

fig, axs = plt.subplots(1, 2)


# x1 = [randint(1, 10) for _ in range(100)]
# y1 = [randint(1, 10) for _ in range(100)]

# x2 = [randint(1, 10) for _ in range(100)]
# y2 = [randint(1, 10) for _ in range(100)]

x1 = list(range(1, 6))
y1 = [i*i for i in x1]

x2 = list(range(1, 6))
y2 = [i**3 for i in x1]

# x = [1, 2, 3, 4, 5, 6, 7]
# y = [i**2 for i in x]
# print(x, y)

# plt.plot(x, y)

# plt.scatter(x1, y1)
# plt.scatter(x2, y2)

# plt.plot(x1, y1)
# plt.plot(x2, y2)

axs[0].plot(x1, y1)
axs[0].plot(x2, y2)

plt.plot(x1, y1, label='A', color='red')
plt.plot(x2, y2, label='B', color='blue')

# axs.legend()
# ax.grid()

# ax.set_aspect('equal')
# plt.set_title('cat')
# plt.set_xlabel('age')
# plt.set_ylabel('height')

plt.show()