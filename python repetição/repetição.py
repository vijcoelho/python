opcao=0
print ("\tOPERAÇÕES DISPONIVEIS")
print ("")
print ("1. Listar Alunos")
print ("2. Incluir Aluno")
print ("3. Sair")
print ("")

opcao=0
while opcao<1 or opcao>3:
        opcao=int(input("Digite a opção desejada:"))
        if opcao<1 or opcao>3:
            print("Opção não existe")

print ("\n\n")
if (opcao==1):
        print("Listar Dados")
elif (opcao==2):
        print("Incluir Aluno")
elif (opcao==3):
        print("TCHAU")