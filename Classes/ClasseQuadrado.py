class quadrado:
    def __init__(self, lado="0"):
        
        self.lado = lado
    
    def trocarValor(self):
        
        trocar = input('Deseja trocar o valor do lado do quadrado? [s/n] ')
        trocar = trocar[0].lower()
        
        if trocar == 's':
            novoLado = int(input('\nColoque o novo valor do lado do quadrado: '))
            self.lado = novoLado
        else: print('\nO lado continua %s'%(self.lado))

    def calcularArea(self):
        
        print(f'\nO lado é de {self.lado} e a sua area é igual a {self.lado ** 2}cm².')
    
q = quadrado(1)
q.trocarValor()
q.calcularArea()