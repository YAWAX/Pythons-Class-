"""Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
O consumo é especificado no construtor e o nível de combustível inicial é 0."""

class Carro():
    def __init__(self, ConsumoDeCombustivel, QuantidadeDeombustivelNoTanque=0):
        self.ConsumoDeCombustivel = int(ConsumoDeCombustivel)
        self.QuantidadeDeombustivelNoTanque = QuantidadeDeombustivelNoTanque


    #que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina
    def andar(self, kmAndado):
        ConsumoDeCombustivel1 = int(self.ConsumoDeCombustivel * kmAndado)
        self.QuantidadeDeombustivelNoTanque -= ConsumoDeCombustivel1
    

    #Para abastecer o tanque
    def Adicionar(self, Quantidade):
        self.QuantidadeDeombustivelNoTanque += Quantidade


    #retorna o nível atual de combustível
    def ObterGasolina(self):
        print(f"Sobrou {self.QuantidadeDeombustivelNoTanque}L")


MainCarro = Carro(7)
MainCarro.Adicionar(14)
MainCarro.andar(1)
MainCarro.ObterGasolina()
