class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
        self.ligado = False

    def apresentar(self):
        print(f"Carro: {self.modelo} ({self.ano})")

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"O carro {self.modelo} ligou")
        else:
            raise RuntimeError("O carro já está ligado")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"O carro {self.modelo} desligou")
        else:
            raise RuntimeError("O carro já está desligado")

    def acelerar(self, valor):
        if not self.ligado:
            raise RuntimeError("Não é possível acelerar um carro desligado")

        if valor <= 0:
            raise ValueError("A velocidade deve ser maior que zero")

        self.velocidade += valor
        print(f"Acelerou {valor} km/h")
        print(f"Velocidade atual: {self.velocidade} km/h")

    def estado(self):
        estado = "ligado" if self.ligado else "desligado"
        print(f"O carro está {estado} a {self.velocidade} km/h")


# Criano objetos
carro1 = Carro("Palio", 1997)

# carro3 = Carro()

print("*" * 50)

# Chamando métodos
carro1.ligar()
carro1.acelerar(100)
carro1.estado()
carro1.desligar()
carro1.estado()

