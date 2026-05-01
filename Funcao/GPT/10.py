"""🔟 Desafio final 🔥 (nível entrevista)
numeros = [1, 2, 3, 4, 5, 6]

👉 Crie uma função que:

filtra os números pares
dobra os valores
retorna a lista final

Resultado esperado:

[4, 8, 12]"""
def filtro_pares(numeros):
    numeros_pares = []
    for pares in numeros:
        if pares % 2 == 0:
            numeros_pares.append(pares * 2)
    return numeros_pares


numeros = [1, 2, 3, 4, 5, 6]

print(f"O resultado esperado é: {filtro_pares(numeros)}")
