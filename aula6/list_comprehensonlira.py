lista_precos = [500, 1500, 2000, 100, 25]

""" # Caso 1
nova_lista_precos = []

for preco in lista_precos:
    nova_lista_precos.append(preco * 2)
 """

""" · Caso 2: Todos os produtos que custarem acima de 1.000 dolares, imposto de 50% sobre o valor total """
print(f"lista de preços {lista_precos}")
imposto = []
for preco in lista_precos:
    if preco > 1000:
        imposto.append(preco * 0.5)
print(f"lista com imposto {imposto}")


novalista_preco = [preco * 0.5 for preco in lista_precos if preco > 1000]
print(f"nova lista de preços {novalista_preco}")