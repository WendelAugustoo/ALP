maior_imc = 0
menor_imc = 100
soma_p = 0
soma_a = 0
for k in range (1,6):
    peso = float(input(f"Digite o peso {k} em kg: "))
    altura = float(input(f"Digite a altura {k} em metros: "))
    imc = peso / (altura * altura)
    if imc > maior_imc:
        maior_imc = imc
    if imc < menor_imc:
        menor_imc = imc
    soma_p = soma_p + peso
    soma_a = soma_a + altura
media_peso = soma_p/5
media_altura = soma_a/5
print("-------RESULTADOS--------")
print(f"O peso médio é {round(media_peso)} Kg")
print(f"A altura média é {round(media_altura)} metros")
print(f"O menor imc é {round(menor_imc)}")
print(f"O maior imc é {round(maior_imc)}")
