lista_de_compras = ["leite", "pão", "ovos", "tomate", "cenoura", "frango", "arroz", "feijão"]
preco = [3.50, 4.00, 12.00, 2.50, 1.80, 15.00, 8.00, 6.00]
tipo = [1, 1, 1, 0, 0, 1, 0, 0]

for item, valor, tipo in zip(lista_de_compras, preco, tipo):
    print(f"Item: {item}, Preço: R${valor:.2f}, Tipo: {tipo}")


for i, lista_de_compras in enumerate(lista_de_compras, start=1):
    print(f"Item {lista_de_compras}: {i}")


preco_maior_10 = [preco for preco in preco if preco > 10]
print(f"Preços maiores que 10: {preco_maior_10}")