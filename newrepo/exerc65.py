def ficha():
    nome = str(input("Qual o seu nome?: "))
    gols = str(input("Quantos gols você fez?: "))
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    if not nome:
        nome = "<Desconhecido>"
    
    return f"O jogador {nome} fez {gols} gol(s) no campeonato."

print(ficha())