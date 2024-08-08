class Compra:
    def __init__(self,numero,produto,valor,valor_total=0):
        self.num = numero
        self.pro = produto
        self.v = valor
        self.v_t = valor_total

    def n(self):
        return(f"numero do produto: {self.num}")
    
    def produtos(self):
        return(f"produto: {self.pro}")
    
    def valores(self):
        return(f"valor do produto: {self.v}")
    
    def cal_v_t(self):
        icms = self.v * 0.17
        frete = self.v * 0.05
        valor_total = self.v + icms + frete
        return(f"valor total: {valor_total}")
    
class Avista(Compra):
    def __init__(self,numero,produto,valor,valor_total,desconto=30):
        super().__init__(numero,produto,valor,valor_total)
        self.des = desconto

    def descontos(self):
        icms = self.v * 0.17
        frete = self.v * 0.05
        valor_total = self.v + icms + frete
        valor_desconto = valor_total * (self.des/100)
        preco_desconto = valor_total - valor_desconto
        return(f"cliente q paga avista tem 30% de desconto!!\no valor d sua compra com desconto é: {preco_desconto}")


class Parcela(Compra):
    def __init__(self,numero,produto,valor,valor_total,parcelas=3):
        super().__init__(numero,produto,valor,valor_total)
        self.par = parcelas

    def parcela(self):
        icms = self.v * 0.17
        frete = self.v * 0.05
        valor_total = self.v + icms + frete
        num = valor_total/self.par
        return(f"sua compra foi divididas em 3x e a valor de cada parcela é: {num:.2f}")

if __name__ == "__main__": #se tiver no arquivo principal
    Compra_Normal = Compra(1234567,"cll",2000,2.000)
    Compra_Avista = Avista(1234567,"cll",2000,2.000)
    Compra_Parcela = Parcela(1234567,"cll",2000,2000)
    #metodos da classe passagem 
    print(Compra_Normal.n())
    print(Compra_Normal.produtos())
    print(Compra_Normal.valores())
    print(Compra_Normal.cal_v_t())
    
    #metodos da classe ingresso vip
    print(Compra_Avista.descontos())

    print(Compra_Parcela.parcela())
    
    
    

    
    


