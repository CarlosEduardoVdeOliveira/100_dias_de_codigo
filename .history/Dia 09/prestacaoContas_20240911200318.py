import pandas as pd

df = pd.DataFrame.to_csv("sales.csv")

print(df.iloc[3, 3])
