dinheiro = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]

for i in notas:
    quantidade = dinheiro // i
    print(f"{quantidade} nota(s) de R$ {i},00")
    dinheiro = dinheiro % i
