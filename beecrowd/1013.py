"""a, b, c = map(int, input().split(" "))
maior = a

maior_a_b = (a + b + abs(a - b)) / 2
if maior_a_b > maior:
    maior = maior_a_b

maior_a_c = (a + c + abs(a - c)) / 2
if maior_a_c > maior:
    maior = maior_a_c

maior_b_c = (b + c + abs(b - c)) / 2
if maior_b_c > maior:
    maior = maior_b_c

print(f"{int(maior)} eh o maior")
"""

numeros = list(map(int, input().split(" ")))
print(f"{(max(numeros))} eh o maior")
