def fatorial(num=1):
    f = 1
    for contador in range(num, 0, -1):
        f *= contador
    return f
    
    
f1 = fatorial(5)
f2 = fatorial(20)
f3 = fatorial(7)
print(f"Os resultados são {f1}, {f2} e {f3} ")