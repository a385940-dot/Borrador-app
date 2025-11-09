import streamlit as st

st.title("Juego: 🔎 Mito o Verdad sobre el Agua")

# --- Usamos st.session_state ---
if 'pregunta_actual_mito' not in st.session_state:
    st.session_state.pregunta_actual_mito = 0
    st.session_state.puntuacion_mito = 0

# Lista de afirmaciones
mitos_y_verdades = [
    {
        "afirmacion": "Mito o Verdad: El agua embotellada es siempre más segura que el agua del grifo.",
        "respuesta": "Mito",
        "explicacion": "¡Mito! En muchas ciudades de México la calidad del agua de la red es monitoreada constantemente, mientras que el agua embotellada no siempre cumple todos los estándares y además genera muchísimo plástico."
    },
    {
        "afirmacion": "Mito o Verdad: Lavar el coche con manguera gasta más de 300 litros de agua.",
        "respuesta": "Verdad",
        "explicacion": "¡Verdad! Usar la manguera puede gastar hasta 500 litros. Usar una cubeta y esponja gasta solo unos 50 litros."
    },
    {
        "afirmacion": "Mito o Verdad: Hervir el agua elimina los metales pesados (como el plomo).",
        "respuesta": "Mito",
        "explicacion": "¡Mito! Hervir el agua solo mata gérmenes (bacterias, virus). No elimina metales pesados, flúor o sales. Para eso se necesita un filtro."
    },
    {
        "afirmacion": "Mito o Verdad: Se necesita más agua para producir 1kg de carne de res que 1kg de verduras.",
        "respuesta": "Verdad",
        "explicacion": "¡Verdad! Se estima que producir 1kg de carne de res requiere unos 15,000 litros de agua (contando el riego del alimento para el animal), mientras que 1kg de maíz requiere unos 1,200 litros."
    }
]

# Función para reiniciar
def reiniciar_juego_mito():
    st.session_state.pregunta_actual_mito = 0
    st.session_state.puntuacion_mito = 0

# --- Lógica del Juego ---
num_pregunta = st.session_state.pregunta_actual_mito

if num_pregunta < len(mitos_y_verdades):
    item = mitos_y_verdades[num_pregunta]
    
    st.subheader(item["afirmacion"])
    
    # Usamos st.columns para poner los botones uno al lado del otro
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Es Mito", key=f"m_{num_pregunta}", use_container_width=True):
            if item["respuesta"] == "Mito":
                st.success(item["explicacion"])
                st.session_state.puntuacion_mito += 1
            else:
                st.error(f"Incorrecto. {item['explicacion']}")
            st.session_state.pregunta_actual_mito += 1
            st.rerun()

    with col2:
        if st.button("Es Verdad", key=f"v_{num_pregunta}", use_container_width=True):
            if item["respuesta"] == "Verdad":
                st.success(item["explicacion"])
                st.session_state.puntuacion_mito += 1
            else:
                st.error(f"Incorrecto. {item['explicacion']}")
            st.session_state.pregunta_actual_mito += 1
            st.rerun()

else:
    # Fin del juego
    st.header("¡Terminaste el juego de Mitos y Verdades!")
    st.write(f"Tu puntuación fue: {st.session_state.puntuacion_mito} de {len(mitos_y_verdades)}")
    st.balloons()
    
    if st.button("Volver a Jugar"):
        reiniciar_juego_mito()
        st.rerun()

# Mostramos la puntuación en la barra lateral
st.sidebar.write(f"Puntuación Mitos: {st.session_state.puntuacion_mito}")
