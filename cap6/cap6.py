import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# PLOT SIMPLES
x = np.array([1,2,3,4])
# broadcasting
y = x*2
y2 = x**2
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
# PLOT
plt.plot(x, y, 'o--g',
         x, y2, 'x:b',
         linewidth=1.5, markersize=5)
plt.show()

# SUBPLOTS
x = np.array([1,2,3,4])
# broadcasting
y = x*2
y2 = x**2
# SUBPLOT
plt.subplot(1, 2, 1)
plt.plot(x, y, 'o-r')
plt.title('Linear')

# SUBPLOT 2
plt.subplot(1, 2, 2)
plt.plot(x, y2, 'o--g')
plt.title('Exponecial')

plt.show()

# SCATTER PLOT
df = pd.read_csv('cap6/paises.csv', delimiter=';')
# print(df.columns)
df2 = df.nlargest(6, 'Area (sq. mi.)')
plt.scatter(x=df2['Country'], y=df2['Area (sq. mi.)'],
            s=df2['GDP ($ per capita)']/50)
plt.show()