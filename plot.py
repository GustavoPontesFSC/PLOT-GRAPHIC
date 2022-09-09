import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv('data.dat',sep = ' ', skiprows = 0, header = 1).to_numpy()


df = pd.DataFrame()

df['x'] = file[:,1]
df['y'] = file[:,2]
df['Energy'] = file[:,3]

# print(df.head())

matrix = df.to_numpy()

x = matrix[:,0]
y = matrix[:,1]
z = matrix[:,2]

mask = z>0

fig, axes = plt.subplots(3,1)
fig.set_size_inches((1280,780))

axes[0].plot(x[~mask], y[~mask], label = 'x|y' ,color = 'red')
axes[1].plot(x[~mask], z[~mask], label = 'x|Energy', color = 'red')
axes[2].plot(y[~mask], z[~mask], '*', label = 'y|Energy', color = 'red')

axes[0].set_xlabel('x')
axes[1].set_xlabel('x')
axes[2].set_xlabel('y')
axes[0].set_ylabel('y')
axes[1].set_ylabel('Energy')
axes[2].set_ylabel('Energy')

axes[0].plot(x[mask], y[mask], label = 'x|y' ,color = 'green')
axes[1].plot(x[mask], z[mask], label = 'x|Energy', color = 'green')
axes[2].plot(y[mask], z[mask], '*' ,label = 'y|Energy', color = 'green')

plt.show()

print(x)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
fig.set_size_inches((1280,780))

ax.plot(x[~mask], y[~mask], z[~mask] ,antialiased=False, label = 'Energy = 0')
ax.plot(x[mask],y[mask], z[mask], label ='Energy > 0' )
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Energy')

plt.legend()

plt.show()
