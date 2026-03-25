from random import randint
def maior(): # definir a função "maior"
    nums = [randint(0,10) for _ in range(randint(1, 10))]#nums recebe uma lista aleatória de numeros de 0 a 10, na quantidade do range aleatorio de 1 a 10
    print("Números gerados:", nums) #printa a lista aleatoria
    print(f"Foram informados {len(nums)} números.")
    if nums:
        m = max(nums)
        print(f"O maior número foi: {m}")
        #retorna o maior(max) da lista(nums) se tiver numeros inteiros, se não tiver valor explicito, retorna None "NADA"
        return m
    else:
        return None
print("-="*40)
print(maior())
print("-="*40)
print(maior())
print("-="*40)
print(maior())
print("-="*40)