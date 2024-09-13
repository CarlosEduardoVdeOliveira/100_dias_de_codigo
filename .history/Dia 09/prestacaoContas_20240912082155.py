import pandas as pd
import numpy as np

data = {
    'vendas': [150, 200, 500, 200, 400, 900, 400, 100, 700, 300]
}

df = pd.DataFrame(data)

# Cálculos usando pandas e numpy
media = df['vendas'].mean()             # Média
mediana = df['vendas'].median()         # Mediana
desvio_padrao = df['vendas'].std()      # Desvio Padrão
maximo = df['vendas'].max()             # Valor Máximo
minimo = df['vendas'].min()             # Valor Mínimo

# Exibindo os resultados
print(f"Média: {media}")
print(f"Mediana: {mediana}")
print(f"Desvio Padrão: {desvio_padrao}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")

