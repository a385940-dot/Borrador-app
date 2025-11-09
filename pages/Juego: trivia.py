import streamlit as st

st.title("Juego: Trivia del Agua 💧")

# --- Usamos st.session_state ---
if 'puntuacion_trivia' not in st.session_state:
    st.session_state.puntuacion_trivia = 0
    
if 'pregunta_actual_trivia' not in st.session_state:
    st.session_state.pregunta_actual_trivia = 0

# Definimos las preguntas
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

# Función para reiniciar el juego
def reiniciar_juego_trivia():
    st.session_state.puntuacion_trivia = 0
    st.session_state.pregunta_actual_trivia = 0

# --- Lógica del Juego ---
num_pregunta = st.session_state.pregunta_actual_trivia

if num_pregunta < len(preguntas):
    
    item = preguntas[num_pregunta]
    st.subheader(f"Pregunta {num_pregunta + 1}")
    st.write(item["pregunta"])
    
    respuesta = st.radio(
        "Selecciona tu respuesta:",
        item["opciones"],
        key=f"q_trivia_{num_pregunta}"
    )
    
    if st.button("Verificar Respuesta", key=f"b_trivia_{num_pregunta}"):
        if respuesta == item["correcta"]:
            st.success(item["explicacion"])
            st.balloons()
            st.session_state.puntuacion_trivia += 1
        else:
            st.error(f"Incorrecto. La respuesta es: {item['correcta']}")
        
        st.session_state.pregunta_actual_trivia += 1
        st.rerun()

else:
    st.subheader("¡Juego Terminado!")
    st.write(f"Tu puntuación final es: {st.session_state.puntuacion_trivia} de {len(preguntas)}")
    
    if st.button("Volver a Jugar"):
        reiniciar_juego_trivia()
        st.rerun()

st.sidebar.write(f"Puntuación Trivia: {st.session_state.puntuacion_trivia}")
