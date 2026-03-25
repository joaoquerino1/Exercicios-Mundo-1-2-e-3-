soma = 0
cont = 0

for c in range(3, 501, 6):
    if c % 3 == 0:
        cont += 1
        soma += c
    print("A soma de todos os {} valores é de {}".format(soma, cont))
    