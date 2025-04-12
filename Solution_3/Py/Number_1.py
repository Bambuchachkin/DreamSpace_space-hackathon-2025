import numpy as np
import matplotlib.pyplot as plt

SIZE = 3000
MAX = 512
MIN = 0

picture_Gaus = np.loadtxt('Gaussian_Noise.txt')
picture_Koshi = np.loadtxt('Cauchy_Noise.txt')
picture_Laplas = np.loadtxt('Laplace_Noise.txt')
picture_Cloud = np.loadtxt('Cloud_Map.txt')

Map_1 = (picture_Gaus+picture_Koshi+picture_Laplas)/3+picture_Cloud
plt.imshow(Map_1, cmap='gray', vmin=MIN, vmax=MAX)
plt.imsave('Map_1.png', Map_1, cmap='gray', vmin=MIN, vmax=MAX)
np.savetxt('Laplace_Map_1Noise.txt', Map_1, fmt='%.0f')
plt.show()

print("Yep!")