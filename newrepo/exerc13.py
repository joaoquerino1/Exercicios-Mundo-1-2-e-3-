nota1 = float(input('Qual a sua primeira nota?'))
nota2 = float(input('Qual a sua segunda nota?'))
media = (nota1 + nota2)  / 2

print('A sua primeira nota é {:.1f} e a segunda {:.1f}, a média é {:.1f}'.format(nota1, nota2, media))

if media >= 5.0 and media < 7:
    print('Voce esta de recuperação')
    
elif media < 5.0:
    print('Voce foi reprovado.')
    
else:
    print('Voce foi aprovado.')