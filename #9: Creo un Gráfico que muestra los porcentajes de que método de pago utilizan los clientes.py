# Creo un Gráfico que muestra los porcentajes de que método de pago utilizan los clientes:

# Lamentablemente, el 31,55% de filas del método de pago eran nulas.
ingreso_metodo = df.groupby("Payment Method")["Payment Method"].count()

ingreso_metodo.plot(
    kind="pie",
    autopct="%1.2f%%",
    figsize=[8,8],
    fontsize=15
)
plt.ylabel("")

plt.title("Comparison of payment methods (Comparación métodos de pago)")
