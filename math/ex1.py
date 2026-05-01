"""Exercícios Propostos

1. Crie um programa que:

o Gere 10 números aleatórios
o Encontre o maior e o menor número
· Calcule a média desses números
"""

import random

numeros = []

for i in range(10):
    numeros.append(random.randint(1, 500))

print(numeros)
print(sorted(numeros)) #imprimir números na

maior = numeros[0]
menor = numeros[0]

""" 
for i in numeros:
    if i > maior:
        maior = i
    if i < menor:
        menor = i

print(f"O maior numero é {maior}")
print(f"O menor numero é {menor}") """

print("********" * 10)

print(f"O maior numero é {max(numeros)}")
print(f"O menor numero é {min(numeros)}")


media = sum(numeros) / len(numeros)

print(f"A soma é: {sum(numeros)}")
print(f"A média é: {media}")
