# Usando lambda com funções built-in
print("-" * 100)
numeros = [3, 2, 3, 4, 5]
quadrados = list(map(lambda x: x**2, numeros))
print("Quadrados:", quadrados)

quadrado = []

for i in numeros:
    quadrado.append(i**2)
print("-" * 100)
print(quadrado)


def novo_quadrado(numeros):
    for i in numeros:
        quadrado.append(i**2)
        return quadrado


print("-" * 100)
print(f"Dobro com função tradicional {novo_quadrado(numeros)}")
print("-" * 100)


# Filtrando com lambda
pares = list(filter(lambda X: X % 2 == 0, numeros))

print("Números pares:", pares)

maiorq2 = list(filter(lambda x: x >= 3, numeros))
print(maiorq2)
