vetor=[0]*10    
for i in range (10):
    vetor[i]=int(input(f'Digite o valor para a posição {i}:'))
conjunto=set(vetor)
diferente=len(conjunto)
print(f'Existem {diferente} valores diferentes no vetor')
 