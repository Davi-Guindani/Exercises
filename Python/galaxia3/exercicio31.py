import numpy as np

lista = []

for i in range(0, 2):
    lista.append(input(": "))

print(np.arange(int(lista[0]), int(lista[1]), 2, dtype=int))
