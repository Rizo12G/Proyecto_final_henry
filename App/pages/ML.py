
import streamlit as st
import pandas as pd
from prophet.serialize import model_from_json
from plotly import graph_objs as go
from prophet.serialize import model_to_json, model_from_json


st.cache_data.clear()
st.cache_resource.clear()

# Título y descripción
st.markdown("""
<div style="display: flex; align-items: center; justify-content: center;">
    <h1 style="margin-right: 0px;">Forecasting</h1>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="width: 50px; height: 50px;">
        <path d="M3,14L3.5,14.07L8.07,9.5C7.89,8.85 8.06,8.11 8.59,7.59C9.37,6.8 10.63,6.8 11.41,7.59C11.94,8.11 12.11,8.85 11.93,9.5L14.5,12.07L15,12C15.18,12 15.35,12 15.5,12.07L19.07,8.5C19,8.35 19,8.18 19,8A2,2 0 0,1 21,6A2,2 0 0,1 23,8A2,2 0 0,1 21,10C20.82,10 20.65,10 20.5,9.93L16.93,13.5C17,13.65 17,13.82 17,14A2,2 0 0,1 15,16A2,2 0 0,1 13,14L13.07,13.5L10.5,10.93C10.18,11 9.82,11 9.5,10.93L4.93,15.5L5,16A2,2 0 0,1 3,18A2,2 0 0,1 1,16A2,2 0 0,1 3,14Z" fill="#367884" />
    </svg>
</div>
""", unsafe_allow_html=True)

# Cargar datos históricos
def cargar_datos(ruta_csv):
    df = pd.read_csv(ruta_csv)
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    df['Fecha'] = df['Fecha'].dt.date
    return df

histo = cargar_datos('App/hist_mensual.csv')
prom = pd.read_csv('App/prom_mes.csv')

st.header('Datos Históricos (2022 - 2024)')
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

n_months = st.slider('Meses:', 0, 18)

with open('App/json_model/serialized_model.json', 'r') as fin:
    modelo_prophet = model_from_json(fin.read())

# Mostrar predicciones
future = modelo_prophet.make_future_dataframe(periods=n_months, freq='M')
forecast = modelo_prophet.predict(future)

forecast = forecast[['ds','yhat']]
forecast.rename(columns={'ds':'Fecha','yhat':'Numero total de viajes'},inplace=True)

forecast['Mes'] = pd.to_datetime(forecast['Fecha']).dt.month
pred= forecast.merge(prom, left_on='Mes', right_on='month')

pred['Fecha'] = pred['Fecha'].dt.date
pred['Numero total de pasajeros'] = pred['Numero total de viajes'] * pred['passenger_trip']
pred['Distancia total recorrida (mi)'] = pred['Numero total de viajes'] * pred['distance_trip']
pred['Ingreso total (USD)'] = pred['Numero total de viajes'] * pred['total_trip']
pred['Duración total recorrido (min)'] = pred['Numero total de viajes'] * pred['duration_trip']
pred.drop(columns=['Mes', 'month','passenger_trip', 'distance_trip','total_trip','duration_trip','n_trips'], inplace=True)
pred = pred.round(2)
pred['Numero total de pasajeros'] = pred['Numero total de pasajeros'].astype(int)
pred['Numero total de viajes'] = pred['Numero total de viajes'].astype(int)

if n_months == 0:
     st.warning('Debes seleccionar un numero de meses a predecir')
else:
     st.write(pred[30:])
#---------
# Crear la gráfica combinada de históricos y pronósticos
fig2 = go.Figure()

# Datos históricos (línea azul)
fig2.add_trace(go.Scatter(
    x=histo['Fecha'], 
    y=histo['Numero total de viajes'],
    mode='lines', 
    name='Datos Históricos',
    line=dict(color='blue')  # Línea azul
))

# Pronósticos (línea roja punteada)
fig2.add_trace(go.Scatter(
    x=pred['Fecha'], 
    y=pred['Numero total de viajes'],
    mode='lines', 
    name='Pronósticos',
    line=dict(color='red', dash='dash')  # Línea roja punteada
))

# Configuración del gráfico
fig2.update_layout(
    title='Datos Históricos y Pronósticos de Número de Viajes',
    xaxis_title='Fecha',
    yaxis_title='Número total de viajes',
    title_font=dict(size=24),
    xaxis_rangeslider_visible=True
)

# Mostrar la gráfica en Streamlit
st.plotly_chart(fig2) 

total_viajes = pred['Numero total de viajes'][30:].sum()

st.metric(f"Numero total de viajes en {n_months} meses:", f"{total_viajes:,}")

pred.to_csv('App/pred.csv')

st.markdown('***')
# Calcular valores de predicción total (en USD) y total de viajes (número de viajes) 
total_usd = pred['Ingreso total (USD)'][30:].sum()  # Sumar los ingresos en USD de los primeros meses seleccionados
total_pas = pred['Numero total de pasajeros'][30:].sum()
total_dist = pred['Distancia total recorrida (mi)'][30:].sum() 
total_dur = pred['Duración total recorrido (min)'][30:].sum() / 60  # Sumar el número de viajes de los primeros meses seleccionados


col1, col2 = st.columns(2, gap='large', vertical_alignment='center')  
    
with col1:
    # Mostrar los valores en una ventana
    st.metric("Total de Pasajeros 👫", f"{total_pas:,}")
    st.metric("Total Ingresos (USD) 💵", f"${total_usd:,.2f}")   

with col2:
    st.metric("Total Distancia recorrida (mi) 🌐", f"{total_dist:,.2f}")
    st.metric("Total Tiempo recorrido (hrs) ⏱", f"{total_dur:,.2f}")  

