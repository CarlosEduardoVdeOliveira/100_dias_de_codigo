import pandas as pd

df = pd.read_("Vendas.xlsx", encoding='ISO-8859-1', on_bad_lines='skip')

print(df.describe())
