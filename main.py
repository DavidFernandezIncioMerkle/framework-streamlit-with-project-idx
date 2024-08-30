import streamlit as st

st.title("Hola, Mundo que tal como lo veis!")
st.write("Esta es una aplicación de ejemplo usando Streamlit en Project IDX.")

# Añadir un control deslizante
slider_value = st.slider("Selecciona un valor", 0, 100, 50)
st.write(f"El valor seleccionado es: {slider_value}")

# Añadir un botón
if st.button("Haz clic aquí"):
    st.write("¡Has hecho clic en el botón!")