RA = str(input("Digite o número do seu RA: "))
lista = list(RA)
numeros = []
for val in RA:
        numeros.append(int(val))

soma = sum(numeros)
print(soma)

def multiplicar_valores(numero_str):
        produto = 1
        for valor in numero_str:
                if valor.isdigit():
                        produto *= int(valor)
        return produto
print(multiplicar_valores(RA))



