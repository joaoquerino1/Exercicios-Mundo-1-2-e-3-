from datetime import date
ano = int(input('Qual seu ano de nascimento?: '))
atual = date.today().year
idade = atual - ano
print('O atleta tem {} anos.'.format(idade))
#MASTER-SENIOR-JUNIOR-INFANTIL-MIRIM
#--25+--->25--->19------->14---->9---
if idade <= 9:
    print('Sua categoria é MIRIM.')
    
elif idade <= 14:
    print('Sua categoria é INFANTIL.')
    
elif idade <= 19:
    print('Sua categoria é JUNIOR.')
    
elif idade <= 25:
    print('Sua categoria é SÊNIOR.')
    
else:
    print('Sua categoria é MASTER.')