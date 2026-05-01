"""
2️⃣ Média de valores

Crie uma função que:

👉 recebe uma lista
👉 retorna a média dos valores

⚠ trate lista vazia"""

""" 
numeros = [1, 2, 3, 4, 5]
soma = 0
media = 0

for i in numeros:
    soma += i
    media = soma / len(numeros)

print(f"A soma é {soma}")
print(f"A média é {media}")
 """


def media_lista(numeros):
    soma = 0
    media = 0
    for i in numeros:
        soma += i
    media = soma / len(numeros)

    return media


notas = [10, 20]
print(f"A média das notas é: {media_lista(notas)}")
