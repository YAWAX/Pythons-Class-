""" 
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
A classe deve possuir os seguintes atributos:
número da conta, nome do correntista e saldo. 

Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, 
com valor default zero e os demais atributos são obrigatórios. 

"""


class ContaCorrente:
    def __init__(self, numero_da_conta, nome_do_correntista, saldo=0):
        self.numero_da_conta = numero_da_conta
        self.nome_do_correntista = nome_do_correntista
        self.saldo = saldo
        
    
    def AlterarNome(self):
        NovoNome = str(input("Qual O Novo Nome Do corretista?\n > "))
        self.nome_do_correntista = NovoNome
        print("Ok O Nome foi alterado para ",NovoNome)
    

    def Deposito(self):
        Deposito = float(input("Qual o Valor Do Deposito?\n > "))
        self.saldo = Deposito
    
    
    def Saque(self):
        Saque = float(input("Qual O Valor Do Saque?\n > "))
        
        if Saque > self.saldo:
            print("Valor Na Conta Insuficiente! ")
        
        else:
            self.saldo -= Saque


    def Printar(self):
        print(f"\n=Numero Da Conta: {self.numero_da_conta}=")
        print(f"=Nome Do Correntista: {self.nome_do_correntista}=")
        print(f"=Saldo Atual: {self.saldo}=\n")


def ContaMain():
    MainConta = ContaCorrente(12345, 'Pedro Silva')
    while True:
        MainConta.Printar()
        Opção = int(input("""1) Alterar Nome\n2) Deposito\n3) Saque\n4) Sair\n>>>>>> """))
        if Opção == 1:
            MainConta.AlterarNome()
        elif Opção == 2:
            MainConta.Deposito()
        elif Opção == 3:
            MainConta.Saque()
        elif Opção == 4:
            print("Obrigado Por Usar! Tenha Uma Boa Vida!")
            break


ContaMain()
