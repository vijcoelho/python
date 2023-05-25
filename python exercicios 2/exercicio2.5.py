n1=float(input("nota de matemática:"))
n2=float(input("nota de português:"))
n3=float(input("nota de geografia:"))
media=float(input("media de exercicio:"))
resultado=((n1+n2*2+n3*3)+media)/7
print(resultado)
if (resultado>=9.0):
    print("Conceito A")
elif(resultado>=7.5<9.0):
    print("Conceito B")
elif(resultado>=6.0<7.5):
    print("Conceito C")
elif(resultado<6.0):
    print("Conceito D")



