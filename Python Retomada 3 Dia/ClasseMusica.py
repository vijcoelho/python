class Musica:
    def __init__(self, nome, cantor, compositor, data_de_lancamento):
        self.nome = nome
        self.cantor = cantor
        self.compositor = compositor
        self.data_de_lancamento = data_de_lancamento
        
    def monstrar_nome_musica(self):
        return "Nome da musica: %s"%self.nome
    
    def mostrar_nome(self):
        return "Nome do cantor: %s"%self.cantor
    
    def mostrar_compositor(self):
        return "Nome do compositor: %s"%self.compositor

    def data(self):
        return "Data de lancamento é dia %s"%self.data_de_lancamento
    
a = Musica("Se eu largar o freio", "Péricles", "Péricles", "21/10/2023")
print(a.monstrar_nome_musica())
print(a.mostrar_nome())
print(a.mostrar_compositor())
print(a.data())