import pandas as pd
import numpy as np

df = pd.DataFrame({
    'nome': ['Kaue', 'Erick', 'Jean', 'Foguete'],
    'cidade': ['Martins', np.nan, 'Pau dos Ferros', np.nan]
})

df['cidade_preenchida'] = df['cidade'].fillna("Não informado")
print(df)