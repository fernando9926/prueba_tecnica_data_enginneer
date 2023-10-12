import pyodbc
import csv

#conexión a la base de datos SQL Server
connection_string = 'DRIVER={SQL Server};SERVER=LAPTOP-3CFPHETV;DATABASE=PB_NEXT;Trusted_Connection=yes'
conn = pyodbc.connect(connection_string)

# Crea un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Ejecuta la consulta SQL para obtener los datos
sql_query = "SELECT * FROM [PB_NEXT].[dbo].[data_prueba_tecnica]"
cursor.execute(sql_query)

#resultados de la consulta
result = cursor.fetchall()

#Archivo CSV de salida
csv_file = "data.csv"

# Escribe resultados en un archivo CSV
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([column[0] for column in cursor.description])  # Escribir encabezados de columna
    writer.writerows(result)

# Cierra la conexión a la base de datos
conn.close()
