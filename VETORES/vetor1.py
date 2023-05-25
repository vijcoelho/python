vecx = []
for i in range(3):
 print('Digite um valor para a posição ', i ,' do vetor x: ')
 vecx.append(float(input()))
vecy = []
for i in range(3):
 print('Digite um valor para a posição ', i ,' do vetor y: ')
 vecy.append(float(input()))
vecr = []
for i in range(3):
 vecr.append(vecx[i]+vecy[i])
 print('O vetor resultante é: ',vecr)