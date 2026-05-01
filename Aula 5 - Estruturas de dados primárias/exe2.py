""" Crie um dicionário representando um livro (Titulo, autor, ano) e adicione e remova informações. """
livro = {'titulo': 'Harry Potter',
         'autor': 'JK Rowling',
         'ano': 2025}


print(livro)

#Adicionar informação
livro["genero"] = "Ficção"

print(livro)

#Atualizar valor
livro['ano'] = 1996

print(livro)

#remover informação com DEL
del livro['autor']
print(livro)

#remover informação pop
livro.pop("ano")
print(livro)