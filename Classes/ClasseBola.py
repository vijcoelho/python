class Bola:
    def __init__(self, cor="unknown", circunf=0, material="unknown"):
        self.cor = cor
        self.circunf = circunf
        self.material = material

    def trocaCor(self):
        troca = input(f"Deseja mudar a cor atual {self.cor}? [s/n]")

        troca = troca[0].lower()

        if troca == "s":
            nova_cor = input("\n> Nova Cor: ")
            self.cor = nova_cor
        else:
            print(f"Ok a cor continua {self.cor}")

    def mostraCor(self):
        print(f"\nA cor atual é {self.cor}")

bola01 = Bola("azul", 5, "metal")


bola01.mostraCor()
bola01.trocaCor()
bola01.mostraCor()

