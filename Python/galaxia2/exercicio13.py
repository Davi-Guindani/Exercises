carteira1 = []
for i in range(0, 3):
    carteira1.append(input("primeira carteira: "))

carteira2 = []
for i in range(0, 3):
    carteira2.append(input("segunda carteira: "))

carteira1 = set(carteira1)
carteira2 = set(carteira2)

print(carteira1 | carteira2)
print(carteira1 & carteira2)
print(carteira1 - carteira2)
