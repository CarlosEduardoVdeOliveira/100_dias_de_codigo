import pandas as pd
import numpy as np

sales_df = pd.read_excel("D:\\www\\codiacademy\\Dia 09\\Sales.xlsx")
sales_df_total_sales = sales_df["Valor Final"]

media = np.mean(sales_df_total_sales)
mediana = np.median(sales_df_total_sales)
desvio_padrao = np.std(sales_df_total_sales, ddof=1)
maximo = np.max(sales_df_total_sales)
minimo = np.min(sales_df_total_sales)

print(media)
print(mediana)
print(desvio_padrao)
print(maximo)
print(minimo)
