class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa("Ricardo", 36)
pessoa2 = Pessoa("Barbara", 25)
pessoa3 = Pessoa("Fernando", 99)

pessoas = [pessoa1, pessoa2, pessoa3]

print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade}")
print(f"Nome: {pessoa2.nome}, Idade: {pessoa2.idade}")
print(f"Nome: {pessoa3.nome}, Idade: {pessoa3.idade}")
