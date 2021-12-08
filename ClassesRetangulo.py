"""
Classe Retangulo: Crie uma classe que modele um retangulo:
Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;

Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local. """


class Retangulo():
    def __init__(self, Base=0, Altura=0):
        self.Base = Base
        self.Altura = Altura


    #Mudança De Valores 
    def MudarValores(self):
        NovoValorBase = int(input("Novo Valor: Base: "))
        NovoValorAltura = int(input("Novo Valor Para Altura: "))
        self.Base = NovoValorBase
        self.Altura = NovoValorAltura
        print("Os Novos Valores Foram Definidos!")


    #Retorna Os Valores, padrão e definifos pelo usuario
    def RetornarValores(self):
        print(f"Base: {self.Base}Cm²")
        print(f"Altura: {self.Altura}Cm²")


    #Calcula a Area sobre a formula A = b x h 
    def Calcular_Area(self):    
        Area = self.Base * self.Altura
        print(f"A Area Do Retangulo é: {Area} Cm²")
        return Area


    #Calcula O Perimetro sobre a Formula P = b + h 
    def CalcularPerimetro(self):
        Perimetro = 2 * (self.Base + self.Altura)
        print(f"O perimetro Do Retangulo é {Perimetro}")


def Menu():
    MainRetangulo = Retangulo()

    while True:
        Opção = int(input("""1) Mudar Valores\n2) Retornar Valores Atuais\n3) Retornar Áreas\n4) Retornar Perimetro\n5) Sair\n>>>>>> """))
        if Opção == 1:
            MainRetangulo.MudarValores()
        elif Opção == 2:
            MainRetangulo.RetornarValores()
        elif Opção == 3:
            MainRetangulo.Calcular_Area()
        elif Opção == 4:
            MainRetangulo.CalcularPerimetro()
        elif Opção == 5:
            print("Obrigado Por Usar! Tenha Uma Boa Vida!")
            break

Menu()
