import pandas as pd
import numpy as np

# Exemplo de DataFrame
data = {
    'vendas': [1500, 2300, 5000, 1200, 3400, 2900, 4100, 1800, 2700]
}

df = pd.DataFrame(data)

# Cálculos usando pandas e numpy
media = np.mean(df['vendas'])           # Média com NumPy
mediana = np.median(df['vendas'])       # Mediana com NumPy
desvio_padrao = np.std(df['vendas'], ddof=1)  # Desvio Padrão com NumPy (ddof=1 para correção)
maximo = np.max(df['vendas'])           # Valor Máximo com NumPy
minimo = np.min(df['vendas'])           # Valor Mínimo com NumPy

# Exibindo os resultados
print(f"Média: {media}")
print(f"Mediana: {mediana}")
print(f"Desvio Padrão: {desvio_padrao}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")
