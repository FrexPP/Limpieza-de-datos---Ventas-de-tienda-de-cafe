# Limpieza de valores sin salvación:

# Como aún pueden haber unos pocos valores nulos, elimino las filas sobrantes donde-
# cantidad, gasto total o fecha son nulos. 
df.dropna(subset=["Quantity","Total Spent","Transaction Date"], inplace=True)
# Y como ya se eiminaron todos los valores nulos de la fecha de transacción, puedo convertir dicha columna en formato fecha.
df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])
