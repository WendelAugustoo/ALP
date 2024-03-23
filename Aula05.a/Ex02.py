nota1 = float(input("Digite sua nota primeira nota:"))
nota2 = float(input("Digite sua segunda nota:"))
media = (nota1 + nota2) /2

if media >=9:
    conceito = "A"
elif 7.5 <= media <9:
    conceito = "B"
elif 6 <=media <7.5:
    conceito = "C"
elif 4 <=media <6.0:
    conceito = "D"
elif media <4:
    conceito = "E"
print("Média de aproveitamento:",media)
print("Conceito:",conceito)
