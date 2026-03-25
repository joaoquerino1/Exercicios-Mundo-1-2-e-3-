from time import sleep
primeiro_valor = int(input("Primeiro valor? "))
segundo_valor = int(input("Segundo valor "))
opção = 0
while opção != 5:   
    print("""   [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair""")
    opção = int(input("Qual sua opção?: "))
    
    if opção == 1:
        somar = primeiro_valor + segundo_valor
        print(f"A soma de {primeiro_valor} com {segundo_valor} é {somar}")
    elif opção == 2:
        multiplicar = primeiro_valor * segundo_valor
        print(f"{primeiro_valor} quando multiplicado por {segundo_valor} retorna em: {multiplicar}")
    elif opção == 3:
        if primeiro_valor > segundo_valor:
            maior = primeiro_valor
        elif primeiro_valor < segundo_valor:
            maior = segundo_valor
        else:
            print("Não há numeros maiores, pois os dois são iguais.")          
        print(f'Entre {primeiro_valor} e {segundo_valor}, {maior} é o maior número.')
    elif opção == 4:
        print("Informe os  numeros novamente: ")
        primeiro_valor = int(input(f'Qual seu novo numero? '))
        segundo_valor = int(input(f'E o outro?' ))        
    elif opção == 5:
        print("Ok! Estou desligando.")
        sleep(1)
        print("DESLIGANDO...")
        sleep(2)
        print("Desligado.")
