import pandas as pd

df = pd.read_excel(r"d:\www\codiacademy\Dia 09\sales.csv", encoding='ISO-8859-1')
print(vendas_df)

display(vendas_df)
print(df.iloc[3, 3])
