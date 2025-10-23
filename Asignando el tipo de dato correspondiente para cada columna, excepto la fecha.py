# Asignando el tipo de dato correspondiente para cada columna, excepto la fecha:

# Para recuperar los demás datos recuperables, necesito convertir los tipos de datos de las columnas correspondientes-
# en datos que se puedan utilizar con operadores aritméticos. (La fecha aún no la incluyo, porque al haber datos nulos lanza un error.) 
df = df.astype({
    "Transaction ID" : "string",
    "Item" : "string",
    "Quantity" : "Int64",
    "Price Per Unit" : "Float64",
    "Total Spent" : "Float64",
    "Payment Method" : "string",
    "Location" : "string",
    })