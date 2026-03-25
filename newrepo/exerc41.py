from random import randint
vitorias  = 0
while True:
    jgd = int(input("Digita um numero: "))
    pc = randint(1, 11)
    total = jgd + pc
    tipo = " "
    while tipo not in "PI": 
            tipo = str(input("Par ou Impar?[P,I] ").upper().strip()[0])
    print(f"Voce jogou {jgd} e o computador {pc}, total deu {total} ", end= "")
    print("Deu par!" if total % 2 == 0 else "Deu impar!")
    if tipo == "P":
        if total % 2 == 0:   
                print ("Voce venceu!")
                vitorias += 1
        else:
            print("Voce perdeu!")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print ("Voce venceu!")
            vitorias += 1
        else:
            print("Voce perdeu!")
            break
    print("Vamos jogar novamente!")
print(f"Game Over! Você ganhou {vitorias} vezes")