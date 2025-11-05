import streamlit as st

# --- 1. Configuración de la Página ---
# Esto debe ser lo primero que se ejecuta
st.set_page_config(
    page_title="Guardianes del Agua",
    page_icon="💧",  # Puedes usar un emoji como ícono
    layout="centered" # "wide" o "centered"
)

# --- 2. Datos del Quiz ---
# Guardamos las preguntas como una lista de diccionarios.
# Esto puede crecer tanto como quieras.
PREGUNTAS = [
    {
        "pregunta": "¿Cuánta agua de la Tierra es agua dulce disponible para nosotros?",
        "opciones": ["50%", "10%", "Menos del 1%", "25%"],
        "respuesta": "Menos del 1%"
    },
    {
        "pregunta": "¿Cuál de estas acciones ahorra MÁS agua?",
        "opciones": ["Cerrar la llave al lavarte los dientes", "Instalar un inodoro de bajo flujo", "Regar el jardín al mediodía", "Lavar el auto con manguera"],
        "respuesta": "Instalar un inodoro de bajo flujo"
    },
    {
        "pregunta": "¿Cuánto tiempo debe durar una ducha para ser considerada 'ahorradora'?",
        "opciones": ["5 minutos", "15 minutos", "20 minutos", "30 minutos"],
        "respuesta": "5 minutos"
    }
]

# --- 3. Inicialización del Estado (Session State) ---
# El 'session_state' es la memoria de Streamlit.
# Nos permite recordar en qué pregunta estamos y cuál es el puntaje.

if 'pregunta_actual' not in st.session_state:
    st.session_state.pregunta_actual = 0
    st.session_state.puntaje = 0
    st.session_state.respuesta_enviada = False

# --- 4. Título y Encabezado ---
st.title("💧 Guardianes del Agua")
st.markdown("¡Aprende y juega para salvar nuestro recurso más valioso!")

# Separador
st.divider()

# --- 5. Sección de Consejos ---
# Usamos 'st.expander' para hacerlo interactivo y no ocupar espacio
with st.expander("Haz clic para ver consejos rápidos para ahorrar agua"):
    st.image("https://images.pexels.com/photos/3839432/pexels-photo-3839432.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1") # 
    st.markdown("""
    * **Cierra la llave** mientras te cepillas los dientes o te enjabonas las manos.
    * **Toma duchas más cortas.** ¡Intenta que no duren más de 5 minutos!
    * **Revisa y repara fugas.** Una gotera puede desperdiciar litros de agua al día.
    * **Usa la lavadora y el lavavajillas** solo con cargas completas.
    * **Riega tus plantas** temprano en la mañana o al anochecer para evitar la evaporación.
    """)

# --- 6. Sección del Juego (Quiz Interactivo) ---
st.header("Juego: ¿Cuánto Sabes?")

# Verificamos si ya pasamos todas las preguntas
if st.session_state.pregunta_actual >= len(PREGUNTAS):
    st.success(f"**¡Juego Terminado!**")
    st.balloons()
    st.write(f"**Tu puntaje final es: {st.session_state.puntaje} de {len(PREGUNTAS)}**")

    # Botón para reiniciar el juego
    if st.button("Jugar de Nuevo"):
        # Reiniciamos el estado
        st.session_state.pregunta_actual = 0
        st.session_state.puntaje = 0
        st.session_state.respuesta_enviada = False
        st.experimental_rerun() # Volvemos a ejecutar el script

else:
    # Obtener la pregunta actual
    idx = st.session_state.pregunta_actual
    pregunta_data = PREGUNTAS[idx]

    st.subheader(f"Pregunta {idx + 1}:")
    st.write(f"**{pregunta_data['pregunta']}**")

    # Usamos un formulario para agrupar el radio button y el botón de envío
    # Esto evita que la app se recargue con cada clic en una opción
    with st.form(key=f"quiz_form_{idx}"):
        
        # 'st.radio' para mostrar las opciones
        opcion_seleccionada = st.radio(
            "Elige tu respuesta:",
            options=pregunta_data["opciones"],
            key=f"radio_{idx}" # Una clave única es importante
        )
        
        # Botón de envío del formulario
        submit_button = st.form_submit_button(label="Enviar Respuesta")

    # --- 7. Lógica de Revisión ---
    # Esto se ejecuta solo si el botón "submit_button" fue presionado
    if submit_button:
        st.session_state.respuesta_enviada = True # Marcamos que se envió
        respuesta_correcta = pregunta_data["respuesta"]

        if opcion_seleccionada == respuesta_correcta:
            st.success("¡Correcto! 👍")
            st.session_state.puntaje += 1
        else:
            st.error(f"Incorrecto. 👎 La respuesta correcta era: {respuesta_correcta}")

    # Mostramos el botón "Siguiente" SOLO si ya se envió una respuesta
    if st.session_state.respuesta_enviada:
        if st.button("Siguiente Pregunta"):
            # Avanzamos a la siguiente pregunta
            st.session_state.pregunta_actual += 1
            # Reseteamos el estado de envío para la próxima pregunta
            st.session_state.respuesta_enviada = False 
            st.experimental_rerun() # Volvemos a ejecutar el script
