class BichinhoVirtual:
    def __init__(self, nome='unknown', fome=0, saude=0, idade=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        
    def AlterarNome(self):
        pergunta = input('\nGostaria da o nome ou trocar o nome do bichinho?[s/n]: ')
        pergunta = pergunta[0].lower()
        if pergunta =='s':
            novoNome = input('Coloque o novo nome: ')
            self.nome = novoNome
            print('\t\nNome: %s'%self.nome)
        else: 
            print('\t\nNome: %s'%self.nome)
            
    def Idade(self):
        self.idade = int(input('\nDefina a idade do seu bichinho: '))
        print(f'\t\nIdade : {self.idade} anos')
        
    def AlterarFome(self):
        while(True):
            lista = int(input('\nPressione (1) para exibir o mercado ou (0) para sair: '))
            if lista == 0: break
            elif lista == 1:
                comidas =  float(input("""\n\t\t\t\t\t\t -MERCADO-
                                    \t Para da comida é só digitar o nome da comida
                                    \t Comidas: 1 - Carne   +2.5(fome)
                                    \t          2 - Maça    +1(fome)
                                    \t          3 - Banana  +1(fome)
                                    \t          4 - Peixe   +1.5(fome)
                                    \t          5 - Batata  +1.5(fome)
                                    \t          6 - P.F     +3(fome)
                                    \t          Coloque Aqui : """))
                if comidas == 1:
                    aumentoFome = self.fome + 2,5
                    self.fome = aumentoFome
                    print(f'\t\nFome : +{self.fome}')
                elif comidas == 2 or comidas == 3:
                    aumentoFome = self.fome + 1
                    self.fome = aumentoFome
                    print(f'\t\nFome : +{self.fome}')
                elif comidas == 4 or comidas == 5:
                    aumentoFome = self.fome + 1.5
                    self.fome = aumentoFome
                    print(f'\t\nFome : +{self.fome}')
                elif comidas == 6:
                    aumentoFome = self.fome + 3
                    self.fome = aumentoFome
                    print(f'\t\nFome : +{self.fome}')
                else: print(f'\t\nFome : +{self.fome}')
    
        print('\n\tFome : %s'%self.fome)
        
    def Saude(self):
        if self.fome > 25:
            self.saude = 100
            print(f"""\nA saúde do seu bichinho PERFEITO 🙌😊| Saúde : {self.saude}
                  E seu humor é de EXTREMA FELICIDADE""")
        elif self.fome > 15:
            self.saude = 80
            print(f"""\nA saúde do seu bichinho está muitooo bemmm 😁| Saúde : {self.saude}
                  E seu humor é de felicidade""")            
        elif self.fome == 10:
            self.saude = 40
            print(f"""\nA saúde do seu bichinho está bem melhor 😉| Saúde : {self.saude}
                  E seu humor cada vez mais feliz""")
        else: 
            print(f"""\nA saúde do seu bichinho nao está muito legal 😢| Saúde : {self.saude}
                  E seu humor está bem baixo""")

          
Bichinho = BichinhoVirtual()
Bichinho.AlterarNome()
Bichinho.Idade()
while(True):
    sair = int(input('\nQuando quiser sair so digitar (0) pra continar digite (1): '))
    if sair == 0:break
    else:
        Bichinho.AlterarFome()
        Bichinho.Saude() 
    