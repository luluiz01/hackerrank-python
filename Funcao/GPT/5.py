"""5️⃣ Dobrar valores (map)

Crie uma função que:

👉 recebe uma lista
👉 retorna todos os valores dobrados usando map"""

""" numeros = [10, 20, 30, 40, 50]

dobro = list(map(lambda x: x * 2, numeros))


print(dobro)


 """


def dobro_da_lista(numeros):
    return numeros * 2


numeros = [10, 20, 30, 40, 50]

dobro = list(map(dobro_da_lista, numeros))

print(dobro)
