class Funcionario:
    def __init__(self,nome,matricula,salario):
        self.nm = nome
        self.matri = matricula
        self.din = salario

    def nomee(self):
        return(f"Nome: {self.nm}")
    
    def mat(self):
        return(f"matricula: {self.matri}")
    
    def receber(self):
        return(f"salario: {self.din}")
    
    def Bater_ponto(self):
        op = int(input("digite 1 para bater ponto ou 0 para não bater o ponto: "))
        if op == 1:
            op = True

        elif op == 0:
            op = False

        else :
            return(f"ocorreu um erro!")

class Vendedor(Funcionario):
    def __init__(self,nome,matricula,salario,bater_meta):
        super().__init__(nome,matricula,salario)
        self.meta = bater_meta

    def compromisso(self):
        return("a meta é R$ 3.000!!")

class Gerente(Funcionario):
    def __init__(self,nome,matricula,salario,senha,email):
        super().__init__(nome,matricula,salario)
        self.se = senha
        self.mail = email

    def senha_getente(self):
        sen = int(input("digite a senha: "))
        
        if sen == 1234:
            return(f"Seja bem-vindo {self.nm}")
        
        else :
            return("Ocorreu um erro!!!")
    def e_mail(self):
        return(f"email: {self.mail}")

if __name__ == "__main__": #se tiver no arquivo principal
    Funcionario_Normal = Funcionario("vitoria caetana",9876,"2.000")
    Funcionario_Vendedor = Vendedor("vitoria caetana",9876,"2.000",1.000)
    Funcionaro_Gerente = Gerente("vitoria caetana",9876,"2.000",1234,"vivi@")
    #metodos da classe passagem 
    print(Funcionario_Normal.nomee())
    print(Funcionario_Normal.mat())
    print(Funcionario_Normal.receber())
    print(Funcionario_Normal.Bater_ponto())

    #metodos da classe ingresso vip
    print(Funcionario_Vendedor.compromisso())
    print("Você não bateu a meta ese mês!!")
    
    #metodos da classe aviao
    print(Funcionaro_Gerente.senha_getente())
    print(Funcionaro_Gerente.e_mail())
    
