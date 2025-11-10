import streamlit as st

st.title(" Consejos para Cuidar el Agua")

st.write("Cada gota cuenta. Aquí tienes acciones prácticas que puedes implementar en tu día a día.")


with st.expander("Al bañarse"):
    st.write(
        """
        - **Reduce el tiempo en la ducha:** Intenta bañarte en 5-10 minutos.
        - **Cierra la llave:** Mientras te enjabonas o te cepillas los dientes.
        - **Usa una cubeta:** Recolecta el agua fría mientras esperas que salga la caliente y úsala para regar plantas o para el inodoro.
        - **Revisa fugas:** Un goteo en el inodoro puede gastar miles de litros al mes.
        """
    )
    st.image("https://media.tenor.com/_iy7RyO-634AAAAM/bubu-dudu.gif")


with st.expander("En la Cocina"):
    st.write(
        """
        - **Remoja los trastes:** Enjabona todo primero y luego enjuaga rápido. No dejes la llave abierta.
        - **Lava las frutas en un tazón:** No bajo el chorro directo.
        - **No uses el chorro para descongelar:** Saca la comida con tiempo o usa el microondas.
        """
    )
    st.image("https://i.pinimg.com/originals/28/ed/52/28ed52a553df9f994789b3739b5abf17.gif")

with st.expander("Para el cuidado del jardín"):
    st.write(
        """
        - **Riega de noche o muy temprano:** Evitas que el sol evapore el agua.
        - **Usa regadera:** Evita la manguera.
        - **Lava el coche con cubeta:** Nunca con manguera.
        - **Barre, no uses la manguera para mojar la banqueta:** Usa la escoba para limpiar patios y banquetas.
        """
    )
