import pandas as pd
import numpy as np

dados = {
    'nomes': ['Ana', 'João', 'Lucas', 'Maria', 'Eva', "Adão", "Carlos"],
    'departamento': ['TI', 'RH', 'TI', 'Marketing', 'RH', "TI", "TI"],
    'salario': [15_000, 3_000, 6_700, 4_500, 5_500, 3_500, 4_500]
}

df = pd.DataFrame(dados)

df_ti = df[df['departamento'] == 'TI']

media_salarial_ti = np.mean(df_ti['salario'])

print(f"A média salarial do departamento de TI é: {media_salarial_ti:.2f}")
