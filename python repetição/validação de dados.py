
nome = input("Seu Nome:")
while (True):
    idade = int(input("Sua idade:"))
    
    if (idade < 0):
        print("Sua idade não pode ser negativa. Digite novamente.")
    elif (idade > 100):
        print ("Sua idade não pode ser mais de 100 anos.")
    else:
        break

end = input("Seu endereço:")
