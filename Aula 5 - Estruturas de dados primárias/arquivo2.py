idade = int(input("Digite sua idade: "))
nome = input("Digite seu nome: ")

def saudacao_com_nome(nome: str, idade: int):  # : str espera uma string como argumento, mas não é obrigatório
    return f"Olá, {nome}! você tem {idade} anos. "  

print(saudacao_com_nome(nome, idade))