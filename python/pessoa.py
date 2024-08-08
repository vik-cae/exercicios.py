class Pessoa :
    def __init__(self,nome,ano__nasc,cpf,raca,time,idade):
        self.name = nome
        self.ano = ano__nasc
        self.cpf = cpf
        self.raca = raca
        self.time = time
        self.idade = idade

    def mostrarano (self):
        return (f"ano do seu nascimento: {self.ano}")
    
    def mostrarquali(self):
        return (f"seu nome é: {self.name} ")
    
    def mostrarcpf(self):
        return(f"o cpf é: {self.cpf}")
    
    def mostrarraca(self):
        return(f"a raça é: {self.raca}")
    
    def mostrartime(self):
        return (f"seu time é: {self.time}")
    
    def mostraridade(self):
        return(f"sua idade é: {self.idade}")
        

p1 = Pessoa("vitoria", 2006, 64433457, "branca", "corinthians", 18)

print(p1.mostrarano())
print(p1.mostrarquali())
print(p1.mostrarcpf())
print(p1.mostrarraca())
print(p1.mostrartime())
print(p1.mostraridade())
