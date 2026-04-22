resto = 0
dinheiro = int(input())


print(dinheiro)
print(f"{dinheiro//100} nota(s) de R$ 100,00")
resto = dinheiro % 100

print(f"{resto//50} nota(s) de R$ 50,00")
resto = resto % 50

print(f"{resto//20} nota(s) de R$ 20,00")
resto = resto % 20

print(f"{resto//10} nota(s) de R$ 10,00")
resto = resto % 10

print(f"{resto//5} nota(s) de R$ 5,00")
resto = resto % 5

print(f"{resto//2} nota(s) de R$ 2,00")
resto = resto % 2

print(f"{resto//1} nota(s) de R$ 1,00")
resto = resto % 1