"""2. Desenvolva uma calculadora que receba inúmeros valores com funções para:

o Soma
o Subtração
o Multiplicação
o Divisão"""


def calculadora(*args):
    return sum(args)


somatorio = calculadora(1, 2, 3)
print(f"A soma ")