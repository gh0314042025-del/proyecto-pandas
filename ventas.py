import pandas as pd

datos ={
    
    "producto": ["Televisor", "Celular","Laptop" ,"Tablet", "Audifonos " ] , 
    "ventas":[150, 200, 250, 300, 100],
    "precio":[750, 650, 900, 400, 120],
    
    
}

df = pd.DataFrame(datos)
print("datos cargados correctamente")
print(df)

html_tabla =df.to_html(index=False)
estadisticas = df.describe().to_html()

html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Datos de Ventas</title>
</head>
<body>
    <h2>Datos de Ventas</h2>
    <h3>Tabla de Datos:</h3>
    {html_tabla}
    <h3>Estadísticas Descriptivas:</h3>
    {estadisticas}
</body>
</html>
"""

with open("tabla.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Archivo 'tabla.html' creado correctamente ")