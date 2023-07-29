num = int(input("Coloque um numero para ser a quantidade de casas da sequencia: "))


vetor = [0, 1]

while len(vetor) < num:
    proximoNum = vetor[-1] + vetor[-2]
    vetor.append(proximoNum)

print("Fibonacci:")
for i in vetor:
    print(i, end=" ")
