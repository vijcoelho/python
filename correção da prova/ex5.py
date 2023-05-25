def qDivisores(n):
    divisores=1
    metade=n/2
    aux=1
    while (aux<=metade):
        if(n%aux)==0:
            divisores+=1
        aux+=1
    return divisores

primos=0
q=0
while (True):
    num=int(input("Numero:"))
    if (num==0): break
    if (qDivisores(num)==5):
        q+=1
    if (qDivisores(num)==2):
        primos+=1


print (f"Foram digitados {q} numeros com 5 divisores")
print (f"Foram digitados {primos} numeros com 5 divisores")