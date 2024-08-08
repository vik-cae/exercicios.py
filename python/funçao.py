
def soma (x,y):
    soma = x+y
    return(soma)
    #nao se usa print dentro da função
res = soma(10,5)
print(res)

## args É UMA LISTA DE PARAMETROS

def multiple(*args):
    for i in args:
        print(i)
res = multiple(3,5,7,9,8)

###
def world_cup_titles(country,*args):
    print('pais: ',country)
    for titulo in args:
        print('ano: ',titulo)
pais = "BRASIL"
world_cup_titles("italia",1950,1962.1994,2002)

##¨KWargs É UM DICIONARIO QUE CONTÉM OS PARAMETROS


def mostrafuncionario(**kwarg):
    print(kwarg)
mostrafuncionario(nome="vitoria",idade="18",email = "vivi",sal = "300000")


