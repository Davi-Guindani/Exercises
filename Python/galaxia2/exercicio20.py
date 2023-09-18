lista = []
for i in range(0, 5):
    lista.append(int(input("cotação: ")))

maior = 0
menor = 99999999
for i in lista:
    if i > maior:
        maior = i
    if i < menor:
        menor = i

print(maior)
print(menor)
