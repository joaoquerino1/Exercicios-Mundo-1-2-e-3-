viagem = float(input('Quanto é a distancia da sua viagem em Km?'))
print('Sua viagem será de {:.1f}Km.'.format(viagem))
if viagem <= 200:
    preço = viagem * 0.50
    print('O preço da sua passagem é de R${:.2f}'.format(preço))
else:
    preço = viagem * 0.45
    print('O preço de sua passagem é de R${:.2f}'.format(preço))
    