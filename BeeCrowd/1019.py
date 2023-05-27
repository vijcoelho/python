segundo = int(input())
minutos = int(segundo/60)
segundo %= 60
horas = int(minutos/60)
minutos %= 60

print(f'{horas}:{minutos}:{segundo}')