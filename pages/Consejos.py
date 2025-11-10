import streamlit as st

st.title(" Consejos para Cuidar el Agua")

st.write("Cada gota cuenta. Aquí tienes acciones prácticas que puedes implementar en tu día a día.")


with st.expander("Al bañarse"):
    st.write(
        """
        - **Reduce el tiempo en la ducha:** Intenta bañarte en 5-10 minutos.
        - **Cierra la llave:** Mientras te enjabonas o te cepillas los dientes.
        - **Usa una cubeta:** Recolecta el agua fría mientras esperas que salga la caliente y úsala para regar plantas o el WC.
        - **Revisa fugas:** Un goteo en el WC puede gastar miles de litros al mes.
        """
    )
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3h0ZHFtdGo3Z3lqZzZ1ZWVnZ2Zid21iYzcxNTNnbXk5a2ltdXZoeSZlcD1zZl9naWZfYnlfaWQmY3Q9Zw/3o7TKLHb0kpe5rM0uc/giphy.gif")


with st.expander("En la Cocina"):
    st.write(
        """
        - **Remoja los trastes:** Enjabona todo primero y luego enjuaga rápido. No dejes la llave abierta.
        - **Lavafrutas en un tazón:** No bajo el chorro directo.
        - **No uses el chorro para descongelar:** Saca la comida con tiempo o usa el microondas.
        """
    )

with st.expander("Para el cuidado del jardín"):
    st.write(
        """
        - **Riega de noche o muy temprano:** Evitas que el sol evapore el agua.
        - **Usa regadera o goteo:** Evita la manguera.
        - **Lava el coche con cubeta:** Nunca con manguera.
        - **Barre, no "riego-laves":** Usa la escoba para limpiar patios y banquetas.
        """
    )

st.caption("Contenedores creados con `st.expander`.")
