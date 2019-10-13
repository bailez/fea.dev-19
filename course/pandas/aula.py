"""
AULA PANDAS -- CURSO FEA.DEV
Felipe Bailez

Pandas é uma biblioteca que trabalha com series temporais e Dataframes,
nesta aula iremos aprender como criar series e dataframes
"""
import pandas as pd
import numpy as np

# %%Criaremos a principio uma lista de numeros aleatorios utilizando numpy
lista_aleatoria = np.random.rand(12)

# %%Para criar uma Serie é simples, utilizamos o comando pd.Series() e passamos a lista
serie = pd.Series(lista_aleatoria)
print(serie)

# %%Podemos renomear a Serie e seu indice
serie.name = 'Inflação'
serie.index.name = 'Date'

# %%Utilizando o formato datetime criaremos uma lista de periodos para associar ao indice
comprimento_da_serie = len(serie)
lista_de_datas = pd.date_range(start='01/01/2019',freq='M',periods=comprimento_da_serie)
serie.index = lista_de_datas
print(serie)
"""
Note que pd.date_range() possui varios argumentos, start é a data inicial, 
freq é a frequencia do dado, ou seja, mensal, diario, trimestral. E periods é o 
numero de periodos que o dado ocorre
"""
# %% Encontrando vairação percentual mes-contra-mes e media movel de 3 meses
mom = serie.pct_change()
mom.name = 'Variacao percentual' #famosa segunda derivada
mavg = serie.pct_change(3)
mavg.name = 'Media móvel 3 meses'
print(mom,'\n',mavg)
# %% Criando dataframe
"""
Existem varias formas de se criar dataframes, podemos utilizar numpy arrays,
combinação de listas e de series. Vamos utilizar as variações para montar nosso dataframe
"""
df = pd.DataFrame(data=[serie,mom,mavg])
print(df)
df = df.T #Assim como numpy podemos transpor dataframes para fazer a data voltar ao indice
print(df)

# %% Filtrando dados com dataframes

df_jan = df[df.index == '2019-01-31']
df_jun_dez = df['2019-06':]
df_var_neg = df[df['Variacao percentual'] < 0]
serie_var_neg = df_var_neg['Inflação']

# %% Operações com dataframes e series

soma = mavg + mom
sub = soma - mavg
print(sub == mom)
mult = df*5