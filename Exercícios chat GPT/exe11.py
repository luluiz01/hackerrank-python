""" Criar uma lista de números e fazer  a média entre eles """

numeros = [1, 2, 3, 4, 5, 158,78]

soma = 0

for i in numeros:
    soma += i

print(f"A soma é: {soma}")

media = soma / len(numeros)

print("Média:", media)