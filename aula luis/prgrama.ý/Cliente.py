class Cliente:
    def __init__(self,nome,idade=None,fone=None,email=None):
        self.__nome = nome #atributo privado com dois __
        self.idade = idade
        self.fone = fone
        self.email = email

    def comprar(self):
        print(f"{self.__nome} realiza compra; ")

    def getNome(self):
        return self.__nome

class ClientePrimium(Cliente):
    def __init__(self,nome,idade=None,fone=None,email=None,areaVIP=None,desconto=20):
        super().__init__(nome,idade,fone,email)
        self.areavip = areaVIP
        self.desconto = desconto

    def comprar(self):
        print(f"{self.__nome} compra muito com {self.desconto}% de desconto")

clipremium = ClientePrimium("thiago",32,9999,"FGFGFJghg")
