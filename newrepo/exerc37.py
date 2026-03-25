soma = cont = média = maior = menor = 0
resposta = "S"
while resposta in "Ss":
    n = int(input("Digite um numero: "))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resposta = str(input("Quer continuar?: [S,N] ").upper().strip()[0])
média = soma / cont        
print(f"Voce digitou {cont} numeros e a media foi {média:.2f}")
print(f"O maior valor foi de {maior} e o menor {menor}")
print("FIM!")