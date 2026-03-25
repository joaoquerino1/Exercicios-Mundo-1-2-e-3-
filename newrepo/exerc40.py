while True:
# pede um número inteiro
    n = int(input("Digite um número para ver a tabuada: "))
    if n < 0:
        break
    # inicializa o multiplicador
    for cont in range(1, 11):
        print(f"{n} x {cont} = {n * cont}")
print("FIM!")