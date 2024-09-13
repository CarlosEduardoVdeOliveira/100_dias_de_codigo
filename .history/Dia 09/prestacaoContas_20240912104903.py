import pandas as pd
import numpy as np

sales_df = pd.read_excel("D:\\www\\codiacademy\\Dia 09\\Sales.xlsx")
sales_df_total_sales = sales_df["Valor Final"]

average_sales = "{:.2f}".format(np.mean(sales_df_total_sales))
median_sales = "{:.2f}".format(np.median(sales_df_total_sales))
standard_deviation_on_sales = "{:.2f}".format(np.std(sales_df_total_sales, ddof=1))
maximum_number_of_sales = "{:.2f}".format(np.max(sales_df_total_sales))
minimum = "{:.2f}".format(np.min(sales_df_total_sales))

print(f"Média de vendas: {average_sales}")
print(f"Mediana sobre vendas: {median_sales}")
print(f"Desvio padrão das vendas: {standard_deviation_on_sales}")
print(f"Valor máximo de vendas: {maximum_number_of_sales}")
print(f"Valor minimo de vendas: {minimum}")
