import pandas as pd
import numpy as np

# Gerando um DataFrame de exemplo com dados de vendas aleatórios
np.random.seed(0)
dados_vendas = {
  'vendas': np.random.randint(100, 1000, size=20)  # Gerando 20 valores de vendas entre 100 e 1000
}

df = pd.(dados_vendas)

# Calculando as estatísticas
media = df['vendas'].mean()
mediana = df['vendas'].median()
desvio_padrao = df['vendas'].std()
maximo = df['vendas'].max()
minimo = df['vendas'].min()

print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Desvio padrao: {desvio_padrao}")
print(f"maximo: {maximo}")
print(f"minimo: {minimo}")

