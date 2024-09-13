import pandas as pd

df = pd.read_excel("sales.xlsx", sheet_name="nome_da_planilha")

print(df.iloc[0, 0])
