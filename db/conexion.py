import streamlit as st
from supabase import create_client, Client

# Verifica si estamos usando Streamlit Cloud (usando Secrets)
if "SUPABASE_URL" in st.secrets:
    SUPABASE_URL = st.secrets["SUPABASE_URL"]
    SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
else:
    st.error("No se encontraron las credenciales de Supabase en Streamlit Secrets.")
    st.stop()

# Crear el cliente de Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Verificar que la conexión se realizó correctamente
try:
    # Obtener todos los materiales (ejemplo de consulta)
    data = supabase.table("materiales").select("*").execute()
    st.write("Conexión exitosa a Supabase")
    st.write(data.data)  # Muestra los datos obtenidos

except Exception as e:
    st.error(f"Error al conectar con Supabase: {e}")
