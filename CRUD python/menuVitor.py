cores = {'limpa':'\033[m', 
        'vermelho':'\033[31m', 
        'verde':'\033[32m', 
        'amarelo':'\033[33m', 
        'azul':'\033[34m', 
        'roxo':'\033[35m', 
        'azulclaro':'\033[36m', 
        'cinza':'\033[37m'}

def mostraMenu ():
    #Escolher qual voce quiser..
    print('{}\t\t=================================={}'.format(cores['vermelho'], cores['limpa']))
    print('{}\t\t|        .1 NOVO cadastro        |{}'.format(cores['azul'], cores['limpa']))
    print('{}\t\t|        .2 ALTERAÇÃO            |{}'.format(cores['azul'], cores['limpa']))
    print('{}\t\t|        .3 DELETAR cadastro     |{}'.format(cores['azul'], cores['limpa']))  
    print('{}\t\t|        .4 PESQUISAR            |{}'.format(cores['azul'], cores['limpa']))
    print('{}\t\t|        .0 SAIR DO PROGRAMA     |{}'.format(cores['azul'], cores['limpa']))
    print('{}\t\t=================================={}'.format(cores['vermelho'], cores['limpa']))

def op1():
    global codigo
    global identidade 
    # Incluir um novo cadastro: Abre o arquivo e pede para colocar o Nome , Idade e um Codigo. Depois de colocar essas 
    # informaçoes sao armazenadas dentro do arquivo que foi aberto.          
    with open("C:/Users/vitor/Documents/GitHub/python/CRUD python/informacoes.txt", "a") as arquivo:
            nome = (input('{}Nome: {}'.format(cores['amarelo'], cores['limpa'])))
            idade = (input('{}Idade: {}'.format(cores['amarelo'], cores['limpa'])))
            codigo =(input('{}Código: {}'.format(cores['amarelo'], cores['limpa'])))
            identidade = nome, idade , codigo
            arquivo.writelines(f"\n{identidade}")

def op2 ():
    # Alterar um cadastro: Agora o arquivo é aberto no modo de leitura e escrita e se pede o codigo que foi colocado para fazer a pesquisa
    # da pessoa. Fazendo a pesquisa dentro do arquivo e mostrando o nome e idade, depois pergunta se quer mudar o nome
    # caso queira ele ira mostrar um campo para digitar o nome e assim poder trocar.
    with open("C:/Users/vitor/Documents/GitHub/python/CRUD python/informacoes.txt", "r+")as arquivo:
        pesquisa = input('{}\t\tInsira o código para pesquisar a pessoa:{}'.format(cores['roxo'], cores['limpa']))
        for linha in arquivo:
            if pesquisa in linha:
                identidade = linha.split(",") # Sera responsavel por dividir a linha
                nome = identidade[0].strip("('") # Ira retirar o ( '
                idade = identidade[1].strip(" ('") # Ira retirar o ( ' 
                print(f"Este é seu nome e idade {nome} e {idade}.")
                continuar = input('{}Mudar Nome? [s/n]: {}'.format(cores['azulclaro'], cores['limpa']))
                if continuar == "s":
                    nomenovo = input('{}Novo Nome: {}'.format(cores['azulclaro'], cores['limpa']))
                    identidade = linha.replace(nome, nomenovo)
                    arquivo.writelines(f"\n{identidade}")
        
def op3():
    global nome
    global idade
    global codigo
    # Deletar um cadastro: O arquivo tambem é aberto no modo de leitura e escrita, depois se pede para inserir o codigo da pessoa
    # para a pesquisa. Quando achar ele ira perguntar se deseja realmente remover, caso queira ele ira excluir do arquivo.
    with open("C:/Users/vitor/Documents/GitHub/python/CRUD python/informacoes.txt", "r+") as arquivo:
        pesquisa = input('{}\t\tInsira o código para pesquisar a pessoa:{}'.format(cores['roxo'], cores['limpa']))
        linhas = arquivo.readlines()
        encontrada = False
        for i, linha in enumerate(linhas):
            if pesquisa in linha:
                encontrada = True
                identidade = linha.split(",") # Sera responsavel por dividir a linha
                nome = identidade[0].strip("('") # Ira retirar o ( ' 
                idade = identidade[1].strip(" ('") # Ira retirar o ( ' 
                codigo = identidade[2]
                deletar = input(f"Atualmente seu cadastro é {nome} {idade} {codigo}. Deseja deletar seu cadastro? [s/n] : ")
                if deletar == 's':
                    linhas.pop(i)
                    arquivo.seek(0)
                    arquivo.writelines(linhas)
                    arquivo.truncate()
                    print('{}Cadastro excluído com sucesso!{}'.format(cores['vermelho'], cores['limpa']))
                else:
                    print("--Voltar ao Inicio--")
        if not encontrada:
            print('{}Cadastro não encontrado.{}'.format(cores['vermelho'], cores['limpa']))

def op4 ():
    global nome
    global idade
    global codigo
    # Pesquisar um cadastro: O arquivo tambem é aberto no modo de leitura e escrita, depois se pede para inserir o codigo da pessoa
    # para a pesquisa. Quando achar ele ira mostrar o nome e a idade da pessoa pesquisada.
    with open("C:/Users/vitor/Documents/GitHub/python/CRUD python/informacoes.txt", "r+") as arquivo:
        pesquisa = input('{}\t\tInsira o código para pesquisar a pessoa:{}'.format(cores['roxo'], cores['limpa']))
        for linha in arquivo:
            if pesquisa in linha:
                identidade = linha.split(",") # Sera responsavel por dividir a linha
                nome = identidade[0].strip("('") # Ira retirar o ( ' 
                idade = identidade[1].strip(" ('") # Ira retirar o ( ' 
                codigo = identidade[2].strip(" ('") # Ira retirar o ( ' 
                print(f"{nome} {idade}")
                                             
while (True):
    mostraMenu ()
    opcao = int(input('\n\tDIGITE SUA OPÇÃO:{}'.format(cores['roxo'], cores['limpa'])))
    if (opcao == 0): break
        
    if opcao == 1:    
        op1()
    elif opcao == 2:    
        op2()
    elif opcao == 3:    
        op3()
    elif opcao == 4:    
        op4()

