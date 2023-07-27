class Filme:
    def __init__(self, nome_do_filme, atores, atrizes, diretor, oscar):
        self.nome_do_filme = nome_do_filme
        self.atores = atores
        self.atrizes = atrizes
        self.diretor = diretor
        self.oscar = oscar
        
    def mostrar_nome_do_filme(self):
        return "Nome do filme: %s"%self.nome_do_filme
    
    def ator(self):
        return "Atores: Shrek e %s"%self.atores
    
    def atriz(self):
        return "Atrizes: Dragão Femea e %s"%self.atrizes
    
    def diretor_do_filme(self):
        return "Diretor: Andrew Adamson e %s"%self.diretor
    
    def tem_oscar(self):
        return "%s tem Oscar"%self.oscar
    
i = Filme("Shrek", "Burro", "Fiona", "Vicky Jenson", "Shrek")
print(i.mostrar_nome_do_filme())
print(i.ator())
print(i.atriz())
print(i.diretor_do_filme())
print(i.tem_oscar())
        