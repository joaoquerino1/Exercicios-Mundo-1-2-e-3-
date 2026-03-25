from random import randint
from time import sleep
while True:
    jogos = int(input("Quantos jogos você quer que eu faça? "))
    for cont in range(jogos):
        sortedNumbers = [randint(1, 60) for c in range(5)]
        print(f"Jogo {cont+1}: {sortedNumbers}")
        sleep(1)
    break
print("Te dei essas dicas ai, só não abusa ein")