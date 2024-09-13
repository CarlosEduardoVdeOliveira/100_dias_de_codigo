import pandas as pd
import numpy as np

df = pd.read_excel("D:\\www\\codiacademy\\Dia 09\\Sales.xlsx")
media = np.mean(df['vendas'])
print(df["Valor Final"])
