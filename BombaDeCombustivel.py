
class Bomba_main:
    def __init__(self, TipoCombustivel, Valor_Do_Litro, Quantidade_De_Combustivel):
        self.TipoCombustivel = TipoCombustivel
        self.Valor_Do_Litro = Valor_Do_Litro
        self.Quantidade_De_Combustivel = Quantidade_De_Combustivel


    #Método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
    def Abastecer_Por_Valor(self):
        Valor_A_Ser_Abastecido = int(input("Valor A Ser Abastecido: "))
        Quantidade_De_Litros =  Valor_A_Ser_Abastecido / self.Valor_Do_Litro
        self.Quantidade_De_Combustivel -= Quantidade_De_Litros
        print(f"\nFoi Abastecido: {Quantidade_De_Litros:.2f}L")


    #Método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
    def Abastecer_Por_Litro(self):
        Quantidade_De_Litros = float(input("Quantidade De Litros: "))
        Valor_A_ser_pago = Quantidade_De_Litros * self.Valor_Do_Litro
        self.Quantidade_De_Combustivel -= Quantidade_De_Litros
        print(f"\nValor Pago: R${Valor_A_ser_pago}")


    #Altera o valor do litro do combustível.
    def Alterar_Valor(self):
        self.Valor_Do_Litro = float(input("\nNovo Valor Do Litro: "))


    #Altera o tipo do combustível.
    def Alterar_Combustivel(self):
        self.TipoCombustivel = str(input("\nQual Tipo De Combustivel: "))


    #Altera a quantidade de combustível restante na bomba.
    def Alterar_Quantidade_De_Combustivel(self):
        NovaQuantidade = float(input("Quantidade De Combustivel: "))
        self.Quantidade_De_Combustivel
        Diferença = self.Quantidade_De_Combustivel - NovaQuantidade
        self.Quantidade_De_Combustivel = NovaQuantidade
        print(f"\nForam Adicionados {Diferença:.2f}L De Combustivel")


    #Retonar Os Valores Atuais
    def Printar(self):
        print(f"\nTipo De Combustivel: {self.TipoCombustivel}")
        print(f"Valor Do Litro: R${self.Valor_Do_Litro}")
        print(f"Quantidade De Combustivel Na Bomba: {self.Quantidade_De_Combustivel:.2f}L\n")


def Resultado():
    Bomba_main1 = Bomba_main('Gasolina', 4.25, 100)

    while True:
        Bomba_main1.Printar()
        Opção = int(input("1) Abastecer Por Valor\n2) Abastecer Por Litro\n3) Alterar Valor do Litro\n4) Tipo De Combustivel\n5) Quantidade De Combustivel\n6) Sair\n >"))
        
        if Opção == 1:
            Bomba_main1.Abastecer_Por_Valor()
        elif Opção == 2:
            Bomba_main1.Abastecer_Por_Litro()
        elif Opção == 3:
            Bomba_main1.Alterar_Valor()
        elif Opção == 4:
            Bomba_main1.Alterar_Combustivel()
        elif Opção == 5:
            Bomba_main1.Alterar_Quantidade_De_Combustivel()
        elif Opção == 6:
            print("Obrigado Por Usar! Tenha Uma Boa Vida!")
            break


Resultado()
