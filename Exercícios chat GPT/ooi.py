aluno = {
    'Nome': 'Luiz',
    'Sobrenome': 'Henrique',
    'Idade': '29',
    'Peso': 2.5,
    'Sexo': 'Masculino',
    'Vivo': True

}
print(aluno.keys())
print(aluno.values())

print(aluno['Idade']) # comentar por linha ctrl + ; || comentar por bloco alt + shift + a
print(aluno['Idade']) # shift + alt + seta para baixo duplica
for estudante in aluno.values():
    print(estudante)

if aluno['Vivo'] == False: 
    print("O Luiz está vivo")
else:
    print("O Luiz está morto")

