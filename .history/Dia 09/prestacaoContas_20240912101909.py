import pandas as pd

df = pd.read_excel("Vendas.xlsx", on_bad_lines='skip')

print(df.describe())
