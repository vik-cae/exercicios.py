from Produto import Produto
from Cliente import Cliente
from funcoes import pot

p1 = Produto("sabao","omo",19.90,56)
p1.getNome()
p1.getEstoque()

cli = Cliente("joão", 58)
print()
cli.getNome()

x = pot(2,5)
print(x)