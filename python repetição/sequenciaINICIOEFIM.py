while (True):
    print("-------====DIGITE 2 NUMEROS E VEJA A SUA SEQUENCIA ENTRE ELES====-------")
    
    apartirdeOnde = int(input("\tDigite um valor positivo para ser o inicio da sequencia:"))
    if (apartirdeOnde==0):
        break
    
    ateOnde = int(input("\tDigite um valor positivo para ser o final da sequencia:"))
    if (apartirdeOnde>ateOnde):
        item = apartirdeOnde
        apartirdeOnde = ateOnde
        ateOnde = item
    
    item=apartirdeOnde
    strItens=""
    
    while (item<=ateOnde):
        strItens= strItens +" "+ str(item)
        item= item + 1
    
    print (strItens + "\n")

print ("\t\tCIAOOOOOOOOOOOO!!!!!!!!!!!")
