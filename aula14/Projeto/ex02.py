def calcular_primo(y):
    if y % 2==0:
        return True
    else:
        return False
y = int(input("Digite o número: "))
calcular_primo(y)
print(calcular_primo(y))