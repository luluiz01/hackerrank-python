"""Exercício 2

 2. Faça um jogo onde o computador gera um número aleatório e o usuário tenta adivinhar
o Dê dicas se o número é maior ou menor
o Limite o número de tentativas
o Avise o número de tentativas que o usuário ainda tem
"""

import random

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)
tentativas = 0
limite_tentativas = 5

while True:
    if tentativas >= limite_tentativas:
        print(f"Você excedeu o número máximo de tentativas. O número era {numero_aleatorio}."        )
        break
    else:
        tentativa = int(input("Escolha um número entre 1 e 10: "))
        if tentativa == numero_aleatorio:
            tentativas += 1
            break
        elif tentativa < numero_aleatorio:
            print("Muito baixo. Tente um número maior. ")
        else:
            print("Muito alto. Tente um número menor. ")
        tentativas += 1
        
print(f"Parabéns! Você acertou em {tentativas} tentativa. ")

""" if numero_aleatorio == tentativa:
    print("Parabéns! Você acertou!")
else:
    print("Tente novamente!") """

""" 

print("Jogo de Adivinhação")
while True:
    tentativa = int(input("Escolha um número entre 1 e 10: "))
    tentativas += 1

    if tentativa == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas. ")
        break
    elif tentativa < numero_secreto:
        print("Muito baixo. Tente novamente. ")
    else:
        print("Muito alto. Tente novamente. ") """
