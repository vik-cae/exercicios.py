###MODULO PRODUTO
class Produto:
    def __init__ (self,nome,desc,preco,estoque):
        self.nome = nome
        self.descricao = desc
        self.preco = preco
        self.qtde_estoque = estoque
    def getNome(self):
        print(f"produto: {self.nome}")
    def getEstoque(self):
        print(f"quantidade estoque{self.qtde_estoque}")
        
p1 = Produto("cll",)       
