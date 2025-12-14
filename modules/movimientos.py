import streamlit as st
from db.conexion import conectar_db

def modulo_movimientos():
    st.header("Movimientos de Inventario")

    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("SELECT id_material, nombre_material FROM materiales")
    materiales = cur.fetchall()

    material = st.selectbox("Material", materiales)
    tipo = st.selectbox("Tipo de movimiento", ["ENTRADA", "SALIDA"])
    cantidad = st.number_input("Cantidad", min_value=1)
    obs = st.text_area("Observación")

    if st.button("Registrar movimiento"):
        cur.execute(
            """
            INSERT INTO movimientos
            (id_material, tipo_movimiento, cantidad, observacion)
            VALUES (%s, %s, %s, %s)
            """,
            (material[0], tipo, cantidad, obs)
        )

        if tipo == "ENTRADA":
            cur.execute(
                "UPDATE materiales SET stock_actual = stock_actual + %s WHERE id_material = %s",
                (cantidad, material[0])
            )
        else:
            cur.execute(
                "UPDATE materiales SET stock_actual = stock_actual - %s WHERE id_material = %s",
                (cantidad, material[0])
            )

        conn.commit()
        st.success("Movimiento registrado")

    conn.close()
