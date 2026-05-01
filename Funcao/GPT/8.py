"""Usando zip
nomes = ["Ana", "Bruno"]
idades = [20, 25]

👉 Crie uma função que retorna:

["Ana tem 20 anos", "Bruno tem 25 anos"]"""

""" nomes = ["Ana", "Bruno", "Tigo"]
idades = [20, 25, 5]

for i, v in zip(nomes, idades):
    print(f"{i} tem {v} anos") """


def retorno_dados(nomes, idades):
    dados = []
    for i, v in zip(nomes, idades):
        dados.append(f"{i} tem {v} anos")
    return dados


nomes = ["Ana", "Bruno", "Tigo"]
idades = [20, 25, 5]

print(retorno_dados(nomes, idades))
