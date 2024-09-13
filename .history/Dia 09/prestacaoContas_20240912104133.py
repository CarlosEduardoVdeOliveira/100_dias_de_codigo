import pandas as pd
import numpy as np

sales_df = pd.read_excel("D:\\www\\codiacademy\\Dia 09\\Sales.xlsx")
sales_df_total_sales = sales_df["Valor Final"]

mean = np.mean(sales_df_total_sales)
median = np.median(sales_df_total_sales)
standard_deviation = np.std(sales_df_total_sales, ddof=1)
maximum = np.max(sales_df_total_sales)
minimum = np.min(sales_df_total_sales)

print({mean})
print(median)
print(standard_deviation)
print(maximum)
print(minimum)
