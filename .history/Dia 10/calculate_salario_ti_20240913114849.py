import pandas as pd
import numpy as np

dados = {
    'nomes': ['Alice', 'Bob', 'Carlos', 'Diana', 'Eva'],
    'departamento': ['TI', 'RH', 'TI', 'Marketing', 'TI'],
    'salario': [5000, 4000, 6000, 4500, 5500]
}

df = pd.DataFrame(dados)

# Filtrar os funcionários do departamento "TI"
df_ti = df[df['departamento'] == 'TI']

# Calcular a média salarial dos funcionários de TI
media_salarial_ti = np.mean(df_ti['salario'])

print(f"A média salarial do departamento de TI é: {media_salarial_ti:.2f}")
