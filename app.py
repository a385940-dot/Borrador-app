import streamlit as st

st.set_page_config(page_title="Guardianes del Agua",page_icon="💧")

st.title("Cada Gota Cuenta")

st.write("""¿Cuánto sabes sobre el cuidado del agua?
Navega por las diferentes secciones que tenemos para ti usando el menú de la izquierda para encontrar estadísticas, consejos prácticos y juegos interactivos.

Esperemos que la aplicación sea de tu agrado :)""")

st.image("https://img.freepik.com/vector-gratis/dibujado-mano-ilustracion-dibujos-animados-gota-agua_52683-140083.jpg?semt=ais_hybrid&w=740&q=80",
    caption="El agua es un recurso vital que debemos proteger.")

st.sidebar.success("Selecciona una sección arriba.")
