from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print("-="*30)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}.")
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f"{cont}",end=' ', flush=True)
            sleep(0.5)
            cont += passo       
        print("FIM!")
    else:
        cont = inicio
        while cont >= fim:
            print(f"{cont}",end=' ', flush=True)
            sleep(0.5)
            cont -= passo
        print("Fim!")
contador(1, 10, 1)
contador(78, 5, 6)
print("Agora é sua vez de testar a função:")
ini = int(input("Inicio: "))
fi = int(input("Fim: "))
pas = int(input("Passo:"))
contador(ini, fi, pas)