print("Cálculo De Imposto de Renda")
vhora = float(input('Digite o valor que recebe por hora:'))
Qthoras = int(input('Digite a quantidade de horas que trabalha:'))
sal_bruto = vhora * Qthoras
# calculo do imposto de renda
if sal_bruto <= 900:
    ir = 0
    aliquota = 0
elif sal_bruto <= 1500:
    ir = sal_bruto * 0.05
    aliquota = 5
elif sal_bruto <= 2500:
    ir = sal_bruto * 0.1
    aliquota = 10
else:
    ir = sal_bruto * 0.2
    aliquota = 20

inss = sal_bruto * 0.1

fgts = sal_bruto * 0.11
imp_sind = sal_bruto * 0.03

total_desc = ir + inss

sal_liquido = sal_bruto - total_desc

print("Sálario bruto: (", vhora, "*", Qthoras, ") : R$ ", sal_bruto)
print("(-) IR(", aliquota, "%)                 : R$  ", ir)
print("(-) INSS (10%)               : R$ ", inss)
print("FGTS (11%)                   : R$ ", fgts)
print("Total de descontos           : R$ ", total_desc)
print("Salário Líquido              : R$ ", sal_liquido)
