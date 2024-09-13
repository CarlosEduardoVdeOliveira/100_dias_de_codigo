import pandas as pd
import numpy as np

df = pd.read_excel("D:\\www\\codiacademy\\Dia 09\\Sales.xlsx")
media = np.mean(df['Valor Final'])
mediana = np.median(df['vendas'])
desvio_padrao = np.std(df['vendas'], ddof=1)  # Desvio Padrão com NumPy (ddof=1 para correção)
maximo = np.max(df['vendas'])           # Valor Máximo com NumPy
minimo = np.min(df['vendas'])  
print(media)
