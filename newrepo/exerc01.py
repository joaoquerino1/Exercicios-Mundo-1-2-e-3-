v = float(input('Qual é a velocidade atual do seu carro?'))
if v > 80:
    print ('VOCÊ ESTÁ RAPIDO DEMAIS! VOCE FOI MULTADO! O LIMITE É DE 80Km/h!')
    multa = (v-80) * 7
    print ('Voce vai pagar uma multa de R${:.2f}'.format(multa))
else:
    print ('Voce está dentro da normalidade. Muito bem cidadão, é isso ai!')
    