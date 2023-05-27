valor1 = input().split(" ")
x1, y1 = valor1
valor2 = input().split(' ')
x2, y2 = valor2

distancia = ((float(x2) - float(x1))**2 + (float(y2) - float(y1))**2)**0.5
print("%0.4f"%distancia)