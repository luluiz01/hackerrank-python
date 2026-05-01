"""2. Use a biblioteca os para:

o Criar uma nova pasta
o Listar o conteúdo da pasta atual
· Imprimir o caminho absoluto da pasta
"""

# Biblioteca os: interação com o sistema operacional
import os

# Informações do sistema
print("Diretório atual:", os.getcwd())  # cwd = current working
print("Listando arquivos do diretório:", os.listdir())


# Criando e removendo diretórios
try:
    os.mkdir("exemplo_pasta")
    print("Pasta criada com sucesso ")
except FileExistsError:
    print("Pasta já existe")

# Informações de caminho
caminho = os.path.join("exemplo_pasta", "arquivo.py")
print("Caminho completo:", caminho)
