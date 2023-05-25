print ("Escreva algo abaixo")
palavra =(input(":"))
contador = 0
for x in palavra:
    if x == 'a' or x == 'A':
        contador +=1
print (f"-=-=A letra A aparece {contador} nessa sua palavra-=-=")