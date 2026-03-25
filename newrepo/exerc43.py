total = produtos = menor = cont = 0
barato = " "
while True:
    nome = str(input("Qual o nome do produto? "))
    preço = float(input("Qual o preço? "))
    total += preço
    if preço > 1000:
        produtos += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
 
    resp = ' '
    while resp not in "SN":
        resp = str(input("Quer continuar? [S,N] "))
    if resp == "N":
        break    

print(f"O total  gasto foi de {total:.2f}.")
print(f"Temos {produtos} produtos custando mais de R$1000 reais e {nome} foi o produto mais barato.")
print("FIM!")