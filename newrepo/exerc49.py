num = list()
par = list()
impar = list()
while True:
    num.append(int(input("Digita um numero ai: ")))
    resp = str(input("Deseja continuar? [S,N] ")).upper().strip()[0]
    if resp not in "SN":
        print("Digito Invalido. Tente Novamente.")
    elif resp in "N":
        print("Fechando laço.")
        break
for i, v in enumerate(num):
    if  v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
        
print(f"A lista completa é {num}, numeros pares temos {par} e ímpares temos {impar}.")