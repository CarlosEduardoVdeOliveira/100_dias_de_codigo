import pandas as pd

df = pd.read_csv(r"d:\\www\\codiacademy\\Dia 09\\sales.csv", encoding='ISO-8859-1', error_bad_lines=False)
  # ou 'latin1'
df = pd.read_csv(r"d:\\www\\codiacademy\\Dia 09\\sales.csv", encoding='ISO-8859-1', on_bad_lines='skip')

print(df.head())
#print(df.iloc["Total_sales", 3])
