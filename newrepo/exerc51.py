num = [[],[]]
for i in range (1, 8):
    valor = int(input("Digite um numero: "))
    if valor % 2 == 0:
        num[0].append(valor)
    elif valor % 2 == 1:
        num[1].append(valor)
        
print(f"Os valores da lista são: {num}")
num[0].sort()
num[1].sort()
print(f"Você tem os numeros {num[0]} pares.")
print(f"Voce tem os numeros {num[1]} impares.")