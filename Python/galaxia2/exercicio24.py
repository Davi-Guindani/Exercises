try:
    nome = str(input("Nome: ")).title()
    idade = int(input("Idade: "))
except ValueError:
    print("ValueError")
else:
    print("tudo certo")
