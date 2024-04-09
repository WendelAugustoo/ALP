data = input("Digite uma data <DD/MM/AAAA> : ")
dia = data[0:2]
mes = data[3:5]
ano = data[6::]
data_invertida = ano+mes+dia
print(f"A data é {data_invertida}")