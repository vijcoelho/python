num1 = int(input("Digite um numero: "))
num2 = int (input ("digite outro numero: "))

print ("Digite a operação desejada seguindo a lista a baixo")
print ("\t + para SOMA")
print ("\t - para SUBTRAÇÃO")
print ("\t * para MULTIPLICAÇÃO")
print ("\t / para DIVISÃO")

op= input("Operação: ")

if (op=="+") or (op=="SOMA"):
    print("Soma:\t\t", num1+num2)
elif (op=="-") or (op=="SUBTRAÇÃO"):
    print(f"Subtração:\t {num1-num2}")
elif (op=="*") or (op=="MULTIPLICAÇÃO"):
    print(f"Multiplicação:\t{num1*num2}")
elif (op=="/") or (op=="DIVISÃO"):
    if num2!=0:
        print(f"Divisão:\t{num1/num2}")
    else:
        print("Nao Existe")
