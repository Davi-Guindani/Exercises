lista = []
dados = ["nome", "roe", "pl"]
for i in range(0, 3):
    lista.append(input(dados[i]))

if lista[1] > 20 and lista[2] > 20:
    print("ambos altos")

if lista[1] > 20 and lista[2] < 5:
    print("roe alto")

if lista[1] < 5 and lista[2] > 20:
    print("roe baixo")
