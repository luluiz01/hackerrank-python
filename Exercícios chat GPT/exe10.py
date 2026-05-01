""" Crie uma nova lista sem elementos repetidos.
Resultado esperado: """
numeros = [1, 2, 2, 3, 4, 4, 5]

sem_repetidos = []

for n in numeros:
    if n not in sem_repetidos:
        sem_repetidos.append(n)

print(sem_repetidos)