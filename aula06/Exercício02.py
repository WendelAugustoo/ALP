print("Cálculo de desconto da sua compra")
compra = float(input("Digite o valor da sua compra em R$:"))
if compra <= 1000:
    desconto = '10%'
    valor_final = compra*0.9
elif 1001<=compra <5000:
    desconto = '20%'
    valor_final = compra*0.8
elif compra >= 5000:
    desconto = '30%'
    valor_final = compra*0.7
print("Valor da compra em  R$:",compra)
print("Desconto              :",desconto)
print("Valor a ser pago em R$:",valor_final)