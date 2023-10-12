import pandas as pd
import pyodbc

# Leer el archivo CSV
df = pd.read_csv('data.csv')

# Renombrar las columnas para que coincidan con la tabla "Charges"
df.rename(columns={
    'id': 'id',
    'name': 'company_name',
    'company_id': 'company_id',
    'amount': 'amount',
    'status': 'status',
    'created_at': 'created_at',
    'paid_at ': 'updated_at'  # paid_at trae un espacio en blanco 
}, inplace=True)

# Conexión con la base de datos SQL Server
connection_string = 'DRIVER={SQL Server};SERVER=LAPTOP-3CFPHETV;DATABASE=PB_NEXT;Trusted_Connection=yes'

# Redondear los valores en la columna 'amount' a dos decimales y convertir a FLOAT
df['amount'] = df['amount'].apply(lambda x: round(float(x), 2))

try:
    conn = pyodbc.connect(connection_string)
except pyodbc.Error as e:
    print("Error al conectar a la base de datos:", e)
    exit()

def convert_date(date_str):
    try:
        if date_str.strip():  # Verificar si la cadena no está vacía
            return pd.to_datetime(date_str, format='%Y-%m-%d', errors='coerce')
        else:
            return None 
    except:
        return None


# Aplicar la función de conversión a las columnas 'created_at' y 'updated_at'
df['created_at'] = df['created_at'].apply(convert_date)
df['updated_at'] = df['updated_at'].apply(convert_date)

# Validar y asignar un valor por defecto a las fechas nulas
df['created_at'].fillna(0, inplace=True)
df['updated_at'].fillna(0, inplace=True)



# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Uso de transacciones
try:
    conn.autocommit = False  # Desactivar la confirmación automática

    # Insertar los datos en la tabla "Charges" de SQL Server
    for index, row in df.iterrows():
        if not pd.isna(row['id']):
            insert_charge_query = "INSERT INTO charges ([id], [company_id], [amount], [status], [created_at], [updated_at]) " \
                "VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(insert_charge_query, str(row['id']), str(row['company_id']), float(row['amount']), str(row['status']), row['created_at'], row['updated_at'])
            print(f"Insertado: {row['id']}")  # Mensaje de depuración
        else:
            print(f"ID nulo en fila {index}. No se insertó el registro.")

    conn.commit()  # Confirmar los cambios
    print("Inserción exitosa")

except pyodbc.Error as e:
    conn.rollback()  # En caso de error, deshacer la transacción
    print("Error al insertar datos en la tabla Charges:", e)

finally:
    conn.autocommit = True  # Restaurar la confirmación automática

# Cerrar la conexión 
conn.close()