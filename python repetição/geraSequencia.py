while (True):
    ateOnde = int(input("\tDigite um valor positivo para ser o final da sequencia:"))
    if (ateOnde<=0):
        break
    item=1
    strItens=""
    while (item<=ateOnde):
        strItens= strItens +" "+ str(item)
        item= item + 1
    print (strItens + "\n")

print ("\tCiao")
