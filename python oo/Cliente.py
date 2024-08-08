class Cliente:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def getNome(self):
        print(f"cliente: {self.nome}")

    def getIdade(self):
        print(f"idade: {self.idade}")