class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa("Ricardo", 36)
pessoa2 = Pessoa("Barbara", 25)
pessoa3 = Pessoa("Fernando", 99)

pessoas = [pessoa1, pessoa2, pessoa3]

for i in pessoas:
    print(f"Nome: {i.nome}, Idade: {i.idade}")

