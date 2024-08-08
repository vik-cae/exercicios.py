def argumento(p_eletrica,tempo):
    p_eletrica = float(input("digite a potencia eletrica o aparelho: "))
    tempo = float(input("digite o tempo ligado: "))
    cal = (p_eletrica * tempo * 1)/1000
    res = (p_eletrica*tempo*30)/1000
    print("o consumo do aparelho em um dia em KWh é: ", cal,"kWh/dia")
    print ("\no calculo da conta de energia no mês é: ",res,"kWh/mês")

argumento('p_eletrica','tempo')

