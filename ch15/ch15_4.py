import matplotlib.pyplot as plt

fig, ax = plt.subplots()

N = [1, 2, 3]
K = [50, 70, 20]
E = [30, 50, 70]

ax.plot(N, K)
ax.plot(N, E)
ax.set_xticks(["홍길동", "이순신", "감강찬"])


plt.show()