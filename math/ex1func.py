import random


def media_aleatorio():
    numeros = []
    for i in range(10):
        numeros.append(random.randint(1, 10))

    return {
        "numeros": numeros,
        "maior": max(numeros),
        "menor": min(numeros),
        "media": sum(numeros) / len(numeros),
    }


print(media_aleatorio())
