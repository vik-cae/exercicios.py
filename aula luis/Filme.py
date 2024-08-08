class Filme:
    def __init__(self,nome,duracao):
        self.nome = nome
        self.duracao = duracao
    
    def getFilme(self):
        return(f"foi dado play no filme {self.nome}")
    
class Açao(Filme):
    def __init__(self,nome,duracao,personagem):
        super().__init__(nome,duracao)
        self.personagem = personagem

    def personagem(self):
        return(f"{self.personagem}")
    
    def explodir(self):
        return("explodir")
    
class Drama(Filme):
    def __init__(self,nome,duracao,producao):
        super().__init__(nome,duracao)
        self.producao = producao

    def mortecachorro(self):
        return("buaaa")
    
class Suspense(Filme):
    def __init__(self,nome,duracao,vilao):
        super().__init__(nome,duracao)
        self.vilao = vilao
        
    def assustar(self):
        return("buuuuu!!")

filme = Açao("Duro de matar","2h","Bruce Willis")
print(filme.explodir())
drama = Drama("assim que acaba","2h10","Collen")
print(drama.mortecachorro())
suspense = Suspense("A ilha do medo", "2h18","leonardo DiCaprio")
print(suspense.assustar())





    