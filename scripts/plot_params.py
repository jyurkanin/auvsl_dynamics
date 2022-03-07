import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import axes3d, Axes3D

df = pd.read_csv("../data/params.csv")
#df = df.loc[:400]

#kc,kphi,n0,n1,phi
plt.subplot(1,5,1)
plt.plot(df['kc'])
plt.subplot(1,5,2)
plt.plot(df['kphi'])
plt.subplot(1,5,3)
plt.plot(df['n0'])
plt.subplot(1,5,4)
plt.plot(df['n1'])
plt.subplot(1,5,5)
plt.plot(df['phi'])
plt.show()
