import streamlit as st

st.title("Juego: 🔎 Mito o Verdad sobre el Agua")

# --- Usamos st.session_state ---
if 'pregunta_actual_mito' not in st.session_state:
    st.session_state.pregunta_actual_mito = 0
    st.session_state.puntuacion_mito = 0

# --- NUEVO: Estado para bloquear la respuesta ---
if 'estado_juego_mito' not in st.session_state:
    st.session_state.estado_juego_mito = "preguntando" # "preguntando" o "respondido"

if 'respuesta_usuario_mito' not in st.session_state:
    st.session_state.respuesta_usuario_mito = None # "Mito" o "Verdad"

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
    st.session_state.estado_juego_mito = "preguntando"
    st.session_state.respuesta_usuario_mito = None

# --- Lógica del Juego ---
num_pregunta = st.session_state.pregunta_actual_mito

if num_pregunta < len(mitos_y_verdades):
    item = mitos_y_verdades[num_pregunta]
    
    st.subheader(item["afirmacion"])
    
    # --- LÓGICA DE BOTONES SEPARADA ---
    
    if st.session_state.estado_juego_mito == "preguntando":
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Es Mito", key=f"m_{num_pregunta}", use_container_width=True):
                st.session_state.respuesta_usuario_mito = "Mito"
                st.session_state.estado_juego_mito = "respondido"
                if item["respuesta"] == "Mito":
                    st.session_state.puntuacion_mito += 1
                st.rerun()

        with col2:
            if st.button("Es Verdad", key=f"v_{num_pregunta}", use_container_width=True):
                st.session_state.respuesta_usuario_mito = "Verdad"
                st.session_state.estado_juego_mito = "respondido"
                if item["respuesta"] == "Verdad":
                    st.session_state.puntuacion_mito += 1
                st.rerun()
                
    elif st.session_state.estado_juego_mito == "respondido":
        # Deshabilitamos los botones (solo visual, ya no se muestran)
        # y mostramos la retroalimentación
        
        if st.session_state.respuesta_usuario_mito == item["respuesta"]:
            st.success(item["explicacion"])
        else:
            st.error(f"Incorrecto. La respuesta era: {item['respuesta']}. {item['explicacion']}")
        
        # --- Mostramos el botón para avanzar ---
        if st.button("Siguiente Afirmación"):
            st.session_state.pregunta_actual_mito += 1
            st.session_state.estado_juego_mito = "preguntando"
            st.session_state.respuesta_usuario_mito = None
            st.rerun()

else:
    # --- FIN DEL JUEGO ---
    st.header("¡Terminaste el juego de Mitos y Verdades!")
    st.write(f"Tu puntuación fue: {st.session_state.puntuacion_mito} de {len(mitos_y_verdades)}")
    st.balloons()

    st.divider() 
    st.header("Repaso de Mitos y Verdades")
    
    for item in mitos_y_verdades:
        st.markdown(f"**Afirmación:** {item['afirmacion']}")
        if item["respuesta"] == "Verdad":
            st.success("Respuesta: VERDAD")
        else:
            st.error("Respuesta: MITO")
        st.write(item["explicacion"]) 
        st.caption("---") 

    st.divider()
    
    if st.button("Volver a Jugar"):
        reiniciar_juego_mito()
        st.rerun()

# Mostramos la puntuación en la barra lateral
st.sidebar.write(f"Puntuación Mitos: {st.session_state.puntuacion_mito}")
