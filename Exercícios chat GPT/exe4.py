""" Crie uma lista com números:

numeros = [5, 8, 2, 15, 3]

Encontre o maior número sem usar max(). """

numeros = [5, 8, 2, 15, 3]

maior = numeros[0]
menor = numeros[0]

for i in numeros:
    if i > maior:
        maior = i
    if i < menor:
        menor = i
print(f"O maior numero é o: {maior}")
print(f"O menor numero é o: {menor}")