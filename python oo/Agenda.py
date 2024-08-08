class Agenda:
    def __init__(self,dia,mes,ano,anotacao):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = anotacao
    
    def getDia(self):
        return(f"dia: {self.dia}")
    
    def getMes (self):
        return(f"mes: {self.mes}")
    
    def getAno(self):
        return(f"ano: {self.ano}")
    
    def getAnotacao(self):
        return(f"anotação: {self.anotacao}")
p1 = Agenda(9,11,2024,"aniversario")
print(p1.getDia())
print(p1.getMes())
print(p1.getAno())
print(p1.getAnotacao())