class AlunoAcaemia:
    def __init__(self, nome,idade,peso,altura,men=120):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.men = men

    def getNome(self):
        return(f"nome: {self.nome}")
    
    def getIdade(self):
        return(f"idade: {self.idade}")
    
    def getPeso(self):
        return(f"peso: {self.peso}")
    
    def getAltura(self):
        return(f"alturo: {self.altura}")
    
    def getMen(self):
        return(f"mensalidade: {self.men}")
    
    def getCalIMC(self):
        cal = self.peso/(self.altura**2)
        return(f"IMC: {cal}")
    
    def getValorMensalidade(self):
        
        if self.idade >= 18:
            print("O VALOR DA MENSALIDADE É: R$ 120,00")

        else:
            print("MENOR DE IDADE PAGAM: R$ 60,00")

p1 = AlunoAcaemia("vitoria caetano",18, 70,1.69)
print(p1.getNome())
print(p1.getIdade())
print(p1.getPeso())
print(p1.getAltura())
print(p1.getMen())
print(p1.getCalIMC())
print(p1.getValorMensalidade())