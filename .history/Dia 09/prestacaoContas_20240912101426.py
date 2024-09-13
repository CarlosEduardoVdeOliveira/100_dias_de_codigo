import pandas as pd

df = pd.read_excel("Vendas.xlsx")  # ou 'latin1'

print(df.head(10))
