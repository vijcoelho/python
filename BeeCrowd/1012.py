linha1 = input().split(" ")
a, b, c = linha1
triangulo = (float(a) * float(c) / 2)
pi = 3.14159
raio = (pi* (float(c)**2))
trapezio = ((float(a) + float(b)) * float(c)) / 2
quadrado = (float(b)**2)
retangulo = (float(a) * float(b))

print("TRIANGULO: %0.3f"%(triangulo))
print("CIRCULO: %0.3f"%(raio))
print("TRAPEZIO: %0.3f"%(trapezio))
print("QUADRADO: %0.3f"%(quadrado))
print("RETANGULO: %0.3f"%(retangulo))