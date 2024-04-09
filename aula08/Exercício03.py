v = 0
frase = input("Insira uma frase: ")
for letra in frase:
    if letra.upper()in "AEIOU":
        v = v+1
print(f"Essa frase tem {v} vogais.")