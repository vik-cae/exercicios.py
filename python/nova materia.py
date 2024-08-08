#o programa espera que o usuario digte dois numeros inteiros
try:
    n1 = int(input("digite um numero: "))
    n2 = int(input("digite um numero: 10"))
    res = n1 +n2
    print (res)
except:
    print("por gentilez querido usuario!! \n preste atenção ao digitar os numeros")


###
i = 0
soma = 0
while i <10:
    try:
        num = int(input("digite um numero: "))
        soma += num
        i = i + 1
    except:
        print("entrada invalida!! tente novamente ")

print("total: ",soma)