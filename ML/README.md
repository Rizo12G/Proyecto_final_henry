<h1 align='center'>
<b>Modelo de Predicción (Machine Learning)</b>
</h1>
<p align="center">

## Objetivo
Desarrollar un modelo de predicción del mercado de taxis en la ciudad de Nueva York a *un año* (septiembre 2024 - agosto 2025) del cual se obtendrá el *número de viajes* y su comportamiento. A partir de esta información se calcularan los siguientes KPI's:<br>

  - Utilidad mensual según la flota de vehículos adquirida.
  - Emisiones de CO2 por año. <br>
  
Para estos calculos se empleara la siguiente infomarcion como promedio extraida de la bases de datos o investigaciones adicionales:<br>

  - Valor pagado mensual
  - Distancia recorrida mensual
  - Numero de pasajeros mensual
  - Eficiencia (consumo) por kilometro
  - Costo de combustible (kWh o gal)
  - Emisiones de CO2 por kilometro<br>

## Metodologia
Para alcanzar este objetivo se desarrollará un **modelo de Machine Learning de aprendizaje no supervisado** a traves de un análisis de *Series de Tiempo*. Los valores y calculos obtenidos a partir de este modelo seran desplegados en un portal web elaborado usando la libreria Streamlit.

## Modelo
![modelo_ML](/imagenes/modelo_ML.jpg)

## Tecnologias

Se empleará para este analisis el software Visual Studio Code en lenguaje Python. De este ultimo se emplearon las siguientes libreias: <br>

- Pandas
- Numpy
- Matplotlib
- Seaborn
- Scikit Learn
- StatsModels
- Prophet

## Análisis preliminar

### Estacionalidad
![dist_dia_sem](/imagenes/dist_dia_sem.jpg)

![dist_dia_mes](/imagenes/dist_dia_mes.jpg)

![dist_sem_mes](/imagenes/dist_sem_mes.jpg)

### Tendencia

![trend](/imagenes/trend.jpg)
