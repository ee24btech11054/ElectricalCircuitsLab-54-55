import numpy as np
import matplotlib.pyplot as plt
V1=np.linspace(-5,5,6000)
V2=(25-V1**2)**0.5
V3=-V2

#create a plot
plt.figure(figsize=(12,12))
plt.plot(V1,V2,label='$V_1 v/s V_2$',color='blue')
plt.plot(V1,V3, color='blue')
#label the axes
plt.xlabel('$V_1$ (V)', fontsize=8)
plt.ylabel('$V_2$ (V)', fontsize=8)
plt.title('Phase-space plot of $V_1$ v/s $V_2$', fontsize=14)
plt.legend()

#grid
plt.grid(True)
plt.axis('equal')

plt.savefig("../figs/2/pplot.png")
