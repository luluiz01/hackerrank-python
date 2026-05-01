produtos = [
    {"nome": "camisa", "preco": 50},
    {"nome": "calça", "preco": 120},
    {"nome": "tenis", "preco": 200},
]

""" print(produtos[0]["preco"])
print(produtos[0]["nome"])

print(produtos[1]["preco"])
print(produtos[1]["nome"])
 """

for produto in produtos:
    print(f"O produto {produto["nome"]} custa {produto["preco"]} reais")
