"""1. Crie uma função que calcule o IMC (Índice de Massa Corporal)
o Receba peso e altura como parâmetros
o Retorne a classificação do IMC"""


def calculo_imc(peso, altura):
    # Se a altura vier em centímetros, converte para metros
    if altura > 10:
        altura = altura / 100

    imc = peso / (altura * altura)

    if imc < 18.5:
        categoria = "Abaixo do peso"
    elif imc < 25:
        categoria = "Peso normal"
    elif imc < 30:
        categoria = "Sobrepeso"
    elif imc < 35:
        categoria = "Obesidade grau I"
    elif imc < 40:
        categoria = "Obesidade grau II"
    else:
        categoria = "Obesidade grau III"

    return imc, categoria


resultado = calculo_imc(70, 175)
print(f"IMC: {resultado[0]:.2f}, Classificação: {resultado[1]}")
