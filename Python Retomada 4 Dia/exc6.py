palavra = input(">:") 
palavra = palavra.replace(" ", "")

for i in range (1):
    if palavra != palavra[::-1]:
        print ("nao é palindromo")
    else: 
        print ("é palindromo")
       
            
