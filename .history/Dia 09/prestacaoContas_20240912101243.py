import pandas as pd

df = pd.read_excel(r"d:\\www\\codiacademy\\Dia 09\\Vendas.xlsx")  # ou 'latin1'

print(df.iloc[3, 3])
