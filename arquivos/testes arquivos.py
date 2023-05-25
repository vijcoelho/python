arquivo= open("C:/Users/vitor/Documents/GitHub/Python-and-HTLM/python/arquivos/informacoes.txt", "r")
arquivo.close
primeira_linha = arquivo.readline().split()
arquivo.close()
nome = primeira_linha[0]
print(nome)
    