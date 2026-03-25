list = ['F', 'f', 'M', 'm']
sexo = str(input('Qual seu sexo?:[M/F] '))
while sexo not in list:
    sexo = str(input('Sexo invalido. Por favor, informe seu sexo: '))
else:
    print('Sexo {} registrado com sucesso'.format(sexo))