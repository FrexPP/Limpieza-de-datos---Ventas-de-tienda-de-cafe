# Agregando los últimos datos deducibles:

# El total gastado se puede sacar multiplicando el precio del producto por la cantidad de unidades.
df.loc[df["Total Spent"].isna(),"Total Spent"] = (df["Quantity"] * df["Price Per Unit"])
# La cantidad de unidades se puede sacar dividiendo el total gastado por el precio de unidad.
df.loc[df["Quantity"].isna(),"Quantity"] = (df["Total Spent"] / df["Price Per Unit"])