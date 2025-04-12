import numpy as np
import matplotlib.pyplot as plt

SIZE = 3000
MAX = 512
MIN = 0

loc = 256  # Параметр положения (мода распределения)
scale = 50  # Параметр масштаба (чем больше - тем шире распределение)

# Создание шума по Лапласу
Laplace_Noise = np.random.laplace(loc=loc, scale=scale, size=(SIZE,SIZE))

plt.imshow(Laplace_Noise, cmap='gray', vmin=MIN, vmax=MAX)
plt.imsave('Laplace_Noise.png', Laplace_Noise, cmap='gray', vmin=MIN, vmax=MAX)
np.savetxt('Laplace_Noise.txt', Laplace_Noise, fmt='%.0f')
plt.show()

print("Yep!")