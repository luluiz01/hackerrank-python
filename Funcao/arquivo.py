nome = input(str("Digite seu nome: "))


def saudacao_com_nome(nome: str,):  # : str espera uma string como argumento, mas não é obrigatório
    print(f"Olá, {nome}! ")


# Chamando a função com um argumento
saudacao_com_nome(nome)


print("*" * 20)


# Função com múltiplos parâmetros
# Função com retorno = return
# Função sem retorno = None
# None = um tipo que não tem valor nenhum
def soma(a, b):
    return a + b

resultado_soma = soma(5, 3)
print(f"Resultado da soma: {resultado_soma}")
# print(f"Resultado da soma: {soma(5, 3)}")

def multiplicacao(a, b):
    return a * b

resultado_multiplicacao = multiplicacao(5, 3)
print(f"Resultado da multiplicação: {resultado_multiplicacao}")

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Não é possível dividir por zero."
resultado_divisao = divisao(10, 5)
print(f"Resultado da divisão: {resultado_divisao}") 


def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
resultado_fatorial = fatorial(5)
print(f"Resultado do fatorial: {resultado_fatorial}")

def subtracao(a, b):
    return a - b
resultado_subtracao = subtracao(10, 5)
print(f"Resultado da subtração: {resultado_subtracao}")