import pandas as pd
import numpy as np

df = pd.DataFrame({
    'dia': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'],
    'Temperatura': [30, np.nan, np.nan, 28, 27]
})

# ffill = foward fill/ Valores não nulos: Preenche com o valor da temperatura correspondente; Valores nulos: Preenche com valor da temperatura do registro anterior
df['preenchido_ffill'] = df['Temperatura'].ffill()
print(df)

# bfill = back fill/ valores não nulos: Preenche com o valor da temperatura correspondente; Valores nulos: Preenche com ovalor da temperatura do registro posterior
df['preenchido_bfill'] = df['Temperatura'].bfill()
print(df)