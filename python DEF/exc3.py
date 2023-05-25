def digitos (s):
    for char in s:
        if not char.isdigit():
            return False
        return True

char = (int(input(':')))
resultado = digitos (s)
print(resultado)