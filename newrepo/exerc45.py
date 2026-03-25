#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

tabela = ("Palmeiras", "São Paulo", "Corinthians", "Bahia", "Fluminense", "Athletico-PR", "Bragantino", "Gremio", "Chapecoense", "Mirassol", "Flamengo", "Coritiba", "Santos", "Botafogo", "Vitoria", "Remo", "Atletico-MG", "Internacional", "Cruzeiro", "Vasco")

print(f"Os cinco primeiros times são: {tabela[0:5]}")
print(f"Os ultimos quatro colocados são: {tabela[-4:]}")
print(f"Em ordem alfabética: {sorted(tabela)}")
print(f"A Chapecoense está na {tabela.index("Chapecoense")+1} posição")