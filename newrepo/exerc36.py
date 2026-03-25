n = cont = total = 0
n = int(input("Digite um número: [999 pra sair] "))
while n != 999:
    total += n
    cont += 1
    n = int(input("Digite um número: [999 pra sair] "))
print(f"Voce digitou {cont} numeros e a soma deles é de {total}")
    