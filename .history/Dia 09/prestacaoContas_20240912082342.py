import pandas as pd
import numpy as np

data = {
    'vendas': [150, 200, 500, 200, 400, 900, 400, 100, 700, 300]
}

df = pd.DataFrame(data)

media = df['vendas'].mean()
mediana = df['vendas'].median()
desvio_padrao = df['vendas'].std()
maximo = df['vendas'].max()
minimo = df['vendas'].min()

print(f"Média: {media}")
print(f"Mediana: {mediana}")
print(f"Desvio Padrão: {desvio_padrao}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")

