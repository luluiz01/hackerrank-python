"""3. Crie uma lista de compras e use um laço para:

o Imprimir cada item
o Calcular o total de itens
o Verificar se algum item específico está na lista"""

print("*" * 30)
lista_de_compras = [
    "leite",
    "pão",
    "ovos",
    "tomate",
    "cenoura",
    "frango",
    "arroz",
    "feijão",
]
preco = [3.50, 4.00, 12.00, 2.50, 1.80, 15.00, 8.00, 6.00]

for item, valor in zip(lista_de_compras, preco):
    print(f"Item: {item}, Preço: R${valor:.2f}")

for index, item in enumerate(lista_de_compras, start=1):
    print(f"Item {item}: {index}")


print("*" * 30)
print(f"Total de itens: {len(lista_de_compras)}")
print("*" * 30)


item_busca = (
    input("Digite o item que deseja buscar na lista de compras: ").strip().lower()
)

if item_busca in lista_de_compras:
    print(f"{item_busca} está na lista!")
else:
    print(f"{item_busca} não está na lista.")
