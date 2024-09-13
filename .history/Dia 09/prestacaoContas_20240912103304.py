import pandas as pd
import numpy as np

df = pd.read_excel("D:\\www\\codiacademy\\Dia 09\\Sales.xlsx")
media = np.mean(df["Valor Final"])
mediana = np.median(df["Valor Final"])
desvio_padrao = np.std(df["Valor Final"], ddof=1)  # Desvio Padrão com NumPy (ddof=1 para correção)
maximo = np.max(df["Valor Final"])           # Valor Máximo com NumPy
minimo = np.min(df["Valor Final"])  
print(media)
