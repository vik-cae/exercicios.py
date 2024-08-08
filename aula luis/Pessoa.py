class Pessoa:
    def __init__(self,matricula,nome,idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade


class Aluno(Pessoa):
    def __init__(self,matricula,nome,idade,notas,media):
        super().__init__(matricula,nome,idade)
        self.notas = notas
        self.media = media

    def setnotasaluno(self):
        quant = int(input("digite a quantidade de provas:"))
        i = 0
        pv=0
        while i<quant:
            pv += int(input("digite a nota:"))
            i +=1
        
        cal = pv / quant
        return (f"a media é: {cal}")
    
class Professor(Pessoa):
    def __init__(self,matricula,nome,idade,disciplina,carga_horaria,salario):
        super().__init__(matricula,nome,idade)
        self.disciplinas = disciplina
        self.carga = carga_horaria
        self.salario = salario

p1 = Aluno(1234,"vi",18,5)
print(p1.notasaluno(3))