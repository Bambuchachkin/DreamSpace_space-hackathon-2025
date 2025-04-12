# Поиск диаметра кружка Эйри, который соответствует размеру вулкана на матрице
from random import randint
import numpy as np
import matplotlib.pyplot as plt

MAX = 512
MIN = 0
Volcano_Value = 512 # Число, отвечающее за яркость вулкана

T = 1273 # Температура лавы в К
b = 2.898e-3 # Постоянная Вина
Lambda = b / T # Длина волны соответствует инфракрасному излучению вулкана
f = 32e-3 # Фокусное расстояние линзы
D = 4e-3 # Диаметр линзы
d = 2.44 * Lambda * f / D # Диаметр Эйри для кругового отверстия
d_pixel = 5e-6 # Размер пикселя в метрах
Volcano_pixels = round(d/d_pixel) # Размер вулкана в пикселях
# print(d,Volcano_pixels)

print("Lambda =", Lambda) # = 2.27e-6 м, что соответствует ближнему ИК диапазону < 3e-3 м
# d = 10e-6
print("d =", d)

# Создание массива с координатами вулканов
Volcano_x = np.array([], dtype=int)
Volcano_y = np.array([], dtype=int)
for i in range(13):
    Volcano_x = np.append(Volcano_x, randint(500,2500))
    Volcano_y = np.append(Volcano_y, randint(500,2500))

Map = np.zeros((3000, 3000), dtype=int)
for i in range(len(Volcano_x)):
    x, y = int(Volcano_x[i]), int(Volcano_y[i])
    # Заполняем квадрат вокруг вулкана
    for dx in range(-Volcano_pixels//2, Volcano_pixels//2 + 1):
        for dy in range(-Volcano_pixels//2, Volcano_pixels//2 + 1):
            nx, ny = x + dx, y + dy
            Map[nx, ny] = Volcano_Value


file = open("d.txt", "w", encoding="utf-8")
file.write(str(d))
file.close()

np.savetxt("Volcano_Clear_Map.txt", Map, fmt='%.0f')
# plt.imshow(Map, cmap='hot')
plt.imshow(Map, cmap="gray", vmin=MIN, vmax=MAX)
plt.imsave('Volcano_Clear_Map.png', Map, cmap='gray', vmin=MIN, vmax=MAX)
plt.show()


print("Yep!")