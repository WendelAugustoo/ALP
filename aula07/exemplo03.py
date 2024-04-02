qtd = 0
frase = input("Digite uma frase: ")
for letra in frase:
    if letra in 'AEIOUaeiouãíéõúàÉ':
        qtd = qtd+1
print(f"Existem {qtd} vogais na frase.")