
import streamlit as st
import pandas as pd
from plotly import graph_objs as go

st.cache_data.clear()
st.cache_resource.clear()

st.markdown(
    """
    <div style="display: flex; align-items: center; justify-content: center;">
        <h1 style="margin-right: 0px;">Business Intelligence</h1>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="width: 50px; height: 50px;">
            <path d="M22,21H2V3H4V19H6V10H10V19H12V6H16V19H18V14H22V21Z" fill="#367884" />
        </svg>
    </div>
    """,
    unsafe_allow_html=True
)

pred_past = pd.read_csv('App/pred.csv')
n_months = pred_past.shape[0]

if n_months == 30:
     st.warning('No has seleccionado un numero de meses para predecir. Debes hacerlo en Forecasting :material/timeline:')
else:
    st.markdown("""
    En esta seccion podras realizar un analisis de negocio con base en el comportamiento del mercado de la ciudad a partir de:
    - Evaluacion de costos
    - Impacto ambiental
    """)

    pred_past['Emisiones CO2 (ton)'] = pred_past['Distancia total recorrida (mi)']*(411/1000000)
    pred = pred_past[30:]
    n_months=pred.shape[0]

    total_usd = pred['Ingreso total (USD)'].sum()  # Sumar los ingresos en USD de los primeros meses seleccionados
    total_pas = pred['Numero total de pasajeros'].sum()
    total_dist = pred['Distancia total recorrida (mi)'].sum() 
    total_dur = pred['Duración total recorrido (min)'].sum() / 60  # Sumar el número de viajes de los primeros meses seleccionados
    dias_pred = n_months*30

    st.header(f'Estimaciones para {n_months} meses de operacion')

    st.subheader('Demanda futura en NYC 🗽')

    col, col3 = st.columns(2, gap='large', vertical_alignment='center')

    with col:
        total_viajes = pred['Numero total de viajes'].sum()
        st.metric(f"Numero total de viajes en {n_months} meses:", f"{total_viajes:,}")

    with col:
        viajes_dia = total_viajes/dias_pred
        st.metric(f"Numero aproximado de viajes diarios:", f"{int(viajes_dia):,}")

    with col3:
        viajes_veh = 5.78
        veh_dia = (viajes_dia / viajes_veh )
        st.metric(f"Numero aproximado de vehiculos necesarios:", f"{int(veh_dia):,}")

    st.markdown('***')

    st.subheader('Qué porcentaje de la demanda te gustaria cubrir? 👫')
    per_d = st.slider('Porcentaje:', 0, 100, key='per_d')
    per_d = per_d / 100

    co4, col5 = st.columns(2, gap='large', vertical_alignment='center')

    with co4:
        viajes_dia_cubrir = viajes_dia*per_d
        st.metric(f"Cubririas estos viajes diarios:", f"{int(viajes_dia_cubrir):,}")

    with col5:
        vehiculos_necesarios = veh_dia*per_d
        st.metric(f"Necesitarias este numero de vehiculos:", f"{int(vehiculos_necesarios):,}")

    st.subheader('Selecciona el porcentaje de vehiculos electricos 🍃')
    per = st.slider('Porcentaje:', 0, 100, key='per')
    per = per / 100
    veh_cov = vehiculos_necesarios*(1-per)
    veh_ele = vehiculos_necesarios*per

    dist_diaria = total_dist / dias_pred
    co2 = total_dist*(411/1000000)*(1-per)
    co2_dia = dist_diaria*(411/1000000)*(1-per)
    
    emis = pred.copy()
    emis['Emisiones CO2 (ton)'] = pred['Emisiones CO2 (ton)']*(1-per_d) + pred['Emisiones CO2 (ton)']*(per_d)*(1-per)

    impacto = pd.concat([pred_past[:30],emis], ignore_index=True)

    # Crear la gráfica combinada de históricos y pronósticos
    fig2 = go.Figure()

    # Datos históricos (línea azul)
    fig2.add_trace(go.Scatter(
        x=pred_past['Fecha'], 
        y=pred_past['Emisiones CO2 (ton)'],
        mode='lines', 
        name='Tendencia del mercado',
        line=dict(color='blue')  # Línea azul
    ))

    # Pronósticos (línea roja punteada)
    fig2.add_trace(go.Scatter(
        x=impacto['Fecha'], 
        y=impacto['Emisiones CO2 (ton)'],
        mode='lines', 
        name=f'Impacto de NYC Liberty Transportation',
        line=dict(color='lawngreen', dash='dot')  # Línea roja punteada
    ))

    # Configuración del gráfico
    fig2.update_layout(
        title='Estimacion de emisiones de CO2',
        title_x = 0.25,
        xaxis_title='Fecha',
        yaxis_title='Emisiones de CO2 (ton)',
        title_font=dict(size=22, family='Arial'),
        xaxis_rangeslider_visible=True
    )

    reduccion =  1 - (impacto['Emisiones CO2 (ton)'][30:].sum() / pred_past['Emisiones CO2 (ton)'][30:].sum())
    col1, col2 = st.columns([1, 2.5], vertical_alignment='center')

    # Mostrar la gráfica en Streamlit
    
    with col2:
        st.plotly_chart(fig2) 

    with col1:
        st.markdown('#### Impacto ambiental 🌎')
        st.metric("Emisiones de CO2 en un dia (ton)", f"{co2_dia:,.2f}")
        st.metric(f"Total emisiones de CO2 en {n_months} meses (ton)", f"{co2:,.2f}")
        st.metric("Reduccion de emisiones:", f"{(reduccion*100):,.2f}%")

    st.markdown("***")

    st.markdown('### Tu flota estaria compuesta por:')

    col1, col2= st.columns(2, gap='large', vertical_alignment='center')

    with col1:
        st.metric(f"Vehiculos convencionales:", f"{int(veh_cov):,}")

    with col2:
        st.metric(f"Vehiculos electricos", f"{int(veh_ele):,}")

    st.markdown('***')

    st.subheader('Selecciona el modelo del vehiculo convencional que quisieras adquirir 🚕')

    eleccion2 = None

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image('App/images/Usado.jpg', width= 350)

    with col2:
        st.image('App/images/Nuevo.jpg', width= 350)

    with col3:
        opcion = ['Usado', 'Nuevo']
        estado = st.radio('Estado del vehiculo', opcion)


    st.markdown('***')

    st.subheader('Selecciona el modelo del vehiculo electrico que quisieras adquirir 🚙')

    evs = pd.read_csv('App/EVs models.csv', index_col='ID')

    eleccion1 = None

    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)

    with col1:
        st.image('App/images/Veh1.jpg')
        if st.button("Elegir", key="grupo1_Opcion 1"):
            eleccion1 = 1
    with col2:
        st.image('App/images/Veh2.jpg')
        if st.button("Elegir", key="grupo1_Opcion 2"):
            eleccion1 = 2
    with col3:
        st.image('App/images/Veh3.jpg')
        if st.button("Elegir", key="grupo1_Opcion 3"):
            eleccion1 = 3
    with col4:
        st.image('App/images/Veh4.jpg')
        if st.button("Elegir", key="grupo1_Opcion 4"):
            eleccion1 = 4
    with col5:
        st.image('App/images/Veh5.jpg')
        if st.button("Elegir", key="grupo1_Opcion 5"):
            eleccion1 = 5
    with col6:
        st.image('App/images/Veh6.jpg')
        if st.button("Elegir", key="grupo1_Opcion 6"):
            eleccion1 = 6

    if eleccion1:

        nombre = evs['Brand_Model'][eleccion1]
        precio_veh_ele = evs['PriceUSD'][eleccion1]
        eff = evs['Efficiency_WhKm'][eleccion1]

        st.write(f'Elegiste el vehiculo electrico: {nombre}')

        st.markdown('***')

        col1, col2 = st.columns(2, gap='large', vertical_alignment='top')

        cost_gas = (dist_diaria/40)*3.42*(1-per) if veh_cov > 0 else 0
        cons_kw = ((dist_diaria*per*1.60934)*eff)/1000 if veh_ele > 0 else 0
        cost_kw = cons_kw*0.2

        if estado == 'Usado':
            precio_conv = 15000
        else:
            precio_conv = 27500

        cost_veh_conv = veh_cov*precio_conv
        cost_veh_ele = precio_veh_ele*veh_ele
        cost_veh = cost_veh_ele + cost_veh_conv

        with col1:
            st.subheader('Inversion Inicial 💵')
            st.metric("Costo de vehiculos convencionales (USD)", f"${cost_veh_conv:,.2f}")
            st.metric("Costo de vehiculos electricos (USD)", f"${cost_veh_ele:,.2f}")
            st.metric("Costo total de la flota (USD)", f"${cost_veh:,.2f}")

        with col2:
            st.subheader('Gasto Operacional ⛽')
            st.metric("Costo de gasolina (USD)", f"${cost_gas:,.2f}")
            st.metric("Costo de watts (USD)", f"${cost_kw:,.2f}")
            st.metric("Costo total de combustible en un dia (USD)", f"${(cost_kw+cost_gas):,.2f}")

        st.markdown('***')

        st.subheader('Mantenimiento ⚙')
        col3, col4, col5  = st.columns(3, gap='large', vertical_alignment='top')

        with col3:
            st.markdown('##### Vehiculos Convencionales') 
            mant_conv = 3000
            st.metric("Costo anual por vehiculo", f"${mant_conv:,.2f}")
            st.metric("Costo anual flota convencional", f"${mant_conv*veh_cov:,.2f}")

        with col4:
            st.markdown("##### Vehiculos Electricos")
            mant_ele = 1650
            st.metric("Costo anual por vehiculo", f"${mant_ele:,.2f}")
            st.metric("Costo anual flota electrica", f"${mant_ele*veh_ele:,.2f}")

        with col5: 
            mant_total=(mant_ele*veh_ele)+(mant_conv*veh_cov)
            st.markdown("##### Flota total")
            st.metric(f"Costo anual mantenimiento flota", f"${mant_total:,.2f}")      

        st.markdown('***')

        col3, col4, col5 = st.columns(3, gap='large', vertical_alignment='top')

        with col3:
            st.subheader("Ingresos 💰")
            ingresos_diarios = (total_usd / dias_pred) * per_d
            st.metric(f"Ingreso en un dia (USD)", f"${ingresos_diarios if ingresos_diarios > 0 else 0:,.2f}")
            st.metric(f"Ingreso total en {n_months} meses (USD)", f"${(total_usd*per_d) if (total_usd*per_d) > 0 else 0:,.2f}")

        with col4:
            st.subheader("Utilidad 🤑")
            seguro=833*vehiculos_necesarios
            admin=4500*(vehiculos_necesarios/75)
            mant=mant_total/12
            comb=(cost_kw+cost_gas)*30

            utilidad_mes = (ingresos_diarios*30)-seguro-admin-mant-comb

            st.metric(f"Utilidad estimada en un dia (USD)", f"${(utilidad_mes)/30 if vehiculos_necesarios > 0 else 0:,.2f}")
            st.metric(f"Utilidad total estimada en {n_months} meses (USD)", f"${(utilidad_mes*n_months) if vehiculos_necesarios > 0 else 0:,.2f}")

        with col5:
            import math
            tiempo = math.ceil(cost_veh/utilidad_mes)
            st.subheader("Periodo de Recuperacion 📆")
            st.metric("Costos asociados: Combustible, Mantenimiento, Seguro y Salarios",f"{tiempo} meses")


        with col4:
            st.empty()

        
    else:
        st.warning('Debes seleccionar un vehiculo electrico')

