matriz = [[1,2,3],[4,5,6],[7,8,9]]
soma = 0


for i in range (len(matriz)):
    for j in range (len(matriz[0])):
        soma = matriz [i][j]+soma
print (soma)