# Importación de librerías y solucionar problema principal:

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/franf/OneDrive/Desktop/dirty_cafe_sales.csv")
df.info()
df
# Después de examinar el DataFrame noté que tenía valores nulos en 7 de las 8 columnas.
# También había varios valores como "ERROR" y "UNKNOWN", así que transformé tales valores en nulos.
df.replace(["ERROR","UNKNOWN","NaN","<NA>"],pd.NA,inplace=True)
# Elimino filas duplicadas.
df.drop_duplicates(inplace=True)

"""
Ver resultado de df.info():
[Haz clic aquí para ver la imagen](https://github.com/FrexPP/Limpieza-de-datos---Ventas-de-tienda-de-cafe/blob/main/image.png)
"""
