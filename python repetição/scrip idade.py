import os

def mostraIntroducao ():
    os.system ('cls')
    print ("\n\tEste scrip vai coletar dados de um grupo de pessoas")
    print ("\n\tQuantas pessoas tem mais de 18 anos ")
    print ("\n\tQuantas pessoas tem menos de 18 anos ")
    print ("\n\tQuantas homens tem mais de 18 anos ")

def mostraResultados ():
    os.system ('cls')
    print ("\t\t*****RESULTADO DA PESQUISA*****")
    print (f"\n\tPessoas com mais de 18 anos. : {qtosmaior18}")
    print (f"\n\tPessoas consultadas......... : {qtaspessoas}")
    print (f"\n\tPessoas com menos de 18 anos : {qtosmenor18}")
    print (f"\n\tPessoas com 18 anos......... : {qtostem18}")
    print (f"\n\t\t\tMasculino: {qtosmaior18H}")
    
    

def formataResposta (resp):
    resp = resp.upper() #upper maiusculo #lower minusculo
    resp = resp[0]
    return resp
#-------COMEÇA AQUI------------------------------------------------------

qtosmaior18 = 0
qtaspessoas = 0
qtosmenor18 =0
qtostem18 = 0
qtosmaior18H = 0

mostraIntroducao()
while (True):
    os.system ('cls')
    print ("\n\tDigite os dados da pessoa....")
    print ("\n\tIdade 0 para parar o programa")
    idade = int(input("\n\tIdade: "))
    if (idade == 0):
        break
    sexo = formataResposta (input("\tSexo (M/F): "))
    
    qtaspessoas = qtaspessoas + 1

    if (idade > 18):
        qtosmaior18 = qtosmaior18 + 1
        if (sexo == "M"):
            qtosmaior18H = qtosmaior18H + 1
    
    elif (idade < 18):
        qtosmenor18 = qtosmenor18 + 1

mostraResultados()

qtostem18 = qtaspessoas - qtosmaior18 - qtosmenor18
