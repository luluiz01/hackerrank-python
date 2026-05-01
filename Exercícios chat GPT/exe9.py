numeros = [-2, 5, -1, 8, -3, 10]

positivos = []
negativos = []

for i in numeros:
    if i > 0:
        positivos.append(i)
    else:
        negativos.append(i)

print(positivos)
print(negativos)