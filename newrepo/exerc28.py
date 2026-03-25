soma_idades = 0 #SEMPRE IMPORTANTE!!! ---- Valores que vão somar, ou vão virar numeros maiores, sempre definir eles antes de loopar ou iterar.
mediaidade = 0
maioridadehomem = 0
nomemaisvelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(' ------- {}a PESSOA -------'.format(p))
    
    nome = input('Nome? ').strip()
    idade = int(input('Idade? '))
    sexo = input('Sexo? [F, M]').strip()
    soma_idades += idade
    if p == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 =+ 1
mediaidade = soma_idades / 4
print('A média de idade deles é de {:.1f} anos'.format(mediaidade))
print('O nome do mais velho é {} e tem {} anos'.format(nomemaisvelho, maioridadehomem))
print('Ao todos são {} mulheres com menos de 20 anos.'.format(totmulher20))
