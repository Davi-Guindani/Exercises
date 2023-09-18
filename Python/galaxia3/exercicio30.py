import numpy as np

lista = []

for i in range(0, 3):
    lista.append(input("digite a cotação: "))

vet = np.array(lista)

print(vet)
