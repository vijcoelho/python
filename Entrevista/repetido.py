def repeticao(valor):
    letras = set()
    for i in valor:
        if i in letras:
            return True
        letras.add(i)
    return False

obj = repeticao("teste")
print(obj)