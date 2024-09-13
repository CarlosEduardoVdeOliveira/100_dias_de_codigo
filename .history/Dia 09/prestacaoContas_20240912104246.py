import pandas as pd
import numpy as np

sales_df = pd.read_excel("D:\\www\\codiacademy\\Dia 09\\Sales.xlsx")
sales_df_total_sales = sales_df["Valor Final"]

mean = "{:.2f}".format(np.mean(sales_df_total_sales)
median = "{:.2f}".format(np.median(sales_df_total_sales)
standard_deviation = "{:.2f}".format(np.std(sales_df_total_sales, ddof=1)
maximum = "{:.2f}".format(np.max(sales_df_total_sales)
minimum = "{:.2f}".format(np.min(sales_df_total_sales)

print(f"{mean}")
print(f"{median}")
print(f"{standard_deviation}")
print(f"{maximum}")
print(f"{minimum}")
