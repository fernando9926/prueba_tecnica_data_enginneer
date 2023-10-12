# prueba_tecnica_data_enginneer
El objetivo principal del proyecto es cargar, extraer y transformar datos de un conjunto de datos proporcionado de una prueba técnica de Data Engineer.

Nota: puedes saltarte los pasos y cargar directamente el script llamado "next.sql" pero se recomienda leerlos para tener una nocion de lo que se realizo.

## 1.1 Carga de Información en SQL Server

En esta sección, se describe el proceso de carga de la información proporcionada en el conjunto de datos en una base de datos SQL Server. 

### Instrucciones

1. **Configuración de SQL Server:**
   - Asegúrate de tener una instancia de SQL Server configurada y funcionando.

2. **Creación de la Base de Datos:**
   - Crea una nueva base de datos en SQL Server. Puedes hacerlo a través de SQL Server Management Studio.

3. **Selección de SQL Server:**
    - Por la familiaridad con SQL Server entre los miembros del equipo. La elección de la base de datos puede depender de las herramientas disponibles y de las necesidades específicas del proyecto.

4. **Carga de Datos:**
   - Para cargar los datos del conjunto proporcionado en la base de datos SQL Server. Puedes emplear SQL Server Integration Services (SSIS), para cargar el csv llamado "data_prueba_tecnica".

## 1.2 Extracción de Datos

En esta sección, se detalla el proceso de extracción de datos desde la base de datos SQL Server y la posterior transformación de los datos. Además, se describe por qué se eligió Python como lenguaje de programación y el formato CSV para la extracción.

### Instrucciones

1. **Python como Lenguaje de Extracción:**
   - Para extraer los datos, se eligió Python como lenguaje de programación. Debido a que es utilizado en tareas de extracción y transformación de datos debido a su versatilidad y la disponibilidad de bibliotecas como `pyodbc` que permiten conectarse a bases de datos SQL Server entre otras razones porque el equipo de trabajo se siente comodo usandolo.

2. **Formato de Salida: CSV**
   - El formato de salida elegido para la extracción de datos fue CSV. CSV es un formato ampliamente compatible que facilita la importación y exportación de datos en una variedad de aplicaciones. La elección de este formato fue para facilitar la interoperabilidad con otras herramientas y sistemas.

3. **Script de Extracción:**
   - El script utilizado para la extracción de datos se llama "extraction.py"

## 1.3 Transformacion de datos y 1.4 Dispersion de la informacion

En esta sección, se detalla el proceso de transformación de los datos para que cumplan con el esquema propuesto Y el proceso de dispersión de la información en una base de datos Microsoft SQL Server. Se crea un esquema estructurado con dos tablas relacionadas, "charges" y "companies." Además, se debe incluir un diagrama de la base de datos resultante.

### Instrucciones

1. **Transformaciones Requeridas:**
    - El esquema propuesto para la información incluye columnas con tipos de datos específicos, como "varchar," "decimal," y " timestamp." El conjunto de datos extraído puede no cumplir con estos tipos de datos, por lo que es necesario realizar transformaciones.
    - El script utilizado se llama "transform.py". este scrypt tambien carga los datos en 2 tablas "charges" y "companies"
2. **Explicacion de Transformaciones:**
    * El script renombra las columnas del DataFrame para que coincidan con la estructura propuesta de la tabla "Charges" y "companies" en SQL Server.
    * Redondea los valores en la columna 'amount' a dos decimales y los convierte al tipo de dato FLOAT.
    *Aplica una función de conversión de fecha a las columnas 'created_at' y 'updated_at' para garantizar que tengan el formato correcto
3. **Desafios:**
    * Se enfrentaron algunos desafíos notables. Uno de los desafíos principales fue lidiar con la duplicación de la clave primaria "id" en los datos. El conjunto de datos original contenía duplicados en la columna "id," lo que presentaba un problema al cargar los datos en la base de datos. Para resolver esto, se implementaron estrategias de deduplicación, como eliminar filas duplicadas.
    * Otro desafío fue establecer una conexión efectiva con la base de datos SQL Server para cargar los datos en las tablas "charges" y "companies." La conexión requería configuración adecuada, autenticación y permisos. Asegurarse de que la conexión se estableciera correctamente fue fundamental para el éxito de la carga.
4. **Creación de Tablas y Relaciones:**
    - Para dispersar la información, se deben crear dos tablas en la base de datos SQL Server: "charges" para la información de las transacciones y "companies" para la información de las compañías. Estas dos tablas deben estar relacionadas a través de una clave (company_id).
5. **Script de Creación de Tablas:**
    - El script utilizado para la creacion de ambas tablas fue el siguiente: 
    CREATE TABLE companies (
    company_id VARCHAR(50) PRIMARY KEY,
    company_name VARCHAR(130) NOT NULL
    );

CREATE TABLE charges (
    id VARCHAR(50) PRIMARY KEY NOT NULL,
    company_id VARCHAR(50) NOT NULL,
    amount DECIMAL(16, 2) NOT NULL,
    status VARCHAR(30) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME,
    FOREIGN KEY (company_id) REFERENCES companies (company_id)
    );
6. **Diagrama de base de datos:**
    - Al ya estar relacionadas las tablas "charges" y "companies", SSMS nos da la opcion de crear un diagrama con las tablas seleccionadas. Al seleccionar estas 2 nos arroja ambas tablas con su relacion a traves de "company_id". Esto proporciona una visualización clara de la disposición de los datos.

## 1.5 SQL
Se describe el proceso de diseño de una vista en la base de datos para mostrar el monto total transaccionado por día para las diferentes compañías. Además, se proporciona el script SQL utilizado para crear la vista.

### Instrucciones

1. **Diseño de la Vista:**
    - El objetivo es diseñar una vista que muestre el monto total transaccionado por día para las diferentes compañías. Esto permite una fácil consulta y análisis de los datos agregados.
2. **SCRIPT:**
    - CREATE VIEW monto_total_por_dia AS
SELECT
    c.company_name,
    c.company_id,
    CAST(CONVERT(VARCHAR(10), ch.created_at, 120) AS DATE) AS transaction_date,
    SUM(ch.amount) AS total_amount
FROM
    companies c
JOIN
    charges ch ON c.company_id = ch.company_id
GROUP BY
    c.company_id,
    c.company_name,
    CAST(CONVERT(VARCHAR(10), ch.created_at, 120) AS DATE);
3. **Explicación:**
    - La vista "monto_total_por_dia" se crea mediante una consulta SQL que combina datos de las tablas "companies" y "charges" utilizando una operación JOIN. Luego, se agrupan los resultados por "company_id," "company_name" y "transaction_date," y se calcula la suma total de "amount" para cada grupo.

