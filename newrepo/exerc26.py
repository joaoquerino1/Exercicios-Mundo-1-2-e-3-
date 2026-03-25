from datetime import date
maioridd = 0
menoridd =  0
atual  =  date.today().year
for c in range(1, 8):
    anonasc = int(input('Qual ano você nasceu? '))
    idade = atual - anonasc
    if idade >= 18: #Se a  IDADE for MAIOR IGUAL a 18, ele adiciona 1 à  variavel maioridd.
        maioridd += 1 
    else:           #Se não: adiociona 1 à variavel menoridd.
        menoridd += 1
print('Ao todo tivemos {} maiores e {} menores.'.format(maioridd, menoridd)) #Aqui, trás as variaveis adicionadas e formata elas.