import pandas as pd

# Carrega o arquivo Excel (certifique-se de que o arquivo 'sales.xlsx' está no mesmo diretório)
df = pd.read_excel("sales.xlsx")

# Acessa o primeiro elemento do DataFrame corretamente
print(df.iloc[0, 0])
