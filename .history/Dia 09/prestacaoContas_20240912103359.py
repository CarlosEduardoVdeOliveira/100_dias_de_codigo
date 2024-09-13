import pandas as pd
import numpy as np

df = pd.read_excel("Sales.xlsx")
media = np.mean(df["Valor Final"])
mediana = np.median(df["Valor Final"])
desvio_padrao = np.std(df["Valor Final"], ddof=1)
maximo = np.max(df["Valor Final"])
minimo = np.min(df["Valor Final"])
print(media
mediana
desvio_padrao
maximo
minimo)
