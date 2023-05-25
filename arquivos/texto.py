print("Selecione 1 para adicionar o nome e codigo, ou 2 para pesquisar o codigo e nome.")

opcao = int(input(">:"))

if opcao == 1:
    arquivo= open("C:/Users/vitor/Documents/GitHub/Python-and-HTLM/python/arquivos/informacoes.txt", "a")
    conteudo = arquivo
    informacao = conteudo.split(",")
    nome = (input("nome:"))
    codigo = (input("codigo:"))
    idade = (input("idade:"))
    arquivo.writelines(f"\n{conteudo}")
    arquivo.close

elif opcao == 2:
    arquivo = open("C:/Users/vitor/Documents/GitHub/Python-and-HTLM/python/arquivos/informacoes.txt", "r")
    pesquisar = input("Pesquise aqui [>")
    for linha in arquivo:
        if pesquisar in linha:
            print(linha)
        arquivo.close
    
    