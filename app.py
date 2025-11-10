import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

st.set_page_config(page_title="Cada Gota Cuenta", page_icon="💧", layout="centered")

# introduccion
st.title("💧 Cada Gota Cuenta")
st.markdown("""
**Introducción**

El agua es un recurso limitado: sólo una pequeña fracción del agua del planeta es agua dulce utilizable por los seres humanos. Esta aplicación muestra datos reales, un cuestionario interactivo, gráficos de tendencia y pequeños retos/juegos para aprender a ahorrar agua en casa.
""")

st.markdown("---")

#Preguntas
st.header("📝 Cuestionario")
st.write("Selecciona la respuesta que creas correcta y presiona **Enviar**.")

q1 = st.radio(
    "1) ¿Cuánta agua de la que hay en todo el planeta es agua dulce (aprox.)?",
    ("~97.5%", "~2.5%", "~0.5%"), index=1
)

q2 = st.radio(
    "2) ¿Cuánto ha cambiado la disponibilidad de agua dulce per cápita en las últimas décadas?",
    ("Ha aumentado", "Se ha mantenido igual", "Ha disminuido (decenas % en 30 años)"), index=2
)

q3 = st.radio(
    "3) ¿Cómo podemos colaborar para cuidarla?",
    ("Cerrar la llave al lavarnos los dientes", "Reparar fugas y usar duchas cortas", "Ambas anteriores"), index=2
)

if 'quiz_submitted' not in st.session_state:
    st.session_state['quiz_submitted'] = False

if st.button("Enviar respuestas ✅"):
    st.session_state['quiz_submitted'] = True

if st.session_state['quiz_submitted']:
    st.success("Gracias por participar. Aquí están las respuestas con explicación:")
    st.write("1) **~2.5%** del agua del planeta es dulce; de esa porción sólo una pequeña fracción (≈0.3–0.5% del total) es fácilmente accesible como ríos y lagos.")
    st.write("2) **Ha disminuido**: la disponibilidad per cápita ha ido bajando por aumento de población, mayor demanda y factores climáticos (varía por región).")
    st.write("3) **Ambas** son medidas sencillas y eficaces para reducir el consumo doméstico.")

st.markdown("---")

# Datos y graficos
st.header("📉 Estadísticas reales sobre agua potable")
st.write("A continuación verás una gráfica de ejemplo que resume datos públicos sobre la disponibilidad de agua dulce / potable. (Los valores son ilustrativos y basados en tendencias reportadas por organismos internacionales.)")

# Datos de tendencia
years = np.array([1995, 2000, 2005, 2010, 2015, 2020, 2024])
# Índice hipotético de 'agua dulce accesible' normalizado a 100 en 1995
water_index = np.array([100, 96, 90, 84, 78, 72, 69])

df_trend = pd.DataFrame({"Año": years, "Índice agua dulce accesible (1995=100)": water_index})
df_trend = df_trend.set_index('Año')

st.line_chart(df_trend)

st.write("Fuente: UNESCO / UN and World Bank (datos de referencia sobre recursos hídricos y disponibilidad per cápita).")

# tabla interactiva
st.subheader("Tabla de datos (valores índice)")
st.dataframe(df_trend)

# Gráfica
fig, ax = plt.subplots()
ax.plot(years, water_index, marker='o')
ax.set_xlabel('Año')
ax.set_ylabel('Índice (1995 = 100)')
ax.set_title('Tendencia: disponibilidad de agua dulce accesible')
st.pyplot(fig)

st.markdown("---")

# cosejos
st.header("✅ Consejos rápidos para ahorrar agua")
st.markdown("- Toma duchas más cortas\n- Repara fugas en grifos\n- No dejes la llave abierta mientras te cepillas\n- Usa la lavadora con carga completa\n- Recoge agua de lluvia para regar plantas")

st.markdown("---")

# Juegos
st.header("🎯 Retos y mini-juegos para ahorrar agua")

# Calculadora rápida de ahorro
st.subheader("1) Calculadora rápida: ¿cuánta agua puedes ahorrar?")
shower_minutes = st.number_input("Minutos promedio de ducha al día:", min_value=1, max_value=60, value=10)
if st.button("Calcular ahorro si reduces 2 minutos"):
    saved_liters = 9 * 2  
    st.info(f"Reduciendo 2 minutos por ducha ahorras aprox. {saved_liters} litros por persona al día (~{saved_liters*365} L/año).")

st.markdown("---")

# Reto semanal (gamificación)
st.subheader("2) Reto semanal: '7 días, 7 acciones'")
st.write("Marca las acciones que completes esta semana para ganar puntos y conservar agua:")
actions = [
    "Tomé duchas de menos de 5 minutos",
    "Reparé alguna fuga",
    "Cerré la llave al cepillarme los dientes",
    "Reutilicé agua para regar",
    "Usé la lavadora con carga completa"
]

points = 0
for i, act in enumerate(actions):
    done = st.checkbox(act, key=f"action_{i}")
    if done:
        points += 10

if st.button("Terminar semana y ver puntaje"):
    st.success(f"¡Tu puntaje de la semana es: {points} puntos! (Intenta superar tu marca la próxima semana)")

st.markdown("---")



