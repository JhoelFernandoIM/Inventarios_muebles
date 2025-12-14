import streamlit as st
from db.conexion import conectar_db

def modulo_reportes():
    st.header("Reporte de Inventarios")

    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT nombre_material, stock_actual, stock_minimo
        FROM materiales
    """)
    datos = cur.fetchall()
    conn.close()

    st.table(datos)
