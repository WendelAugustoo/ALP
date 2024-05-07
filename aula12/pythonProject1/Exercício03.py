from funcoes import conversao

h = int(input("Digite a quantidade de horas: "))
m = int(input("Digite a a quantidade de minutos: "))
s = int(input("Digite a quantidade de segundos: "))

print(f"O total de segundos é {conversao(h,m,s)}")