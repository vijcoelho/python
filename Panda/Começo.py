import pandas as pd
pd.Series(data=5)

lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()
print(f'\n{pd.Series(lista_nomes)}')

dados = {
    'nome1': 'Howard',
    'nome2': 'Ian',
    'nome3': 'Peter',
    'nome4': 'Jonah',
    'nome5': 'Kellie',
}

print(f'\n{pd.Series(dados)}')

cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
print(f'\n{pd.Series(lista_nomes, index=cpfs)}')

series_dados = pd.Series(lista_nomes, index=cpfs)
print('\n')
print(series_dados.loc['111.111.111-11'])
print('\n')

series_dados = pd.Series([10.2, -1, None, 15, 23.4])
print('Quantidade de linhas = ', series_dados.shape) # Retorna uma tupla com o número de linhas
print('Tipo de dados', series_dados.dtypes) # Retorna o tipo de dados, se for misto será object
print('Os valores são únicos?', series_dados.is_unique) # Verifica se os valores são únicos (sem duplicações)
print('Existem valores nulos?', series_dados.hasnans) # Verifica se existem valores nulos
print('Quantos valores existem?', series_dados.count()) # Conta quantas valores existem (excluí os nulos)

print('Qual o menor valor?', series_dados.min()) # Extrai o menor valor da Series (nesse caso os dados precisam ser do mesmo tipo)
print('Qual o maior valor?', series_dados.max()) # Extrai o valor máximo, com a mesma condição do mínimo
print('Qual a média aritmética?', series_dados.mean()) # Extrai a média aritmética de uma Series numérica
print('Qual o desvio padrão?', series_dados.std()) # Extrai o desvio padrão de uma Series numérica
print('Qual a mediana?', series_dados.median()) # Extrai a mediana de uma Series numérica

print('\nResumo:\n', series_dados.describe()) # Exibe um resumo sobre os dados na Series

lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()
lista_cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
lista_emails = 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split()
lista_idades = [32, 22, 25, 29, 38]
print(pd.DataFrame(lista_nomes, columns=['nome'], index=lista_cpfs))
print('\n')

dados = list(zip(lista_nomes, lista_cpfs, lista_idades, lista_emails))
print(pd.DataFrame(dados, columns=['nome', 'cpfs', 'idade', 'email']))
print('\n') #SEMPRE TENTAR FAZER ESTE

dados = {
    'nomes': 'Howard Ian Peter Jonah Kellie'.split(),
    'cpfs' : '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split(),
    'emails' : 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split(),
    'idades' : [32, 22, 25, 29, 38]
}

df_dados = pd.DataFrame(dados)

df_uma_coluna = df_dados['idades']
print(type(df_uma_coluna))
print('Média de idades = ', df_uma_coluna.mean())
print(df_uma_coluna)

colunas = ['nomes', 'cpfs']
df_duas_colunas = df_dados[colunas]
print(type(df_duas_colunas))
print(df_duas_colunas)
