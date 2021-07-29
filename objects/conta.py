class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo em...{}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def extrato(self):
        print("Saldo atual de R${} na conta {} do titular {}".format(self.saldo, self.numero, self.titular))

    def deposita(self, valor):
        self.saldo += valor
        print("adicionado R${} na conta de {}, saldo atual: R${}".format(valor, self.titular, self.saldo))
    
    def saque(self, valor):
        self.saldo -= valor 
        print("Sacado R${} da conta, saldo atual: R${}".format(valor, self.saldo))


conta = Conta(123, "Lucas", 100, 1000)

conta.extrato()
conta.deposita(200)
conta.deposita(300)
conta.saque(200)
conta.extrato()
