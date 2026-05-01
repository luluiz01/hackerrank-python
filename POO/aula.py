# Definindo uma classe simples
class Pessoa:  # class Pessoa ()
    def init(self, nome, idade):
        # Atributos da classe
        # # self = um objeto comum à nossa classe | um objeto acessível por todos os métodos
        self.nome = nome
        self.idade = idade


# Método (função de uma classe) para apresentação
def apresentar(self):
    print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos. ")


# Criando objetos
peqsoal = Pessoa("João", 25)
pessoa2 = Pessoa("Maria", 30)
# pessoa3 = Pessoa ()
