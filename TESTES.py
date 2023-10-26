cont = 1;
menor = float('inf');
menor2 = float('inf');
menor3 =  float('inf');
maior = float('-inf');

while(cont < 5):
    num = input(f"Valor {cont}: ")
    if (num.isdigit() or (num[0] == '-' and num[1:].isdigit())):
        cont += 1

        if (menor > num):
            menor3 = menor2
            menor2 = menor
            menor = num;
        elif (menor2 > num):
            menor3 = menor2
            menor2 = menor
            menor = num;