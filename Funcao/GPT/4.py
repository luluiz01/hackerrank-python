numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
maior = numeros[0]
menor = numeros[0]

for i in numeros:
    if i > maior:
        maior = i
    else:
        menor = i

print(f"O Maior número é: {maior}")
print(f"O Menor número é: {menor}")
