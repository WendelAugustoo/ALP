print("Cálculo de quantidade de latas de tinta")
larg = float(input("Digite a largura do aposento em metros:"))
comp = float(input("Digite o comprimento do aposento em metros:"))
lata = float(input("Digite a quantidade de litros da lata de tinta:"))
area1 = larg*2.8*2
area2 = comp*2.8*2
area_total = (area1+area2)
area_pintura = area_total-1.68
litros_nec = area_pintura/3
qt_latas = litros_nec/lata

print("Quantidade de latas necessárias:",qt_latas)