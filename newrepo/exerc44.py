lista = ("zero", "um" , "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
for opção in lista:
    opção = int(input("Escolha um número de 0 a 20: "))
    if opção in range(0,21):
        print(lista[opção])
        break
    else:
        print("Numero invalido. Tente novamente.")
    