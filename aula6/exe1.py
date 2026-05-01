""" Exercícios Propostos

1. Crie um programa que:
o Peça a idade do usuário
o Classifique em categorias (criança, adolescente, adulto, idoso)


3. Crie uma lista de compras e use um laço para:

o Imprimir cada item
o Calcular o total de itens
o Verificar se algum item específico está na lista """

idade = int(input("Qual sua idade: "))

if idade < 5:
    print("Bebe")
elif idade < 12:
    print("Você é uma criança.")
elif idade < 18:
    print("Você é um adolescente.")
elif idade < 60:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")
