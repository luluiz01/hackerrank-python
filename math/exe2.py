"""2. Use a biblioteca os para:

o Criar uma nova pasta
o Listar o conteúdo da pasta atual
· Imprimir o caminho absoluto da pasta"""

# Criando pasta
import os

try:
    os.mkdir("pasta_exercicio")
    print("Pasta criada com sucesso ")
except FileExistsError:
    print("Pasta já existe")


print("Listando arquivos do diretório da pasta que criei:", os.listdir("pasta_exercicio"))

caminho_absoluto = os.path.abspath("pasta_exercicio")
print(f"O caminho absoluto é: {caminho_absoluto}")

print("Diretório atual:", os.getcwd())