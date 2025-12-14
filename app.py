import streamlit as st
from modules.materiales import modulo_materiales
from modules.movimientos import modulo_movimientos
from modules.reportes import modulo_reportes

st.set_page_config(page_title="Módulo de Inventarios", layout="wide")

st.title("ERP – Módulo de Control de Inventarios")

menu = st.sidebar.selectbox(
    "Seleccione una opción",
    ["Materiales", "Movimientos", "Reportes"]
)

if menu == "Materiales":
    modulo_materiales()
elif menu == "Movimientos":
    modulo_movimientos()
elif menu == "Reportes":
    modulo_reportes()
