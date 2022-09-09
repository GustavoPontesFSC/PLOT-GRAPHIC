import os
import pandas as pd

file = pd.read_csv('data.dat',sep = ' ', skiprows = 1, header = None).to_numpy()


df = pd.DataFrame()

df['x'] = file[:,1]
df['y'] = file[:,2]
df['Energy'] = file[:,3]

df.to_csv('matrix_x_y_energy.dat')
