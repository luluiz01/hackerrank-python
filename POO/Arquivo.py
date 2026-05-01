"""Exercícios Propostos

1. Crie uma classe Carro com atributos como modelo, ano e métodos para:

o Ligar o carro
o Desligar o carro
o Acelerar
o Velocidade atual
o Estado do carro (ligado ou desligado)"""


class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
        self.ligado = False

        # Método (função de uma classe) para apresentação

    def apresentar_o_carro(self):
        print(f"Olá, o nome do carro é {self.modelo} e o ano é {self.ano}. ")

    def ligar_o_carro(self):
        if self.ligado == False:
            self.ligado = True
            print(f"O carro {self.modelo} ligou")
        else:
            raise Exception("Você não pode ligar um carro que já está ligado")

    def desligar_o_carro(self):
        if self.ligado == True:
            self.ligado = False
            print(f"O carro {self.modelo} desligou")
        else:
            raise Exception("Você não pode desligar um carro que já está desligado")

    def acelerar(self, velocidade=0):
        if self.ligado == True:
            if velocidade > 0:
                self.velocidade += velocidade
                print(f"O carro acelerou {velocidade} km/h")
            else:
                print("Não foi possível acelerar")
        else:
            raise Exception("Não é possível acelerar um carro desligado")

        print(f"A velocidade atual do carro é {self.velocidade} km/h")

    # def estado_atual_do_carro()


# Criano objetos
carro1 = Carro("Palio", 1997)

# carro3 = Carro()

print("*" * 50)

# Chamando métodos
carro1.ligar_o_carro()
carro1.acelerar(50)
print("*" * 50)
carro1.acelerar(50)
carro1.acelerar()
carro1.ligar_o_carro()