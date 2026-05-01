a, b, c = map(int, input().split(" "))

lista = [a, b, c]
ordenado = sorted(lista)

for i in ordenado:
    print(i)

print("")

# imprime a segunda parte
for i in lista:
    print(f"{i}")
