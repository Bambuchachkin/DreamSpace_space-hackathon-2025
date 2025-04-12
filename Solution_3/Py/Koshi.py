import numpy as np
import matplotlib.pyplot as plt

SIZE = 3000
MAX = 512
MIN = 0

loc = 256 # Параметр положения (аналог среднего)
scale = 50 # Параметр масштаба (аналог стандартного отклонения)

# Создание шума по Коши
Cauchy_Noise = np.random.standard_cauchy((SIZE,SIZE)) * scale + loc

plt.imshow(Cauchy_Noise, cmap='gray', vmin=MIN, vmax=MAX)
plt.imsave('Cauchy_Noise.png', Cauchy_Noise, cmap='gray', vmin=MIN, vmax=MAX)
np.savetxt('Cauchy_Noise.txt', Cauchy_Noise, fmt='%.0f')
plt.show()

print("Yep!")