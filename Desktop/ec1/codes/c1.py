import numpy as np
import matplotlib.pyplot as plt

V1 = np.linspace(-(2)**0.5, 2**0.5, 1000)

V2 = V1

# Create the plot
plt.figure(figsize=(8, 8))
plt.plot(V1, V2, label='$V_1$ vs $V_2$', color='blue')
# Label the axes
plt.xlabel('$V_1$ (V)', fontsize=8)
plt.ylabel('$V_2$ (V)', fontsize=8)

# Add a title and legend
plt.title('Phase-Space Plot of $V_1$ vs $V_2$', fontsize=14)
plt.legend()

# Show the grid
plt.grid(True)

# Display the plot
plt.savefig("../figs/1/pyplot.png")
