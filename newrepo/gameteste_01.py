from random import randint
itens = ("Pedra", "Papel", "Tesoura")
pc = randint(0, 2)
print("""Suas opções:
                [ 0 ] Pedra
                [ 1 ] Papel
                [ 2 ] Tesoura""")
player = int(input("Qual a sua jogada? "))
if player not in range(len(itens)):
    print("JOGADA INVALIDA")
else:
    print("O computador jogou {}".format(itens[pc]))
    print("O Jogador escolheu {}".format(itens[player]))

    if pc == player:
        print("EMPATE!")
    elif pc == 0:
        if player == 1:
            print("Voce ganhou!")
        elif player == 2:
            print("Voce perdeu!")
    elif pc == 1:
        if player == 0:
            print("Voce perdeu!")
        elif player == 2:
            print("Voce ganhou!")
    elif pc == 2:
        if player == 0:
            print("Voce ganhou!")
        elif player == 1:
            print("Voce perdeu!")
