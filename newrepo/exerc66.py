def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print("ERRO! Digite um numero inteiro valido.")
        if ok:
            break
    return valor
num = leiaInt("Digite um numero: ")
print(f"Voce acabou de digitar o numero {num}")