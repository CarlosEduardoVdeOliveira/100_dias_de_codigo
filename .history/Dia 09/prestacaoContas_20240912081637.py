import pandas as pd

df = pd.read_csv(r"d:\\www\\codiacademy\\Dia 09\\sales.csv", encoding='ISO-8859-1', error_bad_lines=False)
  # ou 'latin1'

print(df.iloc[Total_sales, 3])
