lista = []
for i in range(5):
    v = int(input(f"Digite o valor {i+1}: "))
    lista.append(v)

maior = max(lista)

print(f"O maior valor é {maior}, e sua posição é {lista.index(maior)+1}")