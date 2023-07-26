import random as rd

numSecreto = rd.randint(1,100)

while(True):
    chute = int(input())
    
    if chute > numSecreto:
        print("Chute é maior que o numero secreto")
    elif chute < numSecreto:
        print("Chute é menor que o numero secreto")
    else:
        print("Acertouuu")
        break

    