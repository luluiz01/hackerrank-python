def maior_menor(lista):
    
    maior = max(lista)
    menor = min(lista)
    return maior, menor


numeros = [10, 5, 20, 3, 8]

maior, menor = maior_menor(numeros)

print(f"Maior: {maior}")
print(f"Menor: {menor}")
