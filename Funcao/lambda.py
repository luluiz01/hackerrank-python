# Função lambda simples
quadrado = lambda x: x**2
print("Quadrado de 5:", quadrado(5))


def quadrado_do_numero(x):
    return x**2


print("Quadrado de 5:", quadrado_do_numero(6))

somatorio = lambda a, b: a + b
print(f"Soma de 3 e 4:", somatorio(3, 4))

subtracao = lambda a, b: a - b
print(f"A subtração de 10 e 5 é: {subtracao(10, 5)}")

dobro = lambda x: x*2
print(f"O dobro de 10 é: {dobro(10)}") 
# Na função oculta, primeiro vc declara o nome da função como uma váriavé, depis coloca lamba, o argumento : o que vc quer q a função faça
