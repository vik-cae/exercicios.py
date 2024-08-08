class Aluno:
    def __init__(self,nome,ra,n1,n2,n3,n4):
        self.nome = nome
        self.ra = ra
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        
    def getNome(self):
        return(f"nome: {self.nome}")

    def getRa(self):
        return(f"matricula: {self.ra}")

    def setNotas(self):
        cal = ((self.n1+self.n2+self.n3+self.n4)/4)

        if cal>=7:
            return ("aprovado, parabens por fazer sua obrigação")
        
        elif cal >=5 and cal <=6.9:
            return("exame")
        
        else:
            return("reprovado!!!")
            
aluno1 = Aluno("manoel", 2022203633,9,7,10,5)
print(aluno1.setNotas())

