codigo = input("codigo de negociação: ")
if codigo[-1] == "3":
    print("on")
if codigo[-1] == "4":
    print("pn")
if codigo[-2:] == "11":
    print("unit")
