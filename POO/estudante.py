"""2. Implemente uma classe Estudante que:
o Tenha atributos como nome, idade e notas
o Possua um método para calcular a média das notas"""


class Estudante:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def apresentar_estudante(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos. ")

    def calcular_media(self):
        self.media = sum(self.notas) / len(self.notas)

        print(f"A médias das notas é {self.media}")


# Criano objetos
aluno1 = Estudante("Luiz", 29, [0, 1, 2, 3])

aluno1.apresentar_estudante()
aluno1.calcular_media()

