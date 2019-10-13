import pandas as pd
# %%    URL DOS DADOS DO BANCO CENTRAL
url_ibc = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.24364/dados?formato=json&dataInicial=1/1/1500'
url_mult = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1654/dados?formato=json&dataInicial=1/1/1500'

# %%  IMPORTANDO OS DATAFRAMES
ibc = pd.read_json(url_ibc)
mult = pd.read_json(url_mult)
# %% LIMPANDO E ESTRUTURANDO OS DADOS
valores_mult = mult['valor']
ibc['mult'] = valores_mult
data = pd.to_datetime(ibc['data'],format='%d/%m/%Y')
ibc.index = data
ibc = ibc.drop(columns = ['data'])
df = ibc
df.columns = ['ibc','multiplicador']
# %% ENCONTRANDO MATRIZ DE CORRELAÇÃO
correlation_matrix = df.corr()
print(correlation_matrix)
