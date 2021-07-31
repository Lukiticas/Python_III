class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo em...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_branco = "001"
    
    def extrato(self):
        print("Saldo atual de R${} na conta {} do titular {}".format(self.__saldo, self.__numero, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor
        print("adicionado R${} na conta de {}, saldo atual: R${}".format(valor, self.__titular, self.__saldo))


    def __pode_sacar(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor <= valor_disponivel
    
    def saque(self, valor):
        if self.__pode_sacar(valor): 
            self.__saldo -= valor 
            print("Sacado R${} da conta, saldo atual: R${}".format(valor, self.__saldo))
        else: 
            print("O valor {} passou do limite".format(valor))

    def transfere(self, destinatário, valor):
        self.saque(valor)
        destinatário.deposita(valor)
        print("transferido!")
    
    def con_saldo(self):
        return self.__saldo
    
    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular
    
    @property
    def codigo_banco(self):
        return self.__codigo_branco

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite




conta = Conta(123, "Lucas", 300, 1000)
conta1 = Conta(321, "Ni", 100, 1000)

conta.saque(1400)
