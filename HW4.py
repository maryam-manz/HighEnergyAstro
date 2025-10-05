import numpy as np
import matplotlib.pyplot as plt

nu=1.0
R0=2.0
# M_ring=1.0

R = np.linspace(0.1, 10.0, 200) #Because the PDE has 1/R terms. 𝑅=0 would cause a divide-by-zero singularity
dR = R[1] - R[0]

sigma = 0.1   #small sigma
Sigma = np.exp(- (R - R0)**2 / (2*sigma**2))


M_ring = 2 * np.pi * np.sum(Sigma * R * dR)
Sigma *= 1.0 / M_ring  # normalize so total = 1

plt.plot(R, Sigma)
plt.xlabel("Radius R")
plt.ylabel("Surface density Σ(R, 0)")
plt.title("Initial Gaussian ring")
plt.show()


