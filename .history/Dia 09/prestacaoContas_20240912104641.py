import pandas as pd
import numpy as np

sales_df = pd.read_excel("D:\\www\\codiacademy\\Dia 09\\Sales.xlsx")
sales_df_total_sales = sales_df["Valor Final"]

average_sales = "{:.2f}".format(np.mean(sales_df_total_sales))
median = "{:.2f}".format(np.median(sales_df_total_sales))
standard_deviation = "{:.2f}".format(np.std(sales_df_total_sales, ddof=1))
maximum = "{:.2f}".format(np.max(sales_df_total_sales))
minimum = "{:.2f}".format(np.min(sales_df_total_sales))

print(f"Média de vendas: {mean}")
print(f"Mediana sobre vendas: {median}")
print(f"Desvio padrão das vendas: {standard_deviation}")
print(f"Valor maxímo de vendas: {maximum}")
print(f"Valor minimo de vendas: {minimum}")
