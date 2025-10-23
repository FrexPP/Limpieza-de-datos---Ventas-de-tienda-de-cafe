# Creo un Gráfico que muestra de mayor a menor en rentabilidad los 8 productos de la cafetería:

productos_rentables = df.groupby("Item")["Total Spent"].sum()
# Ordeno la Serie de mayor a menor.
productos_ordenados = productos_rentables.sort_values(ascending=False)

productos_ordenados.plot(
    kind="bar",
    figsize=[11,8],
    color=["#1f77b4","#ff7f0e","#2ca02c","#d62728","#9467bd","#8c564b","#e377c2","#7f7f7f"]
)
plt.grid(True, linestyle="--", axis="y",color="black")
plt.title("Products for profitability (Productos por rentabilidad)")
plt.xlabel("")
plt.xticks(rotation=45)
plt.show()