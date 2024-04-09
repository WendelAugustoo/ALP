numero = (input("Digite nove caracteres numéricos: "))
if numero.isdigit():
    milhao = numero[0]
    milhar = numero[1:4]
    centena = numero[4:7]
    decimal = numero[7::]
    print(f"{milhao}.{milhar}.{centena},{decimal}")
else:
    print("Não é um número")