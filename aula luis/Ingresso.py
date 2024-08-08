class Ingresso:
    def __init__(self,preco,setor):
        self.preco = preco
        self.setor = setor

    def alterar_preco(self,novo_preco):
        self.preco = novo_preco

    def mostrar_setor(self):
        return(f"setor do ingresso: {self.setor}")
    
class IngressoVIP(Ingresso):
    def __init__(self,preco,setor,camarote = False, open_bar = False,open_food = False,estacionamento = False):
        super().__init__(preco,setor)
        self.camarote = camarote
        self.open_bar = open_bar
        self.opn_food = open_food
        self.estacionamento = estacionamento

    def pegar_bebida (self):
        if self.open_bar:
            print("voce pode pegar bebida no bar")
        else:
            print("este ingresso nao inclui open bar")

    def acessar_camarote(self):
        if self.camarote:
            print("voce tem acesso ao camarote")
        else:
            print("esse ingresso nao inclui acesso ao camarote")


#exemplo de uso

if __name__ == "__main__": #se tiver no arquivo principal
    Ingresso_normal = Ingresso(preco=50.0,setor="ARQUIBANCADA")
    Ingresso_VIP = IngressoVIP(preco=150.0,setor="VIP",camarote=True,open_bar=True,open_food=True,estacionamento=True)

    #metodos da classe ingressonormal
    Ingresso_normal.mostrar_setor()
    Ingresso_normal.alterar_preco(60.0)
    print(f"novo preço do ingresso normal R${Ingresso_normal.preco: .2f}")
    #metodos da classe ingresso vip
    Ingresso_VIP.mostrar_setor()
    Ingresso_VIP.pegar_bebida()
    Ingresso_VIP.acessar_camarote()
