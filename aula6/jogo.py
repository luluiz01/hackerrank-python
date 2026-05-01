# Simulação de jogo com while
import random

numero_secreto = random.randint(1, 10)
tentativas = 0

print(numero_secreto)
print("\nJogo de Adivinhação")
while True:    
    tentativa = int(input("Escolha um número entre 1 e 10: "))
    tentativas += 1

    if tentativa == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas. ")
        break
    elif tentativa < numero_secreto:
        print("Muito alto. Tente novamente. ")
