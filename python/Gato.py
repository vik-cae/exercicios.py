class Gato:
    def __init__(self,nome,cor,peso):
        self.name = nome
        self.cor = cor
        self.peso = peso
 
    def hello(self):
        print (f"{self.name} MIOUUUU")
        
gato1 =Gato("gato de botas","laranja",5)
gato2 =Gato("Felix", "preto",5)
gato1.hello()

####
#class Circulo:
 #   def __init__(self,r:float):
  #      self.raio = r
#
#    def get_raio(self):
 #       return self.raio
    
  #  def calcular_area(self):
   #     raio = 5
    #    return 3.1415 * (self.raio * self.raio)
#Circule = Circulo(3.4) 
#print(Circulo.calcular_area(3.1415))

##
class Pessoa:
    def __init__(self)->None:
        pass 
    def hello (self):
        print("oi")

p1 = Pessoa()
p1.hello()        

###
class Pessoa :
    def __init__(self,nome,ano__nasc):
        self.name = nome
        self.idade = ano__nasc
    def mostraridade (self):
        return self.idade
    def mostrarquali(self,quali):
        return (f"{self.name} é muito {quali}")
p1 = Pessoa("thiago", 1986)

print(p1.mostraridade())
print(p1.mostrarquali("top"))