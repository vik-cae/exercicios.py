class Funcionario:
    def __init__(self,nome,sobrenome,hrTrabalhadas,valorHora, incrementarHrs):
        self.nome = nome
        self.sobrenome = sobrenome
        self.hr = hrTrabalhadas
        self.valor = valorHora
        self.incrementar = incrementarHrs

    def getNome(self):
        return(f"\nfuncionario: {self.nome}")

    def getSobrenome(self):
        return(f"\nSobrenome: {self.sobrenome}")

    def getHR(self):
        return(f"\nHoras Trabalhadas: {self.hr}")
    
    def getValor(self):
        return(f"\nValor por Horas: {self.valor}")
    
    def getIncrementar(self):
        return(f"\nhoras extras: {self.incrementar}")

    def getnomeCompleto(self):
        return(f"\nnome completo: {self.nome} {self.sobrenome}")
    
    def getcalcularSalario(self):
        salarioMes =  (self.hr) * (self.valor)
        return (f"\nsalario: {salarioMes}")
    
    def getcalculoHrs(self):
        salarioMes =  (self.hr) * (self.valor)
        cal = self.valor + self.incrementar
        total = salarioMes + cal
        return(f"\nvalor das horas extras: {cal}\n\nsalario total: {total} ")
    
p1 = Funcionario("vitoria","caetano faria da silva",100,12.00,10)
print (p1.getNome())
print (p1.getSobrenome())
print (p1.getValor())
print (p1.getHR())
print (p1.getnomeCompleto())
print (p1.getcalcularSalario())
print (p1.getcalculoHrs())