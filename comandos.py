num1 = int(input("Digite um numero: "))

num2 = input ("digite outro numero: ")
num2 = int(num2)

Soma= num1+num2
Subtração = num1-num2
Multiplicação = num1*num2


quest = (input("Soma, Subtração, Multiplicação ou Divisao?: "))

if quest == Soma :
    print("Soma:\t\t", num1+num2)
if  quest == Subtração  :
    print(f"Subtração:\t {num1-num2}")
if quest ==  Multiplicação :
    print(f"Multiplicação:\t{num1*num2}")

if num2!=0:
    print(f"Divisão:\t{num1/num2}")
else: # num2==0
    print("Nao Existe")


