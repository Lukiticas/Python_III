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


conta = Conta(123, "Lucas", 100, 1000)

conta.extrato()
conta.deposita(200)
conta.deposita(300)
conta.saque(200)
conta.extrato()
