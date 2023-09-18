import numpy as np

dias = int(input("numero de dias: "))

retorno = np.random.uniform(-1, 1, dias)

print(retorno[retorno > 0])
print(retorno[0])
print(retorno[-1])
