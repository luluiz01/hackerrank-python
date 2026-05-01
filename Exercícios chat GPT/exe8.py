""" 8️⃣ Lista com entrada do usuário

Peça ao usuário para digitar 5 números e armazene em uma lista.

Depois:

mostre a lista

mostre o maior número """

numeros = []

for i in range(5):
    n = int(input("Digite um número: "))
    numeros.append(n)

print(numeros)

maior = 0
menor = 0
for n in numeros:
    if n > maior:
        maior = n
    if i < menor:
        menor = i

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")