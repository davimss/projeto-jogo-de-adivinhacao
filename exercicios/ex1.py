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
 