soma = cont = num = 0
while True:
    num = int(input("Digite uns numeros ai: "))
    if num == 999:
        break
    cont += 1
    soma += num
print(f"A soma dos seus valores é de {soma}, e foram digitados {cont} numeros.")