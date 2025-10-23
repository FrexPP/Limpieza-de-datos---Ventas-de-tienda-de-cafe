# Creo un gráfico que muestre el total recaudado por mes:

asignar_indice_fecha = df.set_index("Transaction Date")
ingreso_mes = asignar_indice_fecha.resample("M")["Total Spent"].sum()
# Convierto la fecha a string y dejo únicamente el año y el mes, para poder mostrar el total por mes.
ingreso_mes.index = ingreso_mes.index.strftime("%Y-%m")

ingreso_mes.plot(
    kind="line",
    figsize=[13,8],
    color="green",
    marker="o"
)
plt.xticks(ticks=range(12),labels=ingreso_mes.index,rotation=45)
plt.xlabel("")
plt.grid(True,linestyle="--",axis="y",color="black")
plt.title("Sales by month of 2023 (Ventas por meses de 2023)")
plt.show()
