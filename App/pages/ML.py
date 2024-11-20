
import streamlit as st
import pandas as pd
from plotly import graph_objs as go


st.markdown(
    """
    <div style="display: flex; align-items: center; justify-content: center;">
        <h1 style="margin-right: 0px;">Forecasting</h1>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="width: 50px; height: 50px;">
            <path d="M3,14L3.5,14.07L8.07,9.5C7.89,8.85 8.06,8.11 8.59,7.59C9.37,6.8 10.63,6.8 11.41,7.59C11.94,8.11 12.11,8.85 11.93,9.5L14.5,12.07L15,12C15.18,12 15.35,12 15.5,12.07L19.07,8.5C19,8.35 19,8.18 19,8A2,2 0 0,1 21,6A2,2 0 0,1 23,8A2,2 0 0,1 21,10C20.82,10 20.65,10 20.5,9.93L16.93,13.5C17,13.65 17,13.82 17,14A2,2 0 0,1 15,16A2,2 0 0,1 13,14L13.07,13.5L10.5,10.93C10.18,11 9.82,11 9.5,10.93L4.93,15.5L5,16A2,2 0 0,1 3,18A2,2 0 0,1 1,16A2,2 0 0,1 3,14Z" fill="#367884" />
        </svg>
    </div>
    """,
    unsafe_allow_html=True
)

def cargar(csv):
    df = pd.read_csv(csv)
    df.reset_index(drop=True,inplace=True)
    return df

histo = cargar('../App/hist_mensual.csv')
pred = cargar('../App/predicciones.csv')

st.header('Datos Historicos (2022 - 2024)')
st.write(histo)

def plot_historic(df,m):
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=df['Fecha'], y=df['Numero total de viajes']))
	fig.layout.update(title={
            'text': f'Número de viajes {m}',  # Texto del título
            'x': 0.5,  # Centra el título (0 es izquierda, 1 es derecha)
            'xanchor': 'center',  # Asegura el centrado exacto
            'yanchor': 'top'      # Posiciona el título en la parte superior
        },
        title_font={
            'size': 24  # Cambia el tamaño de la letra
        }, xaxis_rangeslider_visible=True)
	st.plotly_chart(fig)

plot_historic(histo,'mensual')

st.header('Predicciones (2024 - 2026)')

st.markdown(
    """
    <p style="text-align: justify;">
    Puedes predecir de septiembre de 2024 (1 mes) a febrero del 2026 (18 meses)
    </p>
    """, 
    unsafe_allow_html=True
)

n_months = st.slider('Meses:', 1, 18)

st.write(pred[:n_months])
plot_historic(pred[:n_months],'futuros')

st.markdown('***')
# Calcular valores de predicción total (en USD) y total de viajes (número de viajes) 
total_usd = pred['Ingreso total (USD)'].head(n_months).sum()  # Sumar los ingresos en USD de los primeros meses seleccionados
total_viajes = pred['Numero total de pasajeros'].head(n_months).sum()
total_dist = pred['Distancia total recorrida (mi)'].head(n_months).sum() 
total_dur = pred['Duración total recorrido (min)'].head(n_months).sum() / 60  # Sumar el número de viajes de los primeros meses seleccionados


col1, col2 = st.columns(2, gap='large', vertical_alignment='center')  
    
with col1:
    # Mostrar los valores en una ventana
    st.metric("Total de Pasajeros 👫", f"{total_viajes:,}")
    st.metric("Total Ingresos (USD) 💵", f"${total_usd:,.2f}")   

with col2:
    st.metric("Total Distancia recorrida (mi) 🌐", f"{total_dist:,.2f}")
    st.metric("Total Tiempo recorrido (hrs) ⏱", f"{total_dur:,.2f}")  

st.markdown('***')
st.subheader('Prediccion de costos y emisiones')

per = st.slider('Porcentaje de vehiculos electricos 🍃:', 0, 100)
per = per / 100

col1, col2 = st.columns(2, gap='large', vertical_alignment='center')

co2 = total_dist*(411/1000000)*(1-per)
cost_gas = (total_dist/40)*3.42*(1-per)
eff = 170
cons_kw = ((total_dist*per*1.60934)*eff)/1000
cost_kw = cons_kw*0.3

with col1:
     st.metric("Costo de gasolina (USD)", f"${cost_gas:,.2f}")
     st.metric("Costo de watts (USD)", f"${cost_kw:,.2f}")
     st.metric("Costo total de combustible (USD)", f"${(cost_kw+cost_gas):,.2f}")

with col2:
     st.metric("Total emisiones de CO2 (ton)", f"{co2:,.2f}")

