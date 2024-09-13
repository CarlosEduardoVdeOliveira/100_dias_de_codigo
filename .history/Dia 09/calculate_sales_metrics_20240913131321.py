import pandas as pd
import numpy as np

data = {
    "sales"': [1531.99, 2399.99, 1818.32, 1221.50, 1950, 2430.36, 1538.81, 1552.56]
}

sales_df =  pd.DataFrame(data)

mean_sales = np.mean(sales_df["sales"])
median_sales = np.median(sales_df["sales"])
standard_deviation_on_sales = np.std(sales_df["sales"])
max_sales = np.max(sales_df["sales"])
min_sales = np.min(sales_df["sales"])

print(f"Média das vendas: R$ {mean_sales}")
print(f"Mediana das vendas: R$ {median_sales}")
print(f"Desvio padrão das vendas: R$ {standard_deviation_on_sales}")
print(f"Maior valor de venda: R$ {max_sales}")
print(f"Menor valor de venda: R$ {min_sales}")
