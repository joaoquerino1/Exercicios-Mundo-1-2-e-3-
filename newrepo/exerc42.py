#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
pessoas = homens = mulheres = 0
sexo = "H,M"
opção = " "
while opção != "N":
    print(" = " * 20)
    idade = int(input("Quantos anos voce tem? "))
    sexo =  str(input("Homem ou Mulher? [H,M] ").upper().strip()[0])
    print(" = " * 20)
    opção = str(input("Deseja continuar? [S,N] ").upper().strip()[0])
    if opção == "N":
        break
    if sexo == "H":
        homens += 1
    elif sexo == "M" and idade < 20:
        mulheres +=1
        
    if idade > 18:
        pessoas += 1
    
print(f"{pessoas} pessoas tem mais de 18 anos, {homens} homens no total, e {mulheres} mulher(es) com menos de 20 anos.")
print("FIM!")