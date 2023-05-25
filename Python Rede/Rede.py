print("Coloque seu IP de rede e em seguida sua máscara de sub-rede.")

rede =  bool(input("Rede:"))
rede_quarto = int(input("Quarto intervalo da rede:"))
mascara = int(input("Máscara:"))
if mascara > 32:
    print("Sua máscara de rede só pode ir até 32")

print("Possiveis intervalos de redes")
redeNova = rede_quarto - 30
print(f"\n{redeNova}")

mascara_sub_rede = 32 - mascara 
print(f"\nQuantidades de Bits para Host {mascara_sub_rede}")

if mascara_sub_rede == 8:
    primeiroB =  2**0
    print(f"\nA máscara da sua rede é: 255.255.255.{primeiroB}")

elif  mascara_sub_rede == 7:
    oitavoB = 2**7
    print(f"\nA máscara da sua rede é: 255.255.255.{oitavoB}")

elif  mascara_sub_rede == 6:
    oitavoB = 2**7
    setimoB  = 2**6
    print(f"\nA máscara da sua rede é: 255.255.255.{oitavoB + setimoB}")


elif  mascara_sub_rede == 5:
    oitavoB = 2**7
    setimoB  = 2**6
    sextoB = 2**5
    print(f"\nA máscara da sua rede é: 255.255.255.{oitavoB + setimoB + sextoB}")

elif  mascara_sub_rede == 4:
    oitavoB = 2**7
    setimoB  = 2**6
    sextoB = 2**5
    quintoB = 2**4
    print(f"\nA máscara da sua rede é: 255.255.255.{oitavoB + setimoB + sextoB + quintoB}")

elif  mascara_sub_rede == 3:
    oitavoB = 2**7
    setimoB  = 2**6
    sextoB = 2**5
    quintoB = 2**4
    quartoB = 2**3
    print(f"\nA máscara da sua rede é: 255.255.255.{oitavoB + setimoB + sextoB + quintoB + quartoB}")  


