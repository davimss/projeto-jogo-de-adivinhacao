'''
5. Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional,
com valor default zero e os demais atributos são obrigatórios.
'''

class Conta_Corrente:
    def __init__(self, conta, nome, saldo=0):
        self.conta = conta
        self.nome = nome
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome = novo_nome
        return self.nome
    
    def deposito(self, saldo_deposito):
        self.saldo += saldo_deposito
        return self.saldo

    def saque(self, saldo_saque):
        self.saldo -= saldo_saque
        return self.saldo
 