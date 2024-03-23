a = (input("Digite o lado a do triãngulo:"))
b = (input("Digite o lado b do triângulo:"))
c = (input("Digite o lado c do triângulo:"))
if (a+b<c) or (b+c<a)or (a+c<b):
    print("Não é possivel formar um triângulo com esses valores")
elif 'a=b=c':
    print("é um triângulo equilátero")
elif 'a=b or a=c or b=c' :
    print("é um triângulo isósceles")
else:
    print("é um triângulo escaleno")