class Triangulo:
    def __init__(self,ladoA,LadoB,LadoC):
        self.ladoA = ladoA     
        self.ladoB = LadoB     
        self.ladoC = LadoC    
        
    def getA(self):
        return(f"LadoA: {self.ladoA}")
    
    def getB(self):
        return(f"LadoB: {self.ladoB}")
    
    def getC(self):
        return(f"LadoC: {self.ladoC}")
    
    def getCalPerimetro(self):
        cal = self.ladoA + self.ladoB + self.ladoC
        return(f"o perimetro é: {cal}")

    def getMaiorLado(self):
        if self.ladoA > self.ladoB and self.ladoA > self.ladoC:
            return("ladoA é o Maior!")
        elif self.ladoB > self.ladoA and self.ladoB > self.ladoC:
            return("o lado B é o maior!")
        else:
            return("o ladoC é o maior")

p1 = Triangulo(10,7,4)
print(p1.getA())
print(p1.getB())
print(p1.getC())
print(p1.getCalPerimetro())
print(p1.getMaiorLado())
