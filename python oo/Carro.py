class Carro:
    def __init__(self, modelo,marca,cor,ano,valor,consumo,nivel=5):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.nivel = nivel
        self.consumo = consumo

    def getModelo(self):
        return(f"modelo: {self.modelo}")
    
    def getMarca(self):
        return(f"marca: {self.marca}")
    
    def getCor(self):
        return(f"cor: {self.cor}")
    
    def getAno(self):
        return(f"ano: {self.ano}")
    
    def getValor(self):
        return(f"valor: {self.valor}")
    
    def getNivel(self):
        return(f"nivel: {self.nivel}")
    
    def getConsumo(self):
        return(f"consumo: {self.consumo}")
    
    
    def getLigar(self= True):
        return (f"o carro esta ligado!")
    
    def getAbastecer(self,novo_nivel):
        cal = self.nivel + novo_nivel
        return(f"o nivel novo é: {cal}")
    
    def getAndar(self,andar):
        return (f"a distancia em km que o veiculo andou é: {andar}")
# basta dividir o valor médio do litro da gasolina pelo consumo médio do carro
    def getVerificar_nivel(self,andar,litros):
        cal = andar / litros
        return(f"a quantidade de litros de combustivel gasto por km foi: {cal}")
    
    def getCalcular_imposto(self):
        cal = self.valor * 0.025
        cal1 = cal / 100
        return(f"o IPVA do carro é: {cal1}")
    
p1 = Carro("SF90","FERRARI","AZUL",2019,497000,8,10)
print(p1.getModelo())
print(p1.getMarca())
print(p1.getCor())
print(p1.getAno())
print(p1.getValor())
print(p1.getNivel())
print(p1.getConsumo())
print(p1.getLigar())
print(p1.getAbastecer(10))
print(p1.getAndar(200))
print(p1.getVerificar_nivel(10,200))
print(p1.getCalcular_imposto())