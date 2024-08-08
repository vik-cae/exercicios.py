class Pessoa:
    def __init__(self,nome,telefone,email,endereco):
        self.nm = nome
        self.tele = telefone
        self.emai = email
        self.ende = endereco

    def name(self):
        return(f"nome: {self.nm}")
    
    def fone(self):
        return(f"telefone: {self.tele}")
    
    def mail(self):
        return(f"email: {self.emai}")
    
    def local(self):
        return(f"endereço: {self.ende}")
    
    def negociar(self):
        neg = input("deseja negociar?")
        if neg == 'sim' or neg == 'SIM' :
            print("vamos negociar!")

        elif neg == 'nao' or neg == 'NAO':
            print("não vamos negociar")

        else:
            print("ocorreu um erro!")

class Pesssoa_Física(Pessoa):
    def __init__(self,nome,telefone,email,endereco,cpf):
        super().__init__(nome,telefone,email,endereco)
        self.cpf1 = cpf

    def mostrar_cpf(self):
        return(f"cpf da pessoa física: {self.cpf1}")

class Pessoa_Jurídica(Pessoa):
    def __init__(self,nome,telefone,email,endereco,cnpj):
        super().__init__(nome,telefone,email,endereco)
        self.cnpj1 = cnpj

    def mostrar_cnpj(self):
        return(f"cnpj da pessoa jurídica: {self.cnpj1}")
    
if __name__ == "__main__": #se tiver no arquivo principal
    Pessoa_normal = Pessoa("vitoria",992095948,"vivi@","senac")
    Fisica = Pesssoa_Física("vitoria",992095948,"vivi@","senac",9875)
    Juridica = Pessoa_Jurídica("vitoria",992095948,"vivi@","senac",345678)

    #metodos da classe pessoa normal
    print(Pessoa_normal.name())
    print(Pessoa_normal.fone())
    print(Pessoa_normal.mail())
    print(Pessoa_normal.local())
    print(Pessoa_normal.negociar())
    
    #metodos da classe pessoa fisica
    print(Fisica.mostrar_cpf())
    
    #metodos da classe pessoa juridica
    print(Juridica.mostrar_cnpj())
    