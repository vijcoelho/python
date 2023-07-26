class Carro:
    def __init__(self, marca="", modelo="", cor="", ano=0):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.ligado = False
    
    def ligar(self):
        self.ligado = True
        print("O carro está ligado")
    
    def desligar(self):
        self.ligado = False
        print("O carro está desligado.")
    
    def acelerar(self):
        if self.ligado:
            print("O carro está acelerando.")
        else:
            print("O carro está desligado.")
    
    def frear(self):
        if self.ligado:
            print("O carro está freando.")
        else:
            print("O carro está desligado.")
    
    def pintar(self, nova_cor):
        self.cor = nova_cor
        print(f"O carro foi pintado de {nova_cor}.")
    
    def mostrar_marca(self):
        print("A marca do carro é %s" % self.marca)
    
    def mostrar_modelo(self):
        print("O modelo do carro é %s" % self.modelo)
                                                       
    def mostrar_cor(self):
        print("Cor do carro: %s" % self.cor)
        
    def mostrar_ano(self):
        print("Ano do carro: %s" % self.ano)

meu_carro = Carro("Toyota", "Corolla", "vermelho", 2011)
meu_carro.mostrar_cor()
meu_carro.pintar("azul")
meu_carro.mostrar_cor()
