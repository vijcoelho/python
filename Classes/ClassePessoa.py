class Pessoa:
    def __init__(self,nome='unknow',idade=0,peso=0, altura=0):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        if self.idade < 21:
            nova_altura = self.altura + 0.05
            self.altura = nova_altura
        self.idade += 1
            
    def engordar(self):
        if self.altura < 1.80:
            novo_peso = self.peso + 5.5
            self.peso = novo_peso
        else: 
            novo_peso = self.peso + 3.5
            
    def emagrecer(self):
        pergunta = input('\nFez atividade física? [s/n]: ')
        pergunta = pergunta[0].lower()
        if pergunta == 's':
            novo_peso = self.peso - 5.7
            self.peso = novo_peso
        else: 
            novo_peso = self.peso + 7.2
            self.peso = novo_peso

    def resultado(self):
        print(f'\nO resultado de tudo é {self.idade} anos, {self.altura:,.2f} altura, {self.peso:,.2f} peso.')
        
Vitor = Pessoa('Vitor', 19, 58, 1.80 )
while (True):
    Vitor.envelhecer()
    Vitor.engordar()
    Vitor.emagrecer()
    Vitor.resultado()