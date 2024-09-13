import pandas as pd

df = pd.read_csv("sales.xlsx")

print(df.iloc[3, 3])
