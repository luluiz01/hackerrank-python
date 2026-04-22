import math

x1, y1 = map(float, input().split(" "))
x2, y2 = map(float, input().split(" "))

distance = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

# print(m.sqrt(49))

print(f"{distance:.4f}")
