def encontrar(n):
    soma = 0
    for i in range(1,n):
        if n % i == 0:
            soma += i
    return soma
    
def somaDivisores():
    
    vec  = []
    for i in range(1, 1000):
        soma = encontrar(i)
        if soma < 1000:
            if i != soma:
                if encontrar(soma) == i:
                    vec.append((i, soma))

    for i in vec:
        print(i)

somaDivisores()