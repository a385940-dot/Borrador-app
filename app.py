import streamlit as st

# Configuración de la página (título, ícono)
st.set_page_config(
    page_title="Guardianes del Agua MX",
    page_icon="💧"
)

# Título principal
st.title("Proyecto: Guardianes del Agua en México 💧")

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
    "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepik.es%2Ffotos-vectores-gratis%2Fdibujos-animados-agua&psig=AOvVaw3svrSmSVR_gklTONXyo8bN&ust=1762814084456000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCLDd9ayQ5pADFQAAAAAdAAAAABAE",
    caption="El agua es un recurso vital que debemos proteger."
)

st.sidebar.success("Selecciona una sección arriba.")
