import psycopg2

db = psycopg2.connect(
    database="users", 
    user="postgres", 
    password="rootroot", 
    host="localhost", 
    port="5432"
)
