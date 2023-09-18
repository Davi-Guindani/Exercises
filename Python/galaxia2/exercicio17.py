import re

numero = input("numero de telefone ")
padrao = r"[1-9]{2}+9[0-9]{8}"
regExp = re.compile(padrao)
if re.fullmatch(regExp, numero):
    print("Numero valido")
else:
    print("Invalido")
