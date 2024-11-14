<h1 align='center'>
<b>Modelo de Predicción (Machine Learning)</b>
</h1>
<p align="center">

## Objetivo
Desarrollar un modelo de predicción del mercado de taxis en la ciudad de Nueva York a *un año* (septiembre 2024 - agosto 2025) del cual se obtendrá el *número de viajes* y su comportamiento. Esto ayudará a dimensionar la flota de transporte, el personal o los recursos necesarios para asegurar una mejor planeación y ditribución. A partir de esta información se podria calcular los siguientes KPI's:<br>
 
  - Utilidad mensual según la flota de vehículos adquirida.
  - Emisiones de CO2 por año. <br>
  
Para estos calculos se emplearia la siguiente informacion adicional como promedio extraida de la bases de datos o investigaciones adicionales:<br>

  - Valor pagado mensual
  - Distancia recorrida mensual
  - Numero de pasajeros mensual
  - Eficiencia (consumo) por kilometro
  - Costo de combustible (kWh o gal)
  - Emisiones de CO2 por kilometro<br>

## Modelo
![modelo_ML](/imagenes/modelo_ML.jpg)

## Metodologia
Se desarrollará a partir del dataset de *taxis* un **modelo de Machine Learning de aprendizaje no supervisado** a traves de un análisis de *Series de Tiempo*. Para comenzar se realizara un analisis preliminar del comportamiento del numero de viajes para diferentes frecuencias de muestreo que se obtendran haciendo uso de la funcion *resample*. <br> Se evaluaran diferentes modelos de prediccion:<br>
- Procesos AR (AutoRegressive) 
- Procesos AM (Moving Average)
- ARIMA (AutoRegressive Integrated Moving Average)
- SARIMA (Seasonal AutoRegressive Integrated Moving Average)
- Prophet
  
Para comparar los modelos se emplearan las siguientes metricas:
- *Coverage (Cobertura de los Intervalos de Incertidumbre ):* Es clave porque ayuda a evaluar cuán confiable es la predicción y si el sistema estará preparado para escenarios extremos (alta demanda o baja demanda). <br>
- *MAE (Mean Absolute Error):* Es util para tener una medida clara del error promedio en el número de viajes que estás prediciendo. Es decir, cual es la cantidad de viajes se esta desviando de la prediccion y si la operacion estaria en la capacidad de cubrirlos.
- *RMSE (Root Mean Squared Error):* Permite tener en cuenta los picos de demanda o eventos especiales (como días festivos o eventos deportivos) que generan una alta variabilidad en el número de viajes.

Los valores y calculos obtenidos a partir de este modelo seran desplegados en un portal web elaborado usando la libreria *Streamlit*.

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

### Estacionariedad

Para los modelos *ARIMA* y *SARIMA* es necesario contar con series estacionarias. Para determinar la estacionariedad de cada serie temporal se empleo el test de Dickey-Fuller. Una serie se considera *estacionaria* si su p-value es menor a 0.05. Los resultados que se obtuvieron fueron los siguientes:

- **Diario:** Es estacionaria (p-value 0.017)
- **Semanal:** Es estacionaria (p-value 0.019)
- **Mensual:** No es estacionaria (p-value 0.479)

De acuerdo con esto, fue necesario realizar un proceso de diferenciacion de la serie *Mensual*. Debido al numero de registros (12) no fue posible realizar una diferenciacion estacional (realizar un desplazamiento de 12 registros) por lo cual se realizo una de primer orden. Al aplicarlo se obtuvo una serie con p-value de 0.002. La serie diferenciada quedó de la siguiente manera.
![men_diff](/imagenes/men_diff.jpg)

