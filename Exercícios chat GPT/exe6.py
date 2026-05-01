""" 6️⃣ Contar números pares
Crie uma lista com números de 1 a 10.
Conte quantos números são pares. """

numeros = list(range(1, 10))

print(numeros)
numeros_impares = 0
numeros_pares = 0

for i in numeros:
    if i % 2 == 0:
        numeros_impares += 1
    else:
        numeros_pares += 1

print(f"A quantidade de números impares é: {numeros_impares}")
print(f"A quantidade de números pares é: {numeros_pares}")
    







""" numero = 0

if numero % 2 == 0:
    print("O numero é par")
else:
    print("O numero é imapar")


 """