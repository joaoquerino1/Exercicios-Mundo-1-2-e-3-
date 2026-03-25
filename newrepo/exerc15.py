v1 = float(input('Primeiro segmento: '))
v2 = float(input('Segundo segmento: '))
v3 = float(input('Terceiro segmento: '))

if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v1 + v2:
    print('Os segmentos PODEM FORMAR um triângulo ', end='')
    if v1 == v2 == v3:
        print('Equilatero!')    
    elif v1 != v2 != v3 != v1:
            print('Escaleno!')
    else:
            print('Isosceles!')
else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo.')
    