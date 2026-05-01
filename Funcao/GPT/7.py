"""7️⃣ Usando enumerate

Crie uma função que:

nomes = ["Ana", "Bruno", "Carlos"]

👉 retorna:

["1 - Ana", "2 - Bruno", "3 - Carlos"]"""

""" for i, v in enumerate(nomes, start=1):
    print(f"{i} - {v}") """


def novos_nomes(nomes):
    novalista = []
    for i, v in enumerate(nomes, start=1):
        novalista.append(f"{i} - {v}")
        
    return novalista


nomes = ["Ana", "Bruno", "Carlos"]

print(novos_nomes(nomes))
