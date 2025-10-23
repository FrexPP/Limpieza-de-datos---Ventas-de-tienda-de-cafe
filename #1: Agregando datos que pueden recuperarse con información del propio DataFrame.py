# Agregando datos que pueden recuperarse con información del propio DataFrame:

# Noté que podía rellenar los valores nulos de los productos y su precio haciendo un "mapa" de todos los productos y sus precios.
productos_completos = df[["Item","Price Per Unit"]].drop_duplicates().dropna()

# Creo un diccionario de Python con el cual podremos acceder a los productos por su precio y viceversa.
mapa_precio = dict(zip(productos_completos["Item"],productos_completos["Price Per Unit"]))
mapa_producto = dict(zip(productos_completos["Price Per Unit"],productos_completos["Item"]))

# Agrego los datos al DataFrame donde: si dice el producto pero no su precio individual, le agrego su precio correspondiente.
df.loc[df["Price Per Unit"].isna(), "Price Per Unit"] = (df.loc[df["Price Per Unit"].isna(), "Item"].map(mapa_precio))
df.loc[df["Item"].isna(), "Item"] = (df.loc[df["Item"].isna(), "Price Per Unit"].map(mapa_producto))

# Como después quedaron unas pocas filas donde no había producto ni precio, lo elimino al no haber forma de recuperar dicha información.
df = df.dropna(subset=["Item","Price Per Unit"], how="all")
