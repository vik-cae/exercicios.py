class Cliente:
    def __init__(self,nome,idade,endereco):
        self.nome = nome
        self.idade = idade
        self.ende = endereco

    def getNome(self):
        return(f"cliente: {self.nome}")

    def setIdade(self, alterarIdade):
        return(f"idade: {alterarIdade}")

    def getEndeco(self):
        return(f"idade: {self.ende}")


p1 = Cliente("vitoria",18,"rua")
print(p1.getNome())
print(p1.setIdade("19"))
print(p1.getEndeco())