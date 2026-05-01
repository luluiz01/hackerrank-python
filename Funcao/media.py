def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media

notas_aluno = [6, 8, 6.5, 9.0]
media_aluno = calcular_media(notas_aluno)
print(f"A média do aluno é: {media_aluno:.2f}")

