"""codigo, quantidade = map(int, input().split())

if codigo == 1:
    total = quantidade * 4.0
elif codigo == 2:
    total = quantidade * 4.5
elif codigo == 3:
    total = quantidade * 5.0
elif codigo == 4:
    total = quantidade * 2.0
elif codigo == 5:
    total = quantidade * 1.5

print(f"Total: R$ {total:.2f}")
"""

precos = {1: 4.0, 2: 4.5, 3: 5.0, 4: 2.0, 5: 1.5}

codigo, quantidade = map(int, input().split())
total = precos[codigo] * quantidade

print(f"Total: R$ {total:.2f}")
