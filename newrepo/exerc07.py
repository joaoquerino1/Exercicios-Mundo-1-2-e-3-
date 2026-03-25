casa = float(input('Qual o valor da casa?'))
salario = float(input('Qual o seu salario?'))
anos = int(input('Em quantos anos voce vai pagar?'))

parcela = casa / (anos * 12)
minimo = salario * 30 / 100

print ('Para pagar uma casa no valor de R${:.2f}, em {} anos, o valor da parcela será R${:.2f}, e o minimo é de {}'.format(casa, anos, parcela, minimo))

if parcela <= minimo:
    print('Seu empréstimo foi CONCEDIDO! Parabéns!')
    
else:
    print ('Seu empréstimo foi negado.')
    