empresa = {"nome": str, "pl": int, "roe": float}
lista = []
while input("Deja entrar com uma nova empresa? s/n: ") == "s":
    for i in empresa:
        empresa[i] = input(i + " ")
    lista.append(empresa)

print(empresa)
