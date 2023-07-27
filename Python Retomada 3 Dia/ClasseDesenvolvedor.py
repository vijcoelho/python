class desenvolvedor:
    def __init__(self, nome, idade, linguagem, bug="unknow"):
        self.nome = nome
        self.idade = idade
        self.linguagem = linguagem
        self.bug = bug
        
    def mostrar_nome(self):
        return "Nome do desenvolvedor: %s"%self.nome
    
    def mostrar_idade(self):
        return "Idade do desenvolvedor: %s"%self.idade
    
    def mostrar_linguagem(self):
        return "Liguagem de programacao favorita é python e %s"%self.linguagem
    
    def achou_ou_n(self):
        pergunta = input("Achou o bug?? [s/n]").lower()
        if pergunta == "s":
            print("Achou o %s"%self.bug)
        else: 
            print("Nao achou o bug, mas o programa funciona? [s/n]")
            pergunta2 = input(":").lower()
            if pergunta2 == "s":
                print("Nem voce sabe como esta funcionando né kkkkkkkkkk")
            else:
                print("É uma pena.")
                
i = desenvolvedor("Vitor", "19", "JAVA", "ERROR")
print(i.mostrar_nome())
print(i.mostrar_idade())
print(i.mostrar_linguagem())
i.achou_ou_n()