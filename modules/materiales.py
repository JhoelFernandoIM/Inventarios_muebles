import streamlit as st
from db.conexion import conectar_db

def modulo_materiales():
    st.header("Gestión de Materiales")

    nombre = st.text_input("Nombre del material")
    categoria = st.text_input("Categoría")
    unidad = st.text_input("Unidad de medida")
    stock = st.number_input("Stock inicial", min_value=0)

    if st.button("Registrar material"):
        conn = conectar_db()
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO materiales
            (nombre_material, categoria, unidad_medida, stock_actual)
            VALUES (%s, %s, %s, %s)
            """,
            (nombre, categoria, unidad, stock)
        )
        conn.commit()
        conn.close()
        st.success("Material registrado correctamente")

    st.subheader("Listado de materiales")

    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM materiales")
    datos = cur.fetchall()
    conn.close()

    st.table(datos)
