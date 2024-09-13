import pandas as pd
import numpy as np

#sales_df = pd.read_excel("Sales.xlsx")
#sales_df_total_sales = sales_df["Valor Final"]

data = {
    'sales': [1531.99, 2399.99, 1818.32, 1221.50, 1950, 2430.36, 1538.81, 1552.56]
}

sales_df =  pd.DataFrame(data)

mean_sales = "{:.2f}".format(np.mean(sales_))
median_sales = "{:.2f}".format(np.median(sales_))
standard_deviation_on_sales = "{:.2f}".format(np.std(sales_, ddof=1))
max_sales = "{:.2f}".format(np.max(sales_))
min_sales = "{:.2f}".format(np.min(sales_))

print(f"Média das vendas: R$ {mean_sales}")
print(f"Mediana das vendas: R$ {median_sales}")
print(f"Desvio padrão das vendas: R$ {standard_deviation_on_sales}")
print(f"Maior valor de venda: R$ {max_sales}")
print(f"Menor valor de venda: R$ {min_sales}")
