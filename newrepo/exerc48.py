lista = []
resp = ""
while True:
    num=int(input("Digite um valor: "))
    lista.append(num)
    resp = str(input("Quer continuar? [S,N] ")).upper().strip()[0]
    if resp not in "SN":
        print("Digito invalido. Responda apenas SIM ou NÃO.")
    if resp in "N":
        print("Fechando laço e finalizando lista.")
        break
lista.sort(reverse=True)
print(f"Na lista contém {len(lista)} elementos, e os valores da lista em ordem decrescente são {lista}.")
if 5 in lista:
    print("O numero cinco se encontra na lista.")
else:
    print("O numero cinco não se encontra na lista")