class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def getRaio(self):
        return(f"raio: {self.raio}")
    
    def getCalculoArea(self):
        A = 3.14 * (self.raio **2)
        return(f"area do circulo: {A}")
    
    def getCircunferencia(self):
        C = 2 * 3.14 * self.raio
        return(f"circunferencia do circulo: {C}")
p1 = Circulo(10)   
print (p1.getRaio())
print (p1.getCalculoArea())
print (p1.getCircunferencia())