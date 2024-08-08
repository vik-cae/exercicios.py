class Livro:
    def __init__(self,nome,autor,editora,paginas):
        self.nome = nome
        self.autor = autor
        self.edi = editora
        self.pag = paginas

    def getNome(self):
        return(f"nome: {self.nome}")

    def getAutor(self):
        return(f"autor: {self.autor}")

    def setEdi(self,novaEditora):
        return(f"editora: {novaEditora}")

    def getPag(self):
        return(f"paginas: {self.pag}")


p1 = Livro("É assim que acaba","Colleen Hoover","Editora Galera",368)
print(p1.getNome())
print(p1.getAutor())
print(p1.setEdi("Grupo Editorial Record"))
print(p1.getPag())
