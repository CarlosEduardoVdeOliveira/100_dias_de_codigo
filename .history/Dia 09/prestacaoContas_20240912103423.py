import pandas as pd
import numpy as np

df = pd.read_excel("Sales.xlsx")
media = np.mean(df["Valor Final"])

print(media)
