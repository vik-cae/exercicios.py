class Brinquedos:
    def __init__(self,nome,cor,tamanho,preco):
        self.nm = nome
        self.c = cor
        self.tama = tamanho
        self.valor = preco

    def n(self):
        return(f"nome do brinquedo: {self.nm}")
    
    def cores(self):
        return(f"cor do brinquedo: {self.c}")
    
    def tamanhos(self):
        return(f"tamanho do brinquedo: {self.tama}")
    
    def valores(self):
        return(f"preço do brinquedo: {self.valor}")
    
class Peao(Brinquedos):
    def __init__(self,nome,cor,tamanho,preco,girar):
        super().__init__(nome,cor,tamanho,preco)
        self.g = girar

    def rodar(self):
        return("girou!")
    
class Bicicleta(Brinquedos):
    def __init__(self,nome,cor,tamanho,preco,andar):
        super().__init__(nome,cor,tamanho,preco)
        self.a = andar

    def andou(self):
        return("bicicleta andou!")
    
class Patins(Brinquedos):
    def __init__(self,nome,cor,tamanho,preco,danca):
        super().__init__(nome,cor,tamanho,preco)
        self.g = danca

    def deslizar(self):
        return("dançar de patins!")
    
class Domino(Brinquedos):
    def __init__(self,nome,cor,tamanho,preco,pecas):
        super().__init__(nome,cor,tamanho,preco)
        self.p = pecas

    def jogar(self):
        return("efeito domino!")
    
if __name__ == "__main__": 
    Bri_Normal = Brinquedos("a","a",3,"a")
    Brinquedo_peao = Peao("Peao","preto e branco", "30cm", 30,"aa")
    Brinquedo_bike = Bicicleta("Peao","preto e branco", "30cm", 30,1)
    Brinquedo_patins = Patins("Peao","preto e branco", "30cm", 30,1)
    Brinquedo_domino = Domino("Peao","preto e branco", "30cm", 30,1)

    print(Brinquedo_peao.rodar())
    print(Brinquedo_bike.andou())
    print(Brinquedo_patins.deslizar())
    
    print(Brinquedo_domino.jogar())

