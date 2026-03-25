maior = 0 #Coloca as variaveis no mesmo valor para, no loop (laço), fazer a condição e conferir se a resposta inputada, é  maior ou menor que o valor. 
menor = 0

for p in range(1, 6):
    peso = float(input('Qual o peso da {} pessoa?'.format(p)))
    if p == 1: # Iniciando o loop, qualquer que seja o valor dito, ele vira o maior e o menor peso ao mesmo tempo.
        maior = p
        menor = p
    else:
        if peso > maior: #Se o valor dito for maior que a primeira occorência, ele vira o novo numero maior.
            maior = peso
        if  peso < menor:#Se o valor dito for menor que a primeira ocorrencia, ele vira o novo numero menor.
            menor = peso
print('O maior peso lido foi {}kg'.format(maior))
print('O menor peso foi {}kg'.format(menor))
