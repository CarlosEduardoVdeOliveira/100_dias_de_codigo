import pandas as pd

df = pd.read_csv(r"D:\\www\\codiacademy\\Dia 09\\sales.csv", encoding='ISO-8859-1')  # ou 'latin1'

print(df.iloc[3, 3])
