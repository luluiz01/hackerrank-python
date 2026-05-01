"""1️⃣ Soma de lista

Crie uma função que:

👉 recebe uma lista de números
👉 retorna a soma de todos os elementos"""

""" numeros = [1, 2, 3, 4, 5]
soma = 0

for i in numeros:
    soma += i

print(soma)
 """


def soma_lista(numeros):
    soma = 0
    for i in numeros:
        soma += i

    return soma


numeros = [1, 2, 3, 4, 5]

print(f"A soma da lista é: {soma_lista(numeros)}")
