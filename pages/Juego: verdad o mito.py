import streamlit as st

st.title("Juego: verdadero o falso sobre el agua")

if 'pregunta_actual_falso' not in st.session_state:
    st.session_state.pregunta_actual_falso = 0
    st.session_state.puntuacion_falso = 0

if 'estado_juego_falso' not in st.session_state:
    st.session_state.estado_juego_falso = "preguntando"

if 'respuesta_usuario_falso' not in st.session_state:
    st.session_state.respuesta_usuario_falso = None 

mitos_y_verdades = [
    {
        "afirmacion": "verdadero o falso: El agua embotellada es siempre más segura que el agua del grifo.",
        "respuesta": "Falso",
        "explicacion": "Falso. En muchas ciudades de México la calidad del agua de la red es monitoreada constantemente, mientras que el agua embotellada no siempre cumple todos los estándares y además genera muchísimo plástico."},
    {
        "afirmacion": "verdadero o falso: Lavar el coche con manguera gasta más de 300 litros de agua",
        "respuesta": "Verdadero",
        "explicacion": "Verdadero. Usar la manguera puede gastar hasta 500 litros. Usar una cubeta y esponja gasta solo unos 50 litros."},
    {
        "afirmacion": "verdadero o falso: Hervir el agua elimina los metales pesados (como el plomo).",
        "respuesta": "Falso",
        "explicacion": "Falso. Hervir el agua solo mata gérmenes (bacterias o virus). No elimina metales pesados, para eso se necesita un filtro."},
    {
        "afirmacion": "verdadero o falso: Se necesita más agua para producir 1kg de carne de res que 1kg de verduras",
        "respuesta": "Verdadero",
        "explicacion": "Verdadero. Se estima que producir 1kg de carne de res requiere unos 15,000 litros de agua (contando el riego del alimento para el animal), mientras que 1kg de maíz requiere unos 1,200 litros."}]

def reiniciar_juego_falso():
    st.session_state.pregunta_actual_falso = 0
    st.session_state.puntuacion_falso = 0
    st.session_state.estado_juego_falso = "preguntando"
    st.session_state.respuesta_usuario_falso = None

num_pregunta = st.session_state.pregunta_actual_falso

if num_pregunta < len(verdadero_o_falso):
    item = verdadero_o_falso[num_pregunta]
    
    st.subheader(item["afirmacion"])
    
    
    if st.session_state.estado_juego_falso == "preguntando":
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Es falso", key=f"m_{num_pregunta}", use_container_width=True):
                st.session_state.respuesta_usuario_falso = "Falso"
                st.session_state.estado_juego_mito = "respondido"
                if item["respuesta"] == "Falso":
                    st.session_state.puntuacion_mito += 1
                st.rerun()

        with col2:
            if st.button("Es verdadero", key=f"v_{num_pregunta}", use_container_width=True):
                st.session_state.respuesta_usuario_falso = "Verdadero"
                st.session_state.estado_juego_falso = "respondido"
                if item["respuesta"] == "Verdadero":
                    st.session_state.puntuacion_falso += 1
                st.rerun()
                
    elif st.session_state.estado_juego_falso == "respondido":
        
        if st.session_state.respuesta_usuario_falso == item["respuesta"]:
            st.success(item["explicacion"])
        else:
            st.error(f"Incorrecto. La respuesta era: {item['respuesta']}. {item['explicacion']}")
        
        if st.button("Siguiente Afirmación"):
            st.session_state.pregunta_actual_falso += 1
            st.session_state.estado_juego_falso = "preguntando"
            st.session_state.respuesta_usuario_falso = None
            st.rerun()

else:
    st.header("Juego terminado")
    st.write(f"Tu puntuación fue: {st.session_state.puntuacion_mito} de {len(verdadero_o_falso)}")
    st.balloons()

    st.divider() 
    st.header("Repaso de respuestas correctas")
    
    for item in verdadero_o_falso:
        st.markdown(f"**Afirmación:** {item['afirmacion']}")
        if item["respuesta"] == "Verdadero":
            st.success("Respuesta: Verdadero")
        else:
            st.error("Respuesta: Falso")
        st.write(item["explicacion"]) 
        st.caption("---") 

    st.divider()
    
    if st.button("Volver a Jugar"):
        reiniciar_juego_mito()
        st.rerun()

st.sidebar.write(f"Puntuación final: {st.session_state.puntuacion_falso}")
