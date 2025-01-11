import psycopg2

#coneccion a la base de datos PostgreSQL

conn = psycopg2.connect(host="localhost", dbname ="", user="", password="", port=5432)

#cursor 
cur = conn.cursor()

#hacer query 

cur.execute("""CREATE TABLE IF NOT EXISTS person (
            
            id SERIAL PRIMARY KEY,
            name VARCHAR(45),
            age INT

            );
            """)


conn.commit()

cur.close()
conn.close()