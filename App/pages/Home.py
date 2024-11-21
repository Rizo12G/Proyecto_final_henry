import streamlit as st
import re
import requests
import webbrowser
import pandas as pd

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
    Esta plataforma es una herramienta de análisis diseñada por DATAVISION para la empresa de transporte NYC LIBERTY TRANSPORTATION 
    que le permitirá explorar y comprender el mercado de taxis en la ciudad de Nueva York. Podras encontrar insights puntuales a través 
    del uso de machine learning y business intelligence, permitiéndote analizar datos y realizar predicciones de
    manera precisa y eficiente.

    Si quieres conocer todo el proceso de elaboracion de este modelo lo puedes encontrar aqui:
    </p>
    """, 
    unsafe_allow_html=True
)
if st.button("Ir al modelo 📂"):
    webbrowser.open("https://github.com/Rizo12G/Proyecto_final_henry/tree/main/ML")

st.markdown('***')

st.header('Mercado actual de taxis NYC 🗽')
st.markdown(
    """
    <p style="text-align: justify;">
    En Nueva York, los servicios de taxis y viajes compartidos como Uber han tenido un aumento del 15% en los ultimos años 
    transformando la movilidad urbana, brindando una opción accesible y conveniente frente al transporte público. Al mismo tiempo, 
    el cambio climático, acelerado por el uso de combustibles fósiles en la generación de energía, ha impulsado a las empresas a 
    tomar medidas más sostenibles, adoptando tecnologías y prácticas para reducir su impacto ambiental, con el 
    fin de mejorar la eficiencia energética y promover un consumo más responsable.
    </p>
    """, 
    unsafe_allow_html=True
)
col1, col2, col3 = st.columns(3)

histo = pd.read_csv('../App/hist_mensual.csv')

with col1:
    st.markdown('##### ')
    st.metric("Viajes mensuales promedio", f"{histo['Numero total de viajes'].mean():,.2f}")

with col2:
    st.markdown('##### ')
    st.metric("Numero de pasajeros mensuales promedio", f"{histo['Numero total de pasajeros'].mean():,.2f}") 

with col3:
    st.markdown('##### ')
    st.metric("Ingresos mensuales promedio", f"${histo['Ingreso total (USD)'].mean():,.2f}")

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