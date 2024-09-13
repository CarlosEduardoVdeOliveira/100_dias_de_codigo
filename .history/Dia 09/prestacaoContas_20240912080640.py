import pandas as pd
import numpy as np

# Gerando um DataFrame de exemplo com dados de vendas aleatórios
np.random.seed(0)
dados_vendas = {
  'vendas': np.random.randint(100, 1000, size=20)  # Gerando 20 valores de vendas entre 100 e 1000
}

df = pd.read_csv("sales.csv")

# Calculando as estatísticas
media = df['Total_Sales'].mean()
mediana = df['Total_Sales'].median()
desvio_padrao = df['Total_Sales'].std()
maximo = df['Total_Sales'].max()
minimo = df['Total_Sales'].min()

print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Desvio padrao: {desvio_padrao}")
print(f"maximo: {maximo}")
print(f"minimo: {minimo}")

