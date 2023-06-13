class macaco:
    def __init__(self, nome="unknown", bucho=0):
        self.nome = nome
        self.bucho = bucho
        
    def comer(self):
        global comidas
        comidas = []
        while(True):
            pergunta = int(input("Pressione (1) para abrir o mercado e (0) para sair: "))
            if pergunta == 0: break
            if pergunta == 1:
                print("\t\n Bem vindo ao Mercado")
                comer = int(input("""1 - Salada 
2 - Carne
3 - Peixe
4 - Macarrao
5 - (MACACO)
Opçao : """))
                if comer == 1:
                    comidas.append("Salada")
                    print("Chomp Chomp Chomp")
                elif comer == 2:
                    comidas.append("Carne")
                    print("Chomp Chomp Chomp")
                elif comer == 3:
                    comidas.append("Peixe")
                    print("Chomp Chomp Chomp")                
                elif comer == 4:
                    comidas.append("Macarrao")
                    print("Chomp Chomp Chomp")
                elif comer == 5:
                    print("Macaco nao come MACACO 😡")
                    
    def verBucho(self):
        ver = int(input("\n(1) para ver o BUCHO: "))
        if ver == 1:
            print(f"\nSeu bucho : {comidas}")
        else: 
            print("\nSomente (1)")
            ver = int(input("\n(1) para ver o BUCHO: "))
        
    def digerir(self):
        pergunta = input("Gostaria que o Macaco digerisse as comidas? [s/n]: ")
        pergunta = pergunta[0].lower()
        if pergunta == "s":
            comidas.clear()
            print(f"Bucho Vazio: {comidas}")
        else: print(f"Seu bucho ficou assim: {comidas}")
        
Mamaco = macaco("Macaco")
Mamaco.comer()
Mamaco.verBucho()
Mamaco.digerir()

        