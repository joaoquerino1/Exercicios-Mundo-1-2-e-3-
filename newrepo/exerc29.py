num = 1
par = impar = 0
while num != 10:
    num = int(input('Digite um numero '))
    if num != 10:
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
print('Voce digitou {} numeros pares e {} numeros  impares.'.format(par, impar))
