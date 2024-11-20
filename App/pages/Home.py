import streamlit as st
import re
import requests

### Funciones

# Define una función para mostrar información de contacto
def mostrar_contacto():
    st.write("📧 **Correo electrónico:** contacto@datavision.com")
    st.write("📞 **Teléfono:** +1 553 456 7050")
    st.write("🏢 **Dirección:** Carrera 7 # 105 - 13, Bogota D.C., Colombia")


st.image("./images/portada.jpg", width=1200)


st.title("🚕 ¡Bienvenido!")

st.markdown(
    """
    <p style="text-align: justify;">
    Esta plataforma es una herramienta de análisis diseñada por Data Vision para explorar y comprender el mercado de taxis en la ciudad de Nueva York. 
    Ofrece insights puntuales a través del uso de machine learning y business intelligence, permitiéndote analizar datos y realizar predicciones de
    manera precisa y eficiente.
    </p>
    """, 
    unsafe_allow_html=True
)


st.markdown('***')

col1, col2 = st.columns(2, gap='large', vertical_alignment='center')

with col2:
    
    st.image('images/logo.jpg', width= 350)
    

with col1:
    st.header('¿Quienes somos?', anchor=False)

    st.markdown(
        """
        <p style="text-align: justify;">
        Somos una consultora especializada en análisis, ingeniería y ciencia de datos. Nos enfocamos en ser un socio estratégico para nuestros clientes, 
        ayudándoles a alcanzar sus objetivos mediante el aprovechamiento eficiente de los datos. Nuestro propósito es generar un impacto positivo en 
        el desarrollo y crecimiento del entorno empresarial, utilizando los datos para crear información valiosa.
        </p>
        """, unsafe_allow_html=True
        
    )
    if st.button('📬 Contáctenos'):
        mostrar_contacto()

