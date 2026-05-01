dinheiro = float(input())
centavos = int(round(dinheiro * 100))
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]


print("NOTAS:")

for i in notas:
    quantidade = dinheiro // i
    print(f"{quantidade:.0f} nota(s) de R$ {i:.2f}")
    dinheiro %= i

print("MOEDAS:")

for moeda in moedas:
    quantidade = dinheiro // moeda
    print(f"{quantidade:.0f} moeda(s) de R$ {moeda:.2f}")
    dinheiro %= moeda
