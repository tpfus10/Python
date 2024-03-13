import matplotlib.pyplot as plt

fig, ax = plt.subplots()  

def scatter (x, y, label):
  ax.scatter(x, y, label=label)

x1 = [1, 2, 3, 4]
y1 = [2, 3, 4, 6]
scatter(x1, y1,'blue')  


x2 = [1, 2, 3, 4]
y2 = [1, 2, 3, 4]
scatter(x2, y2, 'yellow')  

ax.legend()
ax.set_title("Plot A and B")
ax.set_xlabel("Age")
ax.set_ylabel("BMI")
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
plt.savefig('plot.png')
plt.show()

