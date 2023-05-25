soma = 0
media = 0.0
cont = 1
while (cont<21):
    print (f"Digite os dados da {cont}a. pessoa")
    nome = input(str("Nome:"))
    idade = int(input("Idade:"))
    soma = soma + idade
    cont += 1

media = soma / 20

print (f"A média de idade é {media}")