class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo em...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print("Saldo atual de R${} na conta {} do titular {}".format(self.__saldo, self.__numero, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor
        print("adicionado R${} na conta de {}, saldo atual: R${}".format(valor, self.__titular, self.__saldo))
    
    def saque(self, valor):
        self.__saldo -= valor 
        print("Sacado R${} da conta, saldo atual: R${}".format(valor, self.__saldo))
    
    def transfere(self, destinatário, valor):
        self.saque(valor)
        destinatário.deposita(valor)
        print("transferido!")



conta = Conta(123, "Lucas", 300, 1000)
conta1 = Conta(321, "Ni", 100, 1000)

conta.transfere(conta1, 200)
