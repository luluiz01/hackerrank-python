"""🔥 Desafio (pra você treinar)

Crie um dicionário de um produto:

nome
preço
quantidade

Depois:

Atualize o preço
Adicione categoria
Remova quantidade
Mostre o resultado final"""

produto = {
    'nome': "PS5",
    "preco": 5000,
    "quantidade": 25,
}
print(produto)

#Atualizar preço (Desconto de 15%)
produto['preco'] = 4000

print(produto)

#Adicionar categoria
produto['publico'] = 'adulto'

print(produto)

#remover quantidade
produto.pop('quantidade')
print(produto)

