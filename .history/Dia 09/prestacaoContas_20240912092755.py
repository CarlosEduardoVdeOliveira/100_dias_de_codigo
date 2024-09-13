import pandas as pd

vendas_df = pd.read_excel(r"sales.xlsx")
print(vendas_df)

display(vendas_df)
print(vendas_df.iloc[3, 3])
