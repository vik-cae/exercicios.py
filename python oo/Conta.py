class Conta:
    def __init__(self,nome,cpf,numero,saldo):
        self.nome = nome
        self.cpf = cpf
        self.num = numero
        self.saldo = saldo

    def getNome(self):
        return(f"\ncliente: {self.nome}")

    def getCpf(self):
        return(f"\nCPF: {self.cpf}")

    def getNum(self):
        return(f"\nNumero: {self.num}")

    def setDeposito(self, novoValor):
        self.saldo = self.saldo + novoValor
        return self.saldo
    
    def setSacar(self, retirar):
        self.saldo = self.saldo - retirar
        return self.saldo
    
    def getImprimir(self):
        return self.saldo
    
p1 = Conta("vitoria",786482986589,992095948,10000.50)
print (p1.getNome())
print (p1.getCpf())
print (p1.getNum())
print (p1.setDeposito(346433.00))
print (p1.setSacar(24851.55))
print (p1.getImprimir())