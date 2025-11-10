import streamlit as st

st.title("Juego: 🌎 Calcula tu Huella Hídrica")

st.write("Descubre cuánta agua (aproximadamente) usas en tu día a día. ¡Los resultados te sorprenderán!")

# --- Usamos st.session_state para guardar el total ---
if 'total_litros' not in st.session_state:
    st.session_state.total_litros = 0

# Factores de gasto (litros) - ¡puedes ajustarlos!
LITROS_POR_MINUTO_DUCHA = 10
LITROS_POR_DESCARGA_WC = 6
LITROS_POR_LAVADO_MANOS = 3
LITROS_POR_LAVADO_TRASTES = 15 # (dejando la llave abierta)
LITROS_POR_LAVADORA = 60

# --- Entradas del Usuario ---

# 1. Ducha (st.slider)
st.subheader("🚿 En el Baño")
minutos_ducha = st.slider(
    "¿Cuántos minutos te bañas al día?", 
    min_value=0, 
    max_value=60, 
    value=10
)
gasto_ducha = minutos_ducha * LITROS_POR_MINUTO_DUCHA

# 2. WC (st.number_input)
descargas_wc = st.number_input(
    "¿Cuántas veces usas el WC al día?",
    min_value=0,
    max_value=20,
    value=5
)
gasto_wc = descargas_wc * LITROS_POR_DESCARGA_WC

# 3. Lavado de manos (st.number_input)
lavados_manos = st.number_input(
    "¿Cuántas veces te lavas las manos al día?",
    min_value=0,
    max_value=30,
    value=8
)
gasto_manos = lavados_manos * LITROS_POR_LAVADO_MANOS


# --- Cocina y Ropa ---
st.subheader("🍽️ En la Cocina y Lavandería")

# 4. Trastes (st.radio)
lavado_trastes = st.radio(
    "Al lavar los trastes, ¿cómo lo haces?",
    ["Cierro la llave al enjabonar", "Dejo la llave abierta"]
)
gasto_trastes = 0 if lavado_trastes == "Cierro la llave al enjabonar" else LITROS_POR_LAVADO_TRASTES * 3 # 3 veces al día

# 5. Lavadora (st.number_input)
cargas_lavadora = st.number_input(
    "¿Cuántas cargas de lavadora pones A LA SEMANA?",
    min_value=0,
    max_value=10,
    value=2
)
# Dividimos entre 7 para sacar el promedio diario
gasto_lavadora = (cargas_lavadora * LITROS_POR_LAVADORA) / 7


# --- Botón de Cálculo ---
if st.button("Calcular mi Huella Hídrica Diaria"):
    
    total = gasto_ducha + gasto_wc + gasto_manos + gasto_trastes + gasto_lavadora
    st.session_state.total_litros = total
    
    # Usamos st.metric para un resultado vistoso
    st.metric(
        label="Tu Consumo Diario Aproximado es:",
        value=f"{total:.1f} Litros"
    )
    
    # Damos retroalimentación
    if total < 100:
        st.success("¡Excelente! Eres un verdadero Guardián del Agua. 💧")
    elif total < 250:
        st.info("¡Vas bien! Pero aún puedes mejorar. Revisa los consejos.")
    else:
        st.warning("¡Cuidado! Tu consumo es alto. Pequeños cambios pueden hacer una gran diferencia.")

st.caption("Valores basados en estimaciones. El consumo real puede variar.")

