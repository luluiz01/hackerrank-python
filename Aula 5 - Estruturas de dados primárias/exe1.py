""" Crie uma lista de números e realize as seguintes operações:
        Adicione dois novos números
        Remova um número específico
        Ordene a lista """

numeros = [18, 7, 3, 33, 666, 1000]

print(f"Lista original: {numeros}")

numeros.append(2000)
numeros.append(5000)

print(f"Lista com números adicionados: {numeros}")

numeros.remove(numeros[4]) # ou numeros.remove(666)

print(f"Lista com número da besta removido: {numeros}")

numeros.sort()
print(f"Lista com número ordenados: {numeros}")