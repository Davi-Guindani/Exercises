import numpy as np

cmd = ""
lista = []
while cmd.title() != "N":
    lista.append(float(input("Digite uma cotação: ")))
    cmd = input("deseja continuar?[S/N] ")
    while cmd.title() != "N" and cmd.title() != "S":
        cmd = input("digite um comando válido [S/N] ")

vet = np.array(lista)

print("{:.0%}".format(np.mean(vet)))
print("{:.0%}".format(np.median(vet)))
print("{:.0%}".format(np.std(vet)))
print("{:.0%}".format(vet.max()))
print("{:.0%}".format(vet.min()))