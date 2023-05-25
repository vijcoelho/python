while():
    peso=float(input("Seu peso em Kg:"))
    altura=float(input("Sua altura em metros:"))
    imc=peso/altura**2
    print("Seu IMC é",imc)
    if(imc<=18.5):
        print("Abaixo do peso")
    elif(18.5<imc<=25):
        print("Peso normal")
    elif(25<imc<=30):
        print("Acima do peso normal")
    elif(imc<30):
        print("Acima do peso")