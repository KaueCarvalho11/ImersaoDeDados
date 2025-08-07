# Importando biblioteca para análise de dados

import pandas as pd

# Conteúdo de df será a base de dados
df = pd.read_csv(r"C:\Users\kauec\Downloads\salaries.csv") # r indica que a string é 'raw'(crua), evitando a interpretação de caracteres especiais

# Por padrão, traz o conteúdo das 5 primeiras linhas (0 à 4)
print(df.head())

# Especificação da quantidade de linhas que serão apresentadas
print(df.head(10))

# Apresentar estrutura da tabela
print(df.info())

# Descrição estatística da base de dados/ feita com base nos valores numéricos
print(df.describe())

# Dimensão da base de dados (Linhas, colunas)
print(df.shape)

linhas, colunas = df.shape[0], df.shape[1]

print("Quantidade de linhas: ", linhas)

print("Quantidade de colunas: ", colunas)

# Apresentar colunas da base de dados
print(df.columns)

# Dicionário de tradução das colunas
traducao_colunas = {
    "work_year": "ano",
    "experience_level": "senioridade",
    "employment_type": "contrato",
    "job_title": "cargo",
    "salary": "salario",
    "salary_currency": "moeda_salario",
    "salary_in_usd": "salario_em_usd",
    "employee_residence": "residencia_funcionario",
    "remote_ratio": "remoto",
    "company_location": "localizacao_empresa",
    "company_size": "tamanho_empresa"
}

# Renomeando as colunas
df = df.rename(columns=traducao_colunas)

# Apresentar colunas traduzidas
print(df.columns)

# Exibir contagem dos dados da coluna especificada
print(df["senioridade"].value_counts())
print(df["contrato"].value_counts())
print(df["cargo"].value_counts())

senioridade = {
    'SE': 'Senior',
    'MI': 'Pleno',
    'EN': 'Junior',
    'EX': 'Executivo'
}

# Renomeando categorias da coluna "senioridade"
df["senioridade"] = df["senioridade"].replace(senioridade)
print(df["senioridade"].value_counts)

contrato = {
    'FT': 'Integral',
    'PT': 'Parcial',
    'FL': 'Freelance',
    'CT': 'Contrato'
}

df['contrato'] = df['contrato'].replace(contrato)
print(df["contrato"].value_counts())

tamanho_empresa = {
    'S': 'Pequena', 
    'M': 'Media',
    'L': 'Grande'
}

df["tamanho_empresa"] = df["tamanho_empresa"].replace(tamanho_empresa)
print(df["tamanho_empresa"].value_counts())

remoto = {
    0: 'Presencial',
    50: 'Hibrido',
    100: 'Remoto'
}

df["remoto"] = df["remoto"].replace(remoto)
print(df["remoto"].value_counts())

print(df.head(100))

# Descrição dos dados categóricos
print(df.describe(include="object"))

# Descrição dos dados numéricos
print(df.describe())

def carregar_dados():
    return df