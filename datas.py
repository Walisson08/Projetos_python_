class Data:
    def __init__(self, dia, mes, ano):
        print("Construindo objeto ...{}".format(self))
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print("{:02d}/{:02d}/{}".format(self.dia, self.mes, self.ano))

