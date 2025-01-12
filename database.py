import psycopg2

#coneccion a la base de datos PostgreSQL

conn = psycopg2.connect(host="localhost", dbname ="postgres", user="postgres", password="usertest123", port=5432)

#cursor 
cur = conn.cursor()

#hacer query 

cur.execute("""CREATE TABLE IF NOT EXISTS GasolinaData (
            id SERIAL PRIMARY KEY,
            zonas_geografica_nombre VARCHAR(50),
            marca_nombre VARCHAR(50),
            combustible_precio DECIMAL
            );
            """)

with open('GasolinaData.csv', 'r') as f:
    next(f)
    cur.copy_from(f, 'gasolinadata', sep=',', columns=('zonas_geografica_nombre', 'marca_nombre','combustible_precio'))

conn.commit()

cur.close()
conn.close()