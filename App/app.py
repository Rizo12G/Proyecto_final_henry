 
import streamlit as st

st.set_page_config(page_title="NYC Taxis Predictor", page_icon="🚕", layout="wide")

pagina1 = st.Page(
    page = 'pages/Home.py',
    title = 'Home',
    icon = ':material/home:', 
    default= True,)

pagina2 = st.Page(
    page = 'pages/BI.py',
    title = 'Business Intelligence',
    icon = ':material/finance:')

pagina3 = st.Page(
    page = 'pages/ML.py',
    title = 'Forecasting',
    icon = ':material/timeline:')

pg = st.navigation(pages=[pagina1, pagina2, pagina3])
pg.run()

st.logo('images/logo.jpg')
st.sidebar.text('Data Vision. 2024')