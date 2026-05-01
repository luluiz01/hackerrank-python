def tamanho_maior_que_3(nome):
    return len(nome) > 3


nomes = ["Ana", "Luiz", "João", "Li"]

novosnomes = list(filter(tamanho_maior_que_3, nomes))

print(novosnomes)
