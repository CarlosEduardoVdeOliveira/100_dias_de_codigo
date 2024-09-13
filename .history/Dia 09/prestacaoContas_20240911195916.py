import pandas as pd

df = pd.read_excel("sales.xlsx")

print(df.iloc[3, 2])
