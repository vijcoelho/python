import random

sorteio = random.randint(1,10)

chances = 0
print("\t-----===JOGO DE ADIVINHAÇÃO===-----")
while (chances < 3):   
        num = int(input("Chute um número de 1 a 10: "))
        chances = chances+1
        
        if num == sorteio:
            print ("\t--==Parabéns você Acertou!==--")
            break
         
        elif ((num > sorteio - 2)) and ((num < sorteio +2)):
            print ("FERVENDO")

        elif ((num > sorteio - 3)) and ((num < sorteio +3)):
            print ("Quente")

        else:
             print ("Frio")

        if (num > sorteio):
            print ("DICA ===> O Número que escolheu é maior que o sorteado")
        else:
            print ("DICA ===> O Número que você escolheu é menor que o sorteado")



print ("\t\tESPERO QUE TENHA GOSTADO DE JOGAR :)")
print ("\t\tCASO QUEIRA JOGAR NOVAMENTE, APENAS EXECUTE O PROGAMA :)")