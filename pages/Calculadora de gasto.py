import streamlit as st

st.title("Juego: Calcula tu gasto diario 💦")

st.write("Descubre aproximadamente cuánta agua usas en tu día a día")

if 'total_litros' not in st.session_state:
    st.session_state.total_litros = 0

LITROS_POR_MINUTO_DUCHA = 10
LITROS_POR_DESCARGA_INODORO = 6
LITROS_POR_LAVADO_MANOS = 3
LITROS_POR_LAVADO_TRASTES = 15 
LITROS_POR_LAVADORA = 60

st.subheader("En el Baño🚿")
minutos_ducha = st.slider("¿Cuántos minutos duras bañandote al día?", 
    min_value=0, 
    max_value=60, 
    value=10)
gasto_ducha = minutos_ducha * LITROS_POR_MINUTO_DUCHA

descargas_inodoro = st.number_input("¿Cuántas veces usas el inodoro al día?",
    min_value=0,
    max_value=20,
    value=5)
gasto_inodoro = descargas_inodoro * LITROS_POR_DESCARGA_INODORO

lavados_manos = st.number_input("¿Cuántas veces te lavas las manos al día?",
    min_value=0,
    max_value=30,
    value=8)
gasto_manos = lavados_manos * LITROS_POR_LAVADO_MANOS

st.subheader("En la cocina y lavandería🍽️")

lavado_trastes = st.radio("Al lavar los trastes, ¿cómo lo haces?",["Cierro la llave al enjabonar", "Dejo la llave abierta"])
gasto_trastes = 0 if lavado_trastes == "Cierro la llave al enjabonar" else LITROS_POR_LAVADO_TRASTES * 3 
cargas_lavadora = st.number_input("¿Cuántas cargas de lavadora pones a la semana?",
    min_value=0,
    max_value=10,
    value=2)
gasto_lavadora = (cargas_lavadora * LITROS_POR_LAVADORA) / 7

if st.button("Calcular mi gasto diario💦"):
    
    total = gasto_ducha + gasto_inodoro + gasto_manos + gasto_trastes + gasto_lavadora
    st.session_state.total_litros = total
    
    st.metric(label="Tu gasto diario aproximado es:",
        value=f"{total:.1f} Litros")
    
    
    if total < 100:
        st.success("¡Excelente!, estas cuidando el agua")
    elif total < 250:
        st.info("¡Vas bien! Pero aún puedes reducir tu gasto")
    else:
        st.warning("¡Mal! Tu consumo es alto")
