num = int(input('Digite um numero inteiro:'))
print ('''Escolha uma das bases para conversão:
       [ 1 ] conversão para binario
       [ 2 ] conversão para octal
       [ 3 ] conversão para hexadecimal''')
opção = int(input('Sua opção:'))
if opção == 1:
    print ('{} convertido em binario é: {}'.format(num, bin(num)[2:]))
    
elif opção == 2:
    print ('{} convertido em octal é: {}'.format(num, oct(num)[2:]))
    
elif opção == 3:
    print('{} convertido para hexadecimal é: {}'.format(num, hex(num)[2:]))
    
else:
    print('Opção invalida, tente novamente.')
    