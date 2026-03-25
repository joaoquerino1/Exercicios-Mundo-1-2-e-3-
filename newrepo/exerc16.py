peso = float(input('Qual seu peso? (kg) '))
altura = float(input('Qual sua altura? (m) '))
imc = peso / (altura ** altura)

print('Seu IMC é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Voce está ABAIXO do peso.')
elif 18.5 <= imc < 25:
        print ('Voce esta no PESO IDEAL.')
elif 25 <= imc < 30:
        print ('Voce esta com SOBREPESO.')
elif 30 <= imc < 40:
        print('Voce  esta IMENSO!')
else:
    print ('Voce esta na faixa da OBESIDADE MORBIDA')