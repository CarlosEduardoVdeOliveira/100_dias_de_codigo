import pandas as pd
import numpy as np

sales_df = pd.read_excel("D:\\www\\codiacademy\\Dia 09\\Sales.xlsx")
sales_df_total_sales = df["Valor Final"]
media = np.mean()
mediana = np.median(df["Valor Final"])
desvio_padrao = np.std(df["Valor Final"], ddof=1)
maximo = np.max(df["Valor Final"])
minimo = np.min(df["Valor Final"])

print(media)
print(mediana)
print(desvio_padrao)
print(maximo)
print(minimo)
