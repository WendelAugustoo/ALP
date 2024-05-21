y = int(input("Digite a quantidade de cabeças: "))
pes = int(input("Digite a quantidade de pés: "))
coelho = (pes - 2 * y)//2
pato = y - coelho
print(f"O total de patos é: {pato}")
print(f"O total de coelhos é: {coelho}")