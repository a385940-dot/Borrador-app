import streamlit as st

# --- 1. Configuración de la Página ---
st.set_page_config(
    page_title="Guardianes del Agua 💧🌎",
    page_icon="🌊",
    layout="centered", # "wide" o "centered"
    initial_sidebar_state="expanded"
)

# --- 2. CSS Personalizado (¡Para los colores y el estilo divertido!) ---
# Inyectamos CSS para darle una apariencia más personalizada y atractiva
st.markdown("""
<style>
/* Fondo general */
.stApp {
    background: linear-gradient(to bottom, #e0f2f7, #bbdefb); /* Degradado suave de azul claro */
    color: #212121; /* Texto oscuro para contraste */
    font-family: 'Poppins', sans-serif; /* Fuente moderna */
}

/* Encabezados */
h1, h2, h3, h4, h5, h6 {
    color: #007bb6; /* Azul brillante para títulos */
    font-family: 'Lobster', cursive; /* Fuente más divertida para títulos principales */
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
}

h1 {
    font-size: 3.5em; /* Título principal más grande */
    text-align: center;
    color: #004d7c; /* Azul oscuro para el título principal */
}

/* Contenedores principales */
.main .block-container {
    background-color: rgba(255, 255, 255, 0.9); /* Blanco semitransparente para el contenido */
    border-radius: 15px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    padding: 2em;
    margin-top: 1em;
}

/* Botones */
.stButton>button {
    background-color: #4CAF50; /* Verde vibrante */
    color: white;
    border-radius: 8px;
    border: none;
    padding: 0.7em 1.5em;
    font-size: 1.1em;
    font-weight: bold;
    transition: all 0.3s ease-in-out;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.stButton>button:hover {
    background-color: #45a049; /* Verde más oscuro al pasar el ratón */
    transform: translateY(-2px); /* Pequeño efecto de elevación */
    box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
}

/* Botones de radio (opciones del quiz) */
div[role="radiogroup"] label {
    background-color: #e3f2fd; /* Azul muy claro para las opciones */
    border-left: 5px solid #2196f3; /* Borde azul para destacar */
    padding: 10px 15px;
    margin-bottom: 5px;
    border-radius: 5px;
    transition: all 0.2s ease-in-out;
}

div[role="radiogroup"] label:hover {
    background-color: #c5e1fd; /* Más oscuro al pasar el ratón */
    transform: translateX(5px);
}

/* Mensajes de éxito y error */
.st.success {
    background-color: #e8f5e9; /* Fondo verde claro */
    color: #2e7d32; /* Texto verde oscuro */
    border-left: 5px solid #4CAF50;
    border-radius: 5px;
    padding: 10px;
}

.st.error {
    background-color: #ffebee; /* Fondo rojo claro */
    color: #d32f2f; /* Texto rojo oscuro */
    border-left: 5px solid #f44336;
    border-radius: 5px;
    padding: 10px;
}

/* Texto general */
p {
    font-size: 1.1em;
}

/* Fuentes importadas de Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Lobster&family=Poppins:wght@300;400;600&display=swap');
</style>
""", unsafe_allow_html=True)


# --- 3. Datos del Quiz ---
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
    },
    {
        "pregunta": "¿Qué es la 'huella hídrica'?",
        "opciones": ["La marca que dejan tus pies en la arena mojada", "El volumen total de agua dulce utilizada para producir bienes y servicios", "El camino que sigue un río", "La cantidad de agua en una botella"],
        "respuesta": "El volumen total de agua dulce utilizada para producir bienes y servicios"
    },
    {
        "pregunta": "¿Cuál es la forma más efectiva de regar un jardín para ahorrar agua?",
        "opciones": ["Con una manguera sin boquilla", "Por inundación una vez a la semana", "Usando un sistema de riego por goteo", "Regando al mediodía"],
        "respuesta": "Usando un sistema de riego por goteo"
    }
]

# --- 4. Inicialización del Estado (Session State) ---
if 'pregunta_actual' not in st.session_state:
    st.session_state.pregunta_actual = 0
    st.session_state.puntaje = 0
    st.session_state.respuesta_enviada = False
    st.session_state.opcion_elegida_para_quiz = None
    st.session_state.juego_iniciado = False

# --- 5. Título y Encabezado con Diseño ---
st.markdown("<h1>Guardianes del Agua 💧🌎</h1>", unsafe_allow_html=True)
st.markdown("### ¡Tu misión es aprender, jugar y salvar nuestro recurso más valioso!")

# <-- CORRECCIÓN: Usando imagen local de la carpeta 'images'
st.image("images/gota.jpeg",
         caption="¡Cada gota cuenta!", use_column_width=True)

st.divider() # Un separador visual

# --- 6. Sección de Inicio del Juego ---
if not st.session_state.juego_iniciado:
    st.info("¡Bienvenido/a! Prepara tu mente para una aventura acuática. Conoce hechos asombrosos sobre el agua y pon a prueba tus conocimientos.")
    if st.button("¡Comenzar la Aventura! 🚀", help="Haz clic para iniciar el juego y aprender."):
        st.session_state.juego_iniciado = True
        st.rerun()
else:

    # --- 7. Sección de Consejos (con más estilo) ---
    with st.expander("✨ Consejos Rápidos: ¡Sé un Héroe del Agua! ✨"):
        st.markdown("""
        <div style="background-color: #f0f8ff; padding: 15px; border-radius: 10px; border-left: 5px solid #42a5f5;">
            <p>Aquí tienes acciones sencillas que marcan una gran diferencia:</p>
            <ul>
                <li>💧 **Cierra la llave** mientras te cepillas los dientes o te enjabonas las manos. ¡Ahorra hasta 10 litros por minuto!</li>
                <li>🚿 **Duchas cortas:** Intenta que no duren más de 5 minutos. ¡Pon tu canción favorita y sal antes de que termine!</li>
                <li>Leak **Repara las fugas:** Una gotera insignificante puede desperdiciar miles de litros al año. ¡Revisa tu casa!</li>
                <li>🧺 **Cargas completas:** Usa la lavadora y el lavavajillas solo cuando estén llenos.</li>
                <li>🌱 **Riego inteligente:** Riega tus plantas temprano en la mañana o al anochecer para evitar que el agua se evapore con el sol.</li>
                <li>🚗 **Lava el coche con cubeta:** Evita usar la manguera directamente, ahorrarás mucha agua.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # --- 8. Sección del Juego (Quiz Interactivo) ---
    st.header("🧠 Juego: ¿Cuánto Sabes de Agua? 🌊")

    # Barra de progreso del quiz
    progreso = (st.session_state.pregunta_actual) / len(PREGUNTAS)
    st.progress(progreso, text=f"Progreso: {st.session_state.pregunta_actual} de {len(PREGUNTAS)} preguntas")

    # Verificamos si ya pasamos todas las preguntas
    if st.session_state.pregunta_actual >= len(PREGUNTAS):
        st.success(f"**🎉 ¡Juego Terminado! ¡Felicidades, Guardián/a del Agua! 🎉**")
        st.balloons() # Animación de globos
        st.markdown(f"## Tu puntaje final es: **{st.session_state.puntaje} de {len(PREGUNTAS)}**")

        if st.session_state.puntaje == len(PREGUNTAS):
            st.markdown("¡Impresionante! Eres un verdadero experto/a en el agua. ¡Gracias por ser un ejemplo!")
        elif st.session_state.puntaje >= len(PREGUNTAS) / 2:
            st.markdown("¡Muy bien! Tienes un buen conocimiento. ¡Sigue aprendiendo para ser un campeón!")
        else:
            st.markdown("¡Buen intento! Cada pregunta es una oportunidad para aprender algo nuevo. ¡Sigue practicando!")

        # <-- CORRECCIÓN: Usando imagen local de la carpeta 'images'
        st.image("images/gracias.jpeg",
                 caption="¡Gracias por cuidar el agua!", use_column_width=True)

        # Botón para reiniciar el juego
        if st.button("🔄 Jugar de Nuevo", help="Haz clic para reiniciar el quiz."):
            # Reiniciamos el estado
            st.session_state.pregunta_actual = 0
            st.session_state.puntaje = 0
            st.session_state.respuesta_enviada = False
            st.session_state.opcion_elegida_para_quiz = None
            st.rerun()

    else:
        # Obtener la pregunta actual
        idx = st.session_state.pregunta_actual
        pregunta_data = PREGUNTAS[idx]

        st.subheader(f"Pregunta {idx + 1}:")
        st.markdown(f"**❓ {pregunta_data['pregunta']}**")

        # Corrección del índice del radio
        default_index = 0
        if st.session_state.opcion_elegida_para_quiz in pregunta_data["opciones"]:
            default_index = pregunta_data["opciones"].index(st.session_state.opcion_elegida_para_quiz)
        
        opcion_seleccionada = st.radio(
            "Elige tu respuesta:",
            options=pregunta_data["opciones"],
            key=f"radio_{idx}",
            index=default_index,
            disabled=st.session_state.respuesta_enviada 
        )
        st.session_state.opcion_elegida_para_quiz = opcion_seleccionada

        # --- Lógica de Revisión y Botones ---
        col1, col2 = st.columns(2) # Usamos columnas para los botones

        with col1:
            if st.button("✅ Enviar Respuesta", key=f"submit_btn_{idx}",
                         disabled=st.session_state.respuesta_enviada,
                         help="Haz clic para comprobar tu respuesta."):
                st.session_state.respuesta_enviada = True
                respuesta_correcta = pregunta_data["respuesta"]

                if opcion_seleccionada == respuesta_correcta:
                    st.success("¡Correcto! Eres un campeón/a del agua. 🎉")
                    st.balloons()
                    st.session_state.puntaje += 1
                else:
                    st.error(f"Incorrecto. 😟 La respuesta correcta era: **{respuesta_correcta}**")
                
                st.rerun()

        with col2:
            # El botón "Siguiente" solo aparece si ya se envió una respuesta
            if st.session_state.respuesta_enviada:
                if st.button("➡️ Siguiente Pregunta", key=f"next_btn_{idx}",
                             help="Haz clic para pasar a la siguiente pregunta."):
                    st.session_state.pregunta_actual += 1
                    st.session_state.respuesta_enviada = False
                    st.session_state.opcion_elegida_para_quiz = None
                    st.rerun()

# --- 9. Pie de Página ---
st.divider()
st.info("Un proyecto creado con Streamlit para concienciar sobre el cuidado del agua. ¡Gracias por ser parte de la solución!")
st.markdown("Hecho con ❤️ por un futuro sostenible.")
