value = int(input('Qual o primeiro numero?'))
value2 = int(input('Qual o segundo numero?'))
value3 = int(input('Qual o terceiro numero?'))
menor = value #linha para identificar o 'value' como o menor pre estabelecido, e fazendo as condições nas linhas subsequentes
if value2<value and value2<value3:
    menor = value2
if value3<value and value3<value2:
    menor = value3
maior = value #linha para identificar o 'value' com o maior pre estabelecido, e fazendo as condições nas linhas subsequentes
if value2>value and value2>value3:
    maior = value2
if value3>value and value3>value2:
    maior = value3
    print('O maior valor é {}'.format(maior))
    print('O menor valor é {}'.format(menor))
    
    