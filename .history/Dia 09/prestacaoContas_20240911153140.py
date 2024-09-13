import pandas as pd

# Carrega o arquivo Excel (certifique-se de que o arquivo 'sales.xlsx' está no mesmo diretório)
df = pd.read_excel("sales.xlsx")

print(df.iloc[0, 0])
