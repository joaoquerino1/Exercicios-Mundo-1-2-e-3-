from random import randint
numeros = []

def sorteia():
    #Vai gerar 5 números aleatórios, e colocalos na lista global (numeros)
    for valor in range(5):
        num = randint(0,10)
        numeros.append(num)
        
def somaPar():
    #Calcula a soma dos valores pares na lista "numeros"
    soma = 0
    for valor in numeros:
        if valor % 2 == 0: #Verificação se o valor é par
            soma += valor
    return soma #Retorna a soma, para uso no print 
    
    
# Executa as funções
sorteia()
print(f"Analisando os 5 valores da lista: {numeros}")
print(f"Somando os valores pares de {numeros}, temos {somaPar()}")