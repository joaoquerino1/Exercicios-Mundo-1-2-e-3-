from datetime import date
atual = date.today().year
nasc = int(input('Qual ano voce nasceu?'))
anos = (atual - nasc)
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, anos, atual))

if anos < 18:
    saldo = 18 - anos
    ano = atual + saldo
    print('Ainda faltam {} anos para seu alistamento'.format(saldo))
    print('Voce deve se apresentar no ano de {}'.format(ano))
elif anos == 18:
    print('Voce deve se alistar ainda esse ano.')    
else:
    saldo = anos - 18
    ano2 = atual  - saldo
    print('Seu alistamento foi a {} anos atrás.'.format(saldo))
    print('Voce deveria ter se alistado em {}'.format(ano2))