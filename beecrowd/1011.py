raio = float(input())

volume = lambda x: (4 / 3) * 3.14159 * (raio**3)

print("VOLUME = {}".format(round(volume(raio), 3)))
