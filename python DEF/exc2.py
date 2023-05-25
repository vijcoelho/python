def substituir_letra(texto, letra_antiga, letra_nova):
    novo_texto = ""
    for letra in texto:
        if letra == letra_antiga:
            novo_texto += letra_nova
        else:
            novo_texto += letra
    return novo_texto
while(True):
    texto = input("Coloque seu texto aqui:")
    letra_antiga = input("Letra que queira substituir:")
    letra_nova = input("Nova letra pro texto, porem caso queira sair aperte 0:")
    resultado = substituir_letra(texto, letra_antiga, letra_nova)
    print(f"Seu resultado é: {resultado}")