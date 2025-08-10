import pandas as pd

# Biblioteca para manipulação de dados numéricos
import numpy as np

# Criando base de dados manualmente
df = pd.DataFrame({
    'nome': ['Kaue', 'Jean', 'Erick', 'Foguete'],
    'salario': [1500, np.nan, 4000, np.nan] # Atribuindo valores nulos a determinados registros
})

# Cria coluna 'salario_media', onde serão mantidos os valores originais dos salários não nulos, e, para salários nulos, será atribuido a média dos salários
df['salario_media'] = df['salario'].fillna(df['salario'].mean())
print(df.head())

# Criar coluna 'salario_mediada', onde serão mantidos os valores originais dos salários não nulos, e, para salários nulos, será atribuida a mediada dos salários
df['salario_mediana'] = df['salario'].fillna(df['salario'].median())
print(df.head())
