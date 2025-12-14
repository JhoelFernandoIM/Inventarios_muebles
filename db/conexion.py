import psycopg2

def conectar_db():
    conexion = psycopg2.connect(
        host="db.nulrfxommxyhpgvsweri.supabase.co",
        database="postgres",
        user="postgres",
        password="FREEdos",
        port="5432"
    )
    return conexion
