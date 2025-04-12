import numpy as np
import matplotlib.pyplot as plt

SIZE = 3000
MAX = 512
MIN = 0

mean = 256 # Среднее значение (сигнал до 10 раз сильнее)
std_dev = 50 # Стандартное отклонение

# Создание шума по Гауссу
Gaussian_Noise = np.random.normal(mean, std_dev, (SIZE,SIZE))

plt.imshow(Gaussian_Noise, cmap='gray', vmin=MIN, vmax=MAX)
plt.imsave('Gaussian_Noise.png', Gaussian_Noise, cmap='gray', vmin=MIN, vmax=MAX)
np.savetxt('Gaussian_Noise.txt', Gaussian_Noise, fmt='%.0f')
plt.show()

print("Yep!")