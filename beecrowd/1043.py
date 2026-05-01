a, b, c = map(float, input("").split(" "))

if (a + b) > c and (a + c) > b and (b + c) > a:
    Perimetro = a + b + c
    print(f"Perimetro = {Perimetro}")
else:
    Area = ((a + b) * c) / 2
    print(f"Area = {Area}")
