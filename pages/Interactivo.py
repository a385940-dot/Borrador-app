import streamlit as st

st.title("Juego: ¿Qué tanto sabes del Agua? 💧")

# --- Usamos st.session_state ---
# Esto es crucial para que la app "recuerde" la puntuación entre interacciones.
if 'puntuacion' not in st.session_state:
    st.session_state.puntuacion = 0
    
if 'pregunta_actual' not in st.session_state:
    st.session_state.pregunta_actual = 0

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
        "explicacion": "¡Correcto! Por eso es vital reducir el tiempo en la ducha."
    },
    {
        "pregunta": "¿Cuál es la principal actividad humana que consume más agua en México?",
        "opciones": ["Industria", "Uso doméstico", "Agricultura"],
        "correcta": "Agricultura",
        "explicacion": "¡Correcto! La agricultura (riego) usa más del 70% del agua disponible en el país."
    }
]

# Función para reiniciar el juego
def reiniciar_juego():
    st.session_state.puntuacion = 0
    st.session_state.pregunta_actual = 0

# --- Lógica del Juego ---
num_pregunta = st.session_state.pregunta_actual

if num_pregunta < len(preguntas):
    
    # Mostramos la pregunta actual
    item = preguntas[num_pregunta]
    st.subheader(f"Pregunta {num_pregunta + 1}")
    st.write(item["pregunta"])
    
    # --- Usamos st.radio ---
    respuesta = st.radio(
        "Selecciona tu respuesta:",
        item["opciones"],
        key=f"q_{num_pregunta}"
    )
    
    # --- Usamos st.button ---
    if st.button("Verificar Respuesta", key=f"b_{num_pregunta}"):
        if respuesta == item["correcta"]:
            st.success(item["explicacion"])
            st.balloons()
            st.session_state.puntuacion += 1
        else:
            st.error(f"Incorrecto. La respuesta es: {item['correcta']}")
        
        # Pasamos a la siguiente pregunta
        st.session_state.pregunta_actual += 1
        st.rerun() # Reinicia el script para mostrar la siguiente pregunta

else:
    # --- Fin del juego ---
    st.subheader("¡Juego Terminado!")
    st.write(f"Tu puntuación final es: {st.session_state.puntuacion} de {len(preguntas)}")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXN6OHZ2ZDRhdzRsY2Q5enRlcHQ3MHU1eHRqbWd5eDhmc3doNW5qZyZlcD1zZl9naWZfYnlfaWQmY3Q9Zw/3o7TKLHb0kpe5rM0uc/giphy.gif")
    
    if st.button("Volver a Jugar"):
        reiniciar_juego()
        st.rerun()

# Mostramos la puntuación actual
st.sidebar.write(f"Puntuación: {st.session_state.puntuacion}")
st.caption("Juego creado con `st.radio`, `st.button` y `st.session_state`.")
