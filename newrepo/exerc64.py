# import math (metodo para fazer a conta do fatorial automaticamente)
def fatorial(n, show = False):
    f = 1
    for cont in range(n, 0, -1):
        if show:   
            print(cont, end='')
            if cont > 1:
                print(" X ", end='')
            else:
                print(" = ", end='')
        f *= cont
    return f


print(fatorial(7, False))