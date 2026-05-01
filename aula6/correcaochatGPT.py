import random

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # depois você pode remover isso

tentativas = 0
limite_tentativas = 5
acertou = False

while True:
    if tentativas >= limite_tentativas:
        print(f"Você excedeu o número máximo de tentativas. O número era {numero_aleatorio}.")
        break

    try:
        tentativa = int(input("Escolha um número entre 1 e 10: "))
    except ValueError:
        print("Digite um número válido!")
        continue

    tentativas += 1

    if tentativa == numero_aleatorio:
        acertou = True
        break
    elif tentativa < numero_aleatorio:
        print("Muito baixo. Tente um número maior.")
    else:
        print("Muito alto. Tente um número menor.")

# Resultado final
if acertou:
    if tentativas == 1:
        print(f"Parabéns! Você acertou em {tentativas} tentativa.")
    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")