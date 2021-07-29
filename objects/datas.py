class data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print(f"{self.dia:02d}/{self.mes:02d}/{self.ano}")

d = data(5,11,2003)
d.formatada()