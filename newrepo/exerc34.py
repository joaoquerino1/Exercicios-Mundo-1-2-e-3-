primeiro = int(input("Qual o seu primeiro termo? "))
razão = int(input("E a razão? "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total = mais
    while cont <= 10:
        print(f"{termo} -> ", end= '')
        termo += razão
        cont += 1
    mais = int(input("Quantos termos a mais voce quer?: "))
print(f"A progessão finalizou com {total} termos.")
print("FIM.")