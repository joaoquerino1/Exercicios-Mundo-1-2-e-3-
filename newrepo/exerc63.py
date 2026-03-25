from datetime import date

def voto(ano):
    idade = date.today().year - ano
    if idade > 18 and idade < 65:
        return f"Com {idade} anos, o voto é OBRIGATÓRIO."
    elif idade < 16:
        return f"Com {idade} anos, você NÃO PODE votar."
    elif idade <= 18 > 16:
        return f"Com {idade} anos, o voto é OPCIONAL."
        
ano = int(input("Qual o ano que você nasceu? "))        
voto(ano)