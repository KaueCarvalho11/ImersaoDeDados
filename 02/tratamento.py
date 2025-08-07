# Permite importação de arquivos Python de outras pastas
from sys import path 

# Adicionando caminho para a busca por diretórios
path.append('../IMERSAODEDADOS/01')

# Importando função que retorna a base de dados criada no outro arquivo
from programa import carregar_dados

df = carregar_dados()
print(df.head())

# Retorna base de dados com indicativo se registro é nulo ou não
print(df.isnull())

# Retorna somatório da quantidade de valores nulos de cada campo
print(df.isnull().sum())

# Retorna de maneira única (não duplicada) os valores que o campo 'ano' assume na base de dados
print(df['ano'].unique())

# Retorna todas as linhas da base de dados que possuem pelo menos um valor nulo em qualquer coluna
print(df[df.isnull().any(axis = 1)])

# dropna() exclui valores nulos do campos
df_limpo = df.dropna()
print(df_limpo.isnull().sum())
 
# Modificando tipo de dado do campo 'ano'
df_limpo = df_limpo.assign(ano = df_limpo['ano'].astype('int64'))
print(df_limpo.info())
print(df_limpo.head())

def carregar_df_limpo():
    return df_limpo