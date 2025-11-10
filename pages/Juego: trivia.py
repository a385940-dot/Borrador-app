import streamlit as st

st.title("Juego: Trivia del Agua 💧")

if 'puntuacion_trivia' not in st.session_state:
    st.session_state.puntuacion_trivia = 0
    
if 'pregunta_actual_trivia' not in st.session_state:
    st.session_state.pregunta_actual_trivia = 0

if 'estado_juego_trivia' not in st.session_state:
    st.session_state.estado_juego_trivia = "preguntando" 
    
if 'respuesta_usuario_trivia' not in st.session_state:
    st.session_state.respuesta_usuario_trivia = None


# Preguntas
preguntas = [
    {
        "pregunta": "¿Qué porcentaje del agua del planeta es dulce (no salada)?",
        "opciones": ["25%", "10%", "2.5%"],
        "correcta": "2.5%",
        "explicacion": "¡Correcto! Solo el 2.5% es agua dulce, y la mayoría está en glaciares."
    },
    {
        "pregunta": "¿Cuántos litros de agua gasta una ducha de 10 minutos aproximadamente?",
        "opciones": ["50 litros", "100 litros", "200 litros"],
        "correcta": "200 litros",
        "explicacion": "¡Correcto! Una regadera común gasta unos 20 litros por minuto."
    },
    {
        "pregunta": "¿Cuál es la principal actividad humana que consume más agua en México?",
        "opciones": ["Industria", "Uso doméstico", "Agricultura"],
        "correcta": "Agricultura",
        "explicacion": "¡Correcto! La agricultura (riego) usa más del 70% del agua disponible en el país."
    }
]

def reiniciar_juego_trivia():
    st.session_state.puntuacion_trivia = 0
    st.session_state.pregunta_actual_trivia = 0
    st.session_state.estado_juego_trivia = "preguntando"
    st.session_state.respuesta_usuario_trivia = None

num_pregunta = st.session_state.pregunta_actual_trivia

if num_pregunta < len(preguntas):
    
    item = preguntas[num_pregunta]
    st.subheader(f"Pregunta {num_pregunta + 1}")
    st.write(item["pregunta"])
    
    respuesta = st.radio(
        "Selecciona tu respuesta:",
        item["opciones"],
        key=f"q_trivia_{num_pregunta}",
        disabled=(st.session_state.estado_juego_trivia == "respondido")
    )
    
    if st.session_state.estado_juego_trivia == "preguntando":
        if st.button("Verificar Respuesta", key=f"b_trivia_{num_pregunta}"):
            # Guardamos la respuesta del usuario
            st.session_state.respuesta_usuario_trivia = respuesta
            # Cambiamos el estado a "respondido"
            st.session_state.estado_juego_trivia = "respondido"
            
            # Verificamos y sumamos puntos (solo esta vez)
            if respuesta == item["correcta"]:
                st.session_state.puntuacion_trivia += 1
            
            # Re-ejecutamos para mostrar el resultado y el botón "Siguiente"
            st.rerun()
            
    elif st.session_state.estado_juego_trivia == "respondido":
        # --- Mostramos la retroalimentación ---
        if st.session_state.respuesta_usuario_trivia == item["correcta"]:
            st.success(item["explicacion"])
            st.balloons()
        else:
            st.error(f"Incorrecto. La respuesta correcta es: {item['correcta']}")
        
        # --- Mostramos el botón para avanzar ---
        if st.button("Siguiente Pregunta"):
            # Avanzamos a la siguiente pregunta
            st.session_state.pregunta_actual_trivia += 1
            # Reiniciamos el estado para la nueva pregunta
            st.session_state.estado_juego_trivia = "preguntando"
            st.session_state.respuesta_usuario_trivia = None
            st.rerun()

else:
    # --- FIN DEL JUEGO ---
    st.subheader("¡Juego Terminado!")
    st.write(f"Tu puntuación final es: {st.session_state.puntuacion_trivia} de {len(preguntas)}")
    
    st.divider() 
    st.header("Repaso de Respuestas Correctas")
    
    for i, item in enumerate(preguntas):
        with st.expander(f"**Pregunta {i+1}:** {item['pregunta']}"):
            st.success(f"**Respuesta correcta:** {item['correcta']}")
    
    st.divider() 

    if st.button("Volver a Jugar"):
        reiniciar_juego_trivia()
        st.rerun()

st.sidebar.write(f"Puntuación Trivia: {st.session_state.puntuacion_trivia}")
