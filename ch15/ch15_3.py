import matplotlib.pyplot as plt

x = list(range(1, 31))
sqaure = lambda x : [i**2 for i in x]

fig, ax = plt.subplots()
# ax.scatter(x, sqaure(x), color = "darkblue", label="scatter")
# ax.plot(x, sqaure(x), color = "blue", label="plot")

#컬러맵 사용하기
plt.scatter(x, sqaure(x), c=sqaure(x), cmap=plt.cm.Oranges, label="scatter")
plt.colorbar()

ax.legend()
ax.set_title('SQURE', fontsize = 20)
ax.set_xlabel('X', fontsize = 15)
ax.set_ylabel('Y', fontsize = 15)
ax.tick_params(labelsize = 10)
ax.ticklabel_format(style = 'plain')
plt.style.use('seaborn-v0_8-pastel')

# for s in plt.style.available:
#     print(s)

plt.savefig('colorbar.png')
plt.show()
