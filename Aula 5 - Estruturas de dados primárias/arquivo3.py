# Parâmetros padrão
def calculadora(a, b, operacao="soma"):
    if operacao == "soma":
        return a + b
    elif operacao == "subtracao":
        return a - b
    elif operacao == "multiplicacao":
        return a * b
    else:
        return "Operação inválida"


print("Soma??????????:", calculadora(5, 3))  # calculadora(5, 3, "soma")
print("*" * 20)
print("Subtração:", calculadora(5, 3, "subtracao"))
print("Multiplicação:", calculadora(5, 3, "multiplicacao"))

print("*" * 20)


# Argumentos por palavra-chave
def informacoes_pessoa(nome, idade, curso="Não informado"):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Curso: {curso}")


informacoes_pessoa(nome="João", idade=25)  # curso =?
print("*" * 20)
informacoes_pessoa(nome="Maria", idade=22, curso="Computação")
print("*" * 20)
informacoes_pessoa(idade=29, nome="Luiz", curso="Engenharia")
print("*" * 20)


# Número variável de argumentos
def soma_multiplos(*args,):  # *args = recebe um número variável de argumentos, e os armazena em uma tupla chamada args
    return sum(args)


print("Soma de múltiplos números:", soma_multiplos(1, 2, 3, 4, 5))
