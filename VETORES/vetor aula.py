vet= [0]*5
for i in range(len(vet)):
    vet[i] =int(input('numero: '))
print(vet)
menor=vet[0]
j=1
while j<len(vet):
    if (vet[j]<menor):
        menor=vet[j]
    j=j+1
print ('menor elemento' + str(menor))