#def respostadouser(resp):
#resp = str(input("Quer continuar?[S,N] ")).upper().strip()[0]
#if resp in "S":
#True
#elif resp in "N":
#break
grupotemp = []
principal = []
while True:
    grupotemp.append(str(input("Nome? ")))
    grupotemp.append(float(input("Peso? "))).upper().strip()[0]
    if len(principal) == 0:
         mai = men = grupotemp[1]
    else:
        if grupotemp[1] > mai:
            mai = grupotemp[1]
        if grupotemp[1] < men:
            men = grupotemp[1]
    principal.append(grupotemp[:])
    grupotemp.clear
    resp = str(input("Voce quer continuar? [S,N]")).upper().strip()[0]
    if resp not in "SN":
        print("Tente novamente. Digito errado.")
        resp = str(input("Quer continuar?[S,N] ")).upper().strip()[0]
        if resp == "N":
            print("Laço finalizado.")
            break
    
print(f"O grupo tem {len(principal)} pessoas cadastradas.")
print("O maior peso foi de {mai:.2f}kg. Peso de: ", end="")
for pessoa in principal:
    if pessoa[1] == mai:
        print(f"{pessoa[0]}", end="")
print("E o menor peso foi de {men:.2f}kg.", end='')
for pessoa in principal:
    if pessoa[1] == men:
        print(f"{pessoa[0]}", end='')