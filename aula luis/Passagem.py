class Passagem:
    def __init__(self,preco,setor):
        self.preco = preco
        self.setor = setor

    def alterar_preco(self,novo_preco):
        self.preco = novo_preco

    def mostrar_setor(self):
        return(f"setor da passagem: {self.setor}")
    


class PassagemBus(Passagem):
    def __init__(self,preco,setor,placa,leito):
        super().__init__(preco,setor)
        self.placa1 = placa
        self.leito1 = leito
        

    def placa (self):
        return(f"a placa do onibus é: {self.placa1}")

    def leito(self):
        return(f"o seu leito é: {self.leito1}")




class PassagemAviao(Passagem):
    def __init__(self,preco,setor,portao_de_embarque,checkin):
        super().__init__(preco,setor)
        self.portao1 = portao_de_embarque
        self.checkin1 = checkin
        

    def portao (self):
        return(f"o portao de embarque é: {self.portao1}")

    def checkin (self):
        return(f"checkin: {self.checkin1}")



#exemplo de uso

if __name__ == "__main__": #se tiver no arquivo principal
    Passagem_Normal = Passagem(preco=100.0,setor=0)
    PassagemBus1 = PassagemBus(preco=50.0,setor=1,placa = 1234, leito= 24)
    PassagemAviao1 = PassagemAviao(preco=150.0,setor=1, portao_de_embarque= 2,checkin=123456)

    #metodos da classe passagem
    print(Passagem_Normal.alterar_preco(60.0))
    print(Passagem_Normal.mostrar_setor())
    print(f"novo preço do ingresso normal R${Passagem_Normal.preco: .2f}")


    #metodos da classe ingresso vip
    print(PassagemBus1.placa())
    print(PassagemBus1.leito())
    
    #metodos da classe aviao
    print(PassagemAviao1.portao())
    print(PassagemAviao1.checkin())