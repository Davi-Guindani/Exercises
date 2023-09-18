import numpy as np

lista = []
lista.append(np.random.randint(0, 60, 1)[0])
while len(lista) < 6:
    mega_sena = np.random.randint(0, 60, 1)
    if mega_sena not in lista:
        lista.append(mega_sena[0])
probabilidade = np.random.randint(1)[0]
