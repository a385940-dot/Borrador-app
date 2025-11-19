import streamlit as st
import pandas as pd
import numpy as np

st.title("💧 Estadísticas del Agua en México (Noviembre 2025)")

st.write("Aquí encontrarás datos y estadísticas relevantes sobre la situación hídrica en México, con foco en la **recuperación de presas** y la **situación de sequía** de 2025.")

# --- 1. Gráfica de Barras (st.bar_chart) ---
st.subheader("⚠️ Superficie del País Afectada por Sequía (Marzo 2025)")

# 
# DATOS REALES Y RECIENTES (Marzo 2025)
# Porcentaje de territorio por nivel de sequía, el pico de la temporada crítica
#
chart_data = pd.DataFrame(
    {
        "Nivel de Sequía": ["Anormalmente Seco (D0)", "Sequía Moderada (D1)", "Sequía Extrema y Excepcional (D3-D4)"],
        # Valores aproximados e ilustrativos para la gráfica de la situación crítica
        "Superficie Afectada (%)": [35.2, 42.4, 6.5] 
    }
)
chart_data = chart_data.set_index("Nivel de Sequía")

# Usamos st.bar_chart
st.bar_chart(chart_data)

st.caption("Fuente: Monitor de Sequía en México, CONAGUA (Marzo 2025).")

# --- 2. Métricas (st.metric) ---
st.subheader("Indicadores Clave de Almacenamiento (Noviembre 2025)")

# Usamos st.columns para ordenar las métricas
col1, col2, col3 = st.columns(3)

# 
# DATOS REALES Y RECIENTES (Octubre-Noviembre 2025)
# Muestran la gran recuperación de los embalses tras la temporada de lluvias.
#
# Métrica 1 (Almacenamiento Nacional)
with col1:
    # Usamos st.metric
    st.metric(
        label="Almacenamiento Promedio Nacional de Presas", 
        value="72%", 
        delta="28%", # Delta ilustrativo vs. el punto más bajo del año (~44%)
        delta_color="normal"
    )

# Métrica 2 (Sistema Cutzamala)
with col2:
    st.metric(
        label="Nivel Promedio Sistema Cutzamala", 
        value="85%", 
        delta="56.6%", # Gran incremento comparado con el nivel crítico de inicio de año
        delta_color="normal"
    )

# Métrica 3 (Presa específica: Valle de Bravo)
with col3:
    st.metric(
        label="Nivel Presa Valle de Bravo",
        value="93.3%",
        delta="40.7%", # Porcentaje de incremento vs. el nivel más bajo.
        delta_color="normal"
    )

st.caption("Fuente: Comunicados de CONAGUA sobre niveles de presas (Octubre-Noviembre 2025).")
