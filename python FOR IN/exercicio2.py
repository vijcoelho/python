print ("Escreva uma frase abaixo")
palavra =(input(":")).upper()
print ("Escreva uma letra abaixo")
letra = (input (":")).upper()
contador = 0
for x in palavra:
    if x == letra:
        contador += 1
print (f"\t==-A LETRA {letra}-==")
print (f" Essa letra aparece {contador} vezes na sua frase")
