nomes = ["Luiz", "Ana", "Carlos"]

""" #imprima:
0 - Luiz
1 - Ana
2 - Carlos  """

for i, valor in enumerate(nomes):
    print(f"{i} - {valor}")

print("-" * 50)
# Comeã do 1 agora

for i, valor in enumerate(nomes):
    print(f"{i+1} - {valor}")

print("-" * 50)

for i, nome in enumerate(nomes, start=1):  # Outra forma
    print(i, nome)

print("-" * 50)

# Mostre a posição do número 30.

numeros = [10, 20, 30, 40]
for posicao, numeros in enumerate(numeros):
    if posicao == 30:
        print(posicao)


print("-" * 50)
# Mostrar somente elementos com índice par
numeros = [5, 10, 15, 20, 25]
for i, v in enumerate(numeros):
    if i % 2 == 0:
        print(f"Resultado {v}")

print("-" * 50)


""" 5️⃣ Substituir valores usando índice

Dada:
numeros = [1, 2, 3, 4, 5]
Multiplique cada valor por 2 e atualize a lista. """

numeros = [1, 2, 3, 4, 5]
for i, v in enumerate(numeros):
    print(v * 2)
