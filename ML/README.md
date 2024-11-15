<h1 align='center'>
<b>Modelo de Machine Learning</b>
</h1>

![Portada ML](/imagenes/PortadaML.jpg)


En esta carpeta se encuentra la informacion, datos y analisis correpondientes al modelo de Machine Learning:

- [**Carpeta raw:**](/raw) Archivos csv para cada frecuencia escogida (diario, semanal y mensual) generado usando la funcion *resample*
- [**Analisis_preliminar_ML:**](Analisis_preliminar_ML.ipynb) Notebook con el analisis preliminar de las series de tiempo
- [**Eleccion_modelos_ML:**](Eleccion_modelos_ML.ipynb) Notebook con las primeras aproximaciones al modelo de prediccion

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
Se desarrollará a partir del dataset de *taxis* un **modelo de Machine Learning de aprendizaje no supervisado** a traves de un análisis de *Series de Tiempo* debido a que los datos estan intrinsecamente ordenados cronologicamente. Se utilizara esta tecnica ya que es crucial identificar patrones y tendencias, para anticipar el comportamiento futuro. Para comenzar, se realizara un analisis preliminar del comportamiento del numero de viajes para diferentes frecuencias de muestreo que se obtendran haciendo uso de la funcion *resample*. <br> Se evaluaran diferentes modelos de prediccion:<br>
- Procesos AR (AutoRegressive) 
- Procesos AM (Moving Average)
- ARIMA (AutoRegressive Integrated Moving Average)
- SARIMA (Seasonal AutoRegressive Integrated Moving Average)
- Prophet
  
Para comparar los modelos se emplearan las siguientes metricas:
- **Coverage (Cobertura de los Intervalos de Incertidumbre ):** Es clave porque ayuda a evaluar cuán confiable es la predicción y si el sistema estará preparado para escenarios extremos (alta demanda o baja demanda). <br>
- **MAE (Mean Absolute Error):** Es util para tener una medida clara del error promedio en el número de viajes que estás prediciendo. Es decir, cual es la cantidad de viajes se esta desviando de la prediccion y si la operacion estaria en la capacidad de cubrirlos.
- **RMSE (Root Mean Squared Error):** Permite tener en cuenta los picos de demanda o eventos especiales (como días festivos o eventos deportivos) que generan una alta variabilidad en el número de viajes.

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

A continuacion, se examinan las tendencias y patrones del número de viajes en taxis a diferentes frecuencias temporales (diaria, semanal y mensual) para determinar cuál de estas es la más adecuada para generar modelos predictivos confiables y robustos que puedan ser útiles en la toma de decisiones de inversión.

### Distribucion del numero de viajes en taxi

Se analizó como varía la demanda de taxis dependiendo del contexto temporal para identificar patrones importantes, tales como picos de demanda, estacionalidad y ciclos.
<br><br>
![dist_dia_sem](/imagenes/dist_dia_sem.jpg)
<br><br>
**Distribucion por dia de la semana:** La tendencia semanal muestra un comportamiento bastante consistente a lo largo de los días, con los valores más altos concentrándose entre el martes y el sábado. Los sábados son los días con mayor número de viajes seguido por los viernes, lo cual sugiere que una mayor actividad y demanda los fines de semana. <br> Se puede observar tambien que existe estacionalidad semanal y que sigue un ciclo al tener los valores mas bajos en el domingo y lunes.<br>
Se observan outliers sin embargo todos son hacia la bajo, lo cual podria ser explicado por algun evento puntual dentro del año.
<br><br>
![dist_dia_mes](/imagenes/dist_dia_mes.jpg)
<br><br>
**Distribucion por dia del mes:** Se observa que la distribución de viajes por día del mes tiende a ser relativamente consistente con un leve aumento en los primeros dias del mes con respecto a los ultimos lo cual parece suceder de manera ciclica. No se presenta una estacionalidad marcada al interno de los meses. Nuevamente se presentan outliers hacia la parte inferior que, al estar analizando unicamnete un año, podrian deberse a alguna festividad o evento.
<br><br>
![dist_sem_mes](/imagenes/dist_sem_mes.jpg)
<br><br>
**Distribucion de semanas por mes:** Se puede observar una tendencia claramente estacional, donde los viajes comienzan bajos en los primeros meses (enero y febrero) yalcanzan un pico alrededor de los meses de junio y julio. Después de julio, el número de viajes disminuye gradualmente, mostrando un mínimo notable en septiembre. Este comportamiento coincide con el comportamiento estacional del clima en la ciudad a lo largo de año. En este ultimo grafico tambien se presentan outliers hacia la parte inferior lo cual coincide con lo observado en los graficos anteriores. <br><br>
Se puede concluir que el comportamiento de los viajes en taxis en la ciudad de Nueva York durante el año de estudio muestra patrones estacionales a nivel diario, semanal, mensual y anual. La demanda de taxis posiblemente influenciada por factores como el clima, los eventos festivos, las vacaciones, y las actividades de ocio durante el fin de semana.

### Tendencia
Como parte del análisis se reviso tambien la tendencia de los viajes en tres frecuencias diferentes: diaria, semanal, y mensual. En cada uno de estos gráficos se observa la serie de tiempo real y la media movil para suavizar la tendencia y facilitar el analisis.
<br><br>
![trend](/imagenes/trend.jpg)

Se puede observar que en terminos generales para todas las frecuencias se presenta la misma tendencia a lo largo del año. Sin embargo, es posible apreciar que en el caso diario y semanal esta es un poco mas volatil y que en la mensual es mas claro y definido. Para la frecuencia **diaria** es posible obsevar que los datos presentan una clara oscilación con picos y valles constantes, que reflejan una variabilidad alta. Sin embargo, la linea de media movil se muestra relativamente constante. A nivel **semanal**, se percibe una mayor estabilidad en comparación con la frecuencia diaria, pero aún existe una cierta oscilación marcada. En este caso la linea de media movil muestra una tendencia levemente decreciente. Finalmente, para la serie **mensual** se puede observar una tendencia marcada de aumento y luego disminución en el número de viajes lo cual indica una estacionalidad **anual** clara.

### Anomalias

- **Frecuencia diaria:** Se observan varios picos fuera de la tendencia que pueden ser considerados anomalías, posiblemente debido a eventos especiales o climaticos
- **Frecuencia semanal:** Hay algunas caídas bruscas y picos en la serie de tiempo semanal, que podrían reflejar semanas con cambios drásticos en la movilidad que podrian estar relacionados con festividades.
- **Frecuencia mensual:** La variabilidad a nivel mensual es menor comparada con las otras frecuencias, lo que indica una mayor estabilidad en el promedio mensual.<br>

Con el fin de tener un modelo mas estable se realizo una interpolacion para algunos valores de las series diaria y semanal.

### Estacionariedad

Para los modelos *ARIMA* y *SARIMA* es necesario contar con series estacionarias. Para determinar la estacionariedad de cada serie temporal se empleo el test de Dickey-Fuller. Una serie se considera *estacionaria* si su p-value es menor a 0.05. Los resultados que se obtuvieron fueron los siguientes:

- **Diario:** Es estacionaria (p-value 0.017)
- **Semanal:** Es estacionaria (p-value 0.019)
- **Mensual:** No es estacionaria (p-value 0.479)

De acuerdo con esto, fue necesario realizar un proceso de diferenciacion de la serie *Mensual*. Debido al numero de registros (12) no fue posible realizar una diferenciacion estacional (realizar un desplazamiento de 12 registros) por lo cual se realizo una de primer orden. Al aplicarlo se obtuvo una serie con p-value de 0.002. La serie diferenciada quedó de la siguiente manera.

![men_diff](/imagenes/men_diff.jpg)

