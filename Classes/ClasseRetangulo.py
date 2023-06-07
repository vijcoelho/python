class retangulo:
    
    def __init__(self, base=0, altura=0):
        
        self.base = base
        self.altura = altura
        
    def trocar(self):
        
        troca = input('\nDeseja trocar o valor da Base? [s/n]: ')
        
        if troca == 's':
            trocaBase = int(input('\nColoque o novo valor da Base: '))
            self.base = trocaBase
        
        elif troca == 'n':
            trocaAltura = input('\nDeseja entao trocar o valor da Altura? [s/n]: ')
            if trocaAltura == 's':
                trocaAltura = int(input('\nColoque o novo valor da Altura: '))
                self.altura = trocaAltura
            else: print(f'\nEntão sua Base é {self.base} e a sua Altura é {self.altura} .')
            
    def area(self):
        
        print(f'\nSua área é de {self.base * self.altura} cm².')
        
    def perimetro(self):
        
        print(f'\nSeu perimetro é de {self.base * 2 + self.altura * 2} cm.')
        
    def pisos(self):
        
        print(f'\nA quantidade de pisos necessarios sao de {(self.base * self.altura) * self.altura} .')
        
    def ehQuadrado(self):
        
        if self.base == self.altura: print('\nIsso é um Quadrado')
        else: print('')
        
r = retangulo(10,10)
r.trocar()
r.area()
r.perimetro()
r.pisos()
r.ehQuadrado()