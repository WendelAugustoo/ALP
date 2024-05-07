def conversao(horas, minutos, segundos):
    total_seg = horas * 3600 + minutos * 60 + segundos
    return total_seg
horas = 3
minutos = 20
segundos = 45

total_seg = conversao(horas, minutos, segundos)
print(f"{horas} horas, {minutos} minutos e {segundos} segundos equivalem a {total_seg} segundos ")