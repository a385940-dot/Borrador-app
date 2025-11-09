import streamlit as st

# Configuración de la página (título, ícono)
st.set_page_config(
    page_title="Guardianes del Agua MX",
    page_icon="💧"
)

# Título principal
st.title("Guardianes del agua💧")

# Introducción
st.write(
    """
    ¡Bienvenido a la aplicación sobre el cuidado del agua en México!
    
    Navega por las diferentes secciones usando el menú de la izquierda para
    encontrar estadísticas, consejos prácticos y un juego interactivo.
    """
)

# Imagen de portada (opcional, puedes cambiar la URL)
st.image(
    "https://img.freepik.com/vector-gratis/dibujado-mano-ilustracion-dibujos-animados-gota-agua_52683-140083.jpg?semt=ais_hybrid&w=740&q=80",
    caption="El agua es un recurso vital que debemos proteger."
)

st.sidebar.success("Selecciona una sección arriba.")
