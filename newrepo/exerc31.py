from random import randint
pc = randint(0, 10)
acertou = False
palpites = 0
print(""""Sou o PC
Pensei num numero entre 0 e 10, adivinha ai.""")
while not acertou:
    jogador = int(input("Qual sua jogada?: "))
    palpites += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print("Um pouquinho mais...")
        if jogador > pc:
            print("Um pouquinho menos")
print(f"Você precisou de {palpites} tentivas kkkkkkkkkkkk")
