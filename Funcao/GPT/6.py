"""6️⃣ Filtrar nomes grandes (filter)
nomes = ["Ana", "Luiz", "João", "Li"]

👉 Crie uma função que retorna nomes com mais de 3 letras"""

nomes = ["Ana", "Luiz", "João", "Li"]

novosnomes = list(filter(lambda x: len(x) > 3, nomes))

print(novosnomes)
