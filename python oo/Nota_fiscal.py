class Nota_Fiscal:
    def __init__(self, numero,serie,cnpj,razao_social,data,valor_produto,icms,frete):
        self.numero = numero    
        self.serie = serie    
        self.cnpj = cnpj    
        self.razao = razao_social    
        self.data = data
        self.valor = valor_produto    
        self.icms = icms   
        self.frete = frete    
    def setNumero(self,entrada,saida):
        return(f"o numero de produtos é: {self.numero}")
    
    def getData(self,dia,mes,ano):
        return(f"a data de emissao é: {self.data}")
    
    def setAlterar_razao(self):
        return(f"Razão Social: {self.razao}")
    
    def getCalcular_total(self):
        cal = self.valor + self.frete
        return(f"o valor total é: {cal}")
    
p1 = Nota_Fiscal(230,1,25984299,"160tecnologia ltda",2022,2800,90,10)
print(p1.setNumero(10,3))
print(p1.getData(9,11,2006))
print(p1.setAlterar_razao())
print(p1.getCalcular_total())
