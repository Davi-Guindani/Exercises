import numpy as np

array_desordenado = np.array([])
for i in range(0, 3):
    array_desordenado = np.append(array_desordenado, int(input("lucro: ")))

array_ordenado = -np.sort(-array_desordenado)

print(array_ordenado)
print(array_ordenado)
