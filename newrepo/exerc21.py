num = int(input('Qual numero voce quer ver a tabuada? '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
    