def media_lista(numeros):
    if not numeros:
        return 0

    return sum(numeros) / len(numeros)


notas = [10, 20]
print(f"A média das notas é: {media_lista(notas)}")
