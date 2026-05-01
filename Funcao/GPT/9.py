"""9️⃣ Lista de dicionários (nível intermediário)
produtos = [
    {"nome": "camisa", "preco": 50},
    {"nome": "calça", "preco": 120},
    {"nome": "tenis", "preco": 200}
]

👉 Crie uma função que:

retorna apenas produtos com preço > 100"""

produtos = [
    {"nome": "camisa", "preco": 50},
    {"nome": "calça", "preco": 120},
    {"nome": "tenis", "preco": 200},
]


def filtrar_produtos(produtos):
    nova_lista = []

    for produto in produtos:
        if produto["preco"] > 100:
            nova_lista.append(produto)

    return nova_lista


resutado = filtrar_produtos(produtos)

print(resutado)
