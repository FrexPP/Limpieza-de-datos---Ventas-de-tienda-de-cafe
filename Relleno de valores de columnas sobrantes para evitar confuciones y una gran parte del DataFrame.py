# Relleno de valores de columnas sobrantes para evitar confuciones y una gran parte del DataFrame:

# Como el método de pago y la ubicación tienen muchos valores nulos, preferí cambiarlos-
# a "NO ESPECIFICADO", para no perder una gran parte del DataFrame. 
df["Payment Method"].fillna("NOT SPICIFIED",inplace=True)
df["Location"].fillna("NOT SPICIFIED",inplace=True)
# La limpieza de datos concluyó con 9469 filas limpias de las 10000 que tenía, lo cual supone el 94,69% del total,
# una muestra muy sólida para análisis.
df.info()