class Carro:
    def __init__(self, marca="", modelo="", cor="", ano=0):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    
    def ligar(self):
        print("O carro está ligado.")
    
    def mostrar_marca(self):
        print("A marca do carro é %s" % self.marca)
    
    def mostrar_modelo(self):
        print("O modelo do carro é %s" % self.modelo)
                                                       
    def mostrar_cor(self):
        print("Cor do carro: %s" % self.cor)
        
    def mostrar_ano(self):
        print("Ano do carro: %s" % self.ano)

meu_carro = Carro("Toyota", "Corolla", "vermelho", 2011)
meu_carro.ligar()
meu_carro.mostrar_modelo()
meu_carro.mostrar_marca()
meu_carro.mostrar_cor()
meu_carro.mostrar_ano()
