import math

a, b, c = map(float, input().split(" "))

delta = (math.pow(b, 2)) - 4 * a * c

if delta > 0 and a > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")
else:
    print("Impossivel calcular")
