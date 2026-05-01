import math

# Funções matemáticas
print("Raiz quadrada de 16:", math.sqrt(16))
print("Valor de PI:", math.pi)
print("Cosseno de 0:", math.cos(0))
print("Logaritmo de 10:", math.log(10))

# Arredondamentos e funções trigonométricas
print("Arredondamento para cima de 4.3:", math.ceil(4.3))
print("Arredondamento para baixo de 4.7:", math.floor(4.7))


import random

# Números aleatórios
print("Numero aleatório entre 0 e 1:", random.random())
print("Inteiro aleatório entre 1 e 10:", random.randint(1, 10))

if random.random() > 0.5:
    print("Cara")
else:
    print("Coroa")

# Seleção aleatória
frutas = ["maçã", "banana", "laranja", "uva", "Pera", "Goiaba"]
print("Fruta aleatória:", random.choice(frutas))


# Embaralhar lista
random.shuffle(frutas)
print("Lista embaralhada:", frutas)


deck_cartas = [carta for carta in range(1, 11)]
deck_cartas.append("J")
deck_cartas.append("Q")
deck_cartas.append("K")

random.shuffle(deck_cartas)
print(deck_cartas)
