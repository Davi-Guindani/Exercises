lista = []
while input("continuar? s/n: ") == "s":
    lista.append(int(input("cotação: ")))

for i in range(1, len(lista)):
    print(f"retorno dia {i}: " + str(lista[i] / lista[i - 1]))
