<h1 align='center'>
<b>Modelo de Machine Learning</b>
</h1>

![Portada ML](/imagenes/PortadaML.jpg)


En esta carpeta se encuentra la informacion, datos y analisis correpondientes al modelo de Machine Learning:

- [**Carpeta raw:**](/raw) Archivos csv para cada frecuencia escogida (diario, semanal y mensual) generado usando la funcion *resample*. Incluye los 2.5 alos que se adicionaron al modelo.
- [**Analisis_preliminar_ML_extendido:**](Analisis_preliminar_ML_extendido.ipynb) Notebook con el analisis preliminar de las series de tiempo que incluye el periodo adicional.
- [**Modelos_ARIMA_SARIMA:**](Modelos_ARIMA_SARIMA.ipynb) Notebook con las primeras aproximaciones al modelo de prediccion (ARIMA y SARIMA).
- [**Modelo_Prophet:**](Modelo_Prophet.ipynb) Notebook con el modelo de prediccion definitivo implementado en Prophet.

## Tabla de Contenido
1. [Objetivo](#objetivo)
2. [Planificacion del Modelo](#modelo)
3. [Metodologia](#metodologia)
4. [Tecnologias](#tecnologias)
5. [Analisis Preliminar](#análisis-preliminar)
   - [Distribucion](#distribucion-del-numero-de-viajes-en-taxi)
   - [Tendencia](#tendencia)
   - [Anomalias](#anomalias)
   - [Estacionariedad](#estacionariedad)
6. [Seleccion del modelo](#seleccion-del-modelo)
   - [Eleccion de la frecuencia temporal](#eleccion-de-la-frecuencia-temporal)
   - [Eleccion de tecnica/enfoque](#eleccion-de-tecnicaenfoque)
7. [Resultado final](#resultado-final)
8. [Conclusiones Finales](#conclusiones-finales)
9. [Despliegue (Aplicacion Web)](#despliegue-aplicacion-web)

## Objetivo
Desarrollar un modelo de predicción del mercado de taxis en la ciudad de Nueva York a *un año* (septiembre 2024 - agosto 2025) del cual se obtendrá el *número de viajes* y su comportamiento. Esto ayudará a dimensionar la flota de transporte, el personal o los recursos necesarios para asegurar una mejor planeación y ditribución. A partir de esta información se podria calcular los siguientes KPI's:<br>
 
  - Utilidad según la flota de vehículos adquirida.
  - Emisiones de CO2. <br>
  
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

- ARIMA (AutoRegressive Integrated Moving Average)
- SARIMA (Seasonal AutoRegressive Integrated Moving Average)
- Prophet
- Redes Neuronales
  
Para comparar los modelos se emplearan las siguientes metricas:
- **Coverage (Cobertura de los Intervalos de Incertidumbre ):** Es clave porque ayuda a evaluar cuán confiable es la predicción y si el sistema estará preparado para escenarios extremos (alta demanda o baja demanda). <br>
- **MAE (Mean Absolute Error):** Es util para tener una medida clara del error promedio en el número de viajes que estás prediciendo. Es decir, cual es la cantidad de viajes se esta desviando de la prediccion y si la operacion estaria en la capacidad de cubrirlos.
- **MAPE (Mean Absolute Percentage Error):** Debido a que se trabaja con valores del orden de los millones, es importante esta metrica para poder dimensionar la magnitud del resultado del MAE.

Los valores y calculos obtenidos a partir de este modelo seran desplegados en un portal web elaborado usando la libreria *Streamlit*.

## Tecnologias

Se empleará para este analisis el software Visual Studio Code en lenguaje Python. De este ultimo se emplearon las siguientes libreias: <br>

- Pandas
- Numpy
- Matplotlib
- Seaborn
- Pyplot
- Scikit Learn
- StatsModels
- Prophet
- Streamlit

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

## Seleccion del modelo

Para el desarrollo de este modelo el enfoque principal fue lograr predicciones precisas y confiables que permitan la toma de decisiones estratégicas en el mercado de taxis. De acuerdo con esto, se tuvo en cuenta 2 criterios principales: la frecuencia temporal y la tecnicas de modelado. Se realizó una primera ronda de modelos sin embargo no se obtuvo resultados suficientemente buenos para considerar que se habia llegado a un modelo optimo. Debido a esto, se tomo la decision de adicionar a los datos historicos 2.5 años mas, es decir, se realizo el analisis desde marzo de 2022 a agosto 2024.

### Eleccion de la frecuencia temporal

En el momento de seleccionar la serie de tiempo se tuvo en cuenta que el objetivo era realizar un modelo que pudiera realizar predicciones a largo plazo. De acuerdo con esto, se observo que las series *diarias* y *semanales* eran demasiado sensibles a las variaciones en los datos por lo que no presentaban una tendencia lo suficientemente estable para representar los datos historicos y los futuros. Por el lado de la serie **mensual** se obtuvo una tendencia suave con estacionalidad anual lo cual se considero ideal para las necesidades del modelo.

### Eleccion de tecnica/enfoque

Una vez se selecciono la frecuencia a emplear se paso a revisar las diferentes tecnicas disponibles. Teniendo en cuenta los enfoques mecionados anteriormente se decidió comenzar desde el mas simple (ARIMA) al mas complejo (Redes Neuronales) con el fin de lograr un buen modelo de prediccion con la menor cantidad de recursos computacionales. Para los modelos de **ARIMA** y **SARIMA** se empleo la *serie diferenciada* de la frecuencia mensual y su posterior conversion a datos reales. A pesar de realizar esta adaptacion de los datos no fue posible llegar a un modelo que proyectara el numero de viajes de una manera coherente. Esto es posible observarlo en las siguientes graficas.

![ARIMA_SARIMA](/imagenes/ARIMA-SARIMA.png)

Debido a estos resultados se continuo con la implementacion de los modelos de **Prophet** y **Redes Neuronales**. Sin embargo, se obtuvo buenos resultados con la implementacion de Prophet por lo que no se termino el modelado en Redes.

## Resultado final

### Resultado de metricas
El modelo se ajusto de manera iterativa hasta lograr una estabilizacion de las metricas respecto a la variacion de los hiperparametros, se lograron valores apropiados para las métricas clave seleccionadas que validan la calidad de las predicciones:<br>

<p align="center">
  <img src="/imagenes/metricas.jpg" alt="Metricas" width="250">
</p>

Para alcanzar estos resultados, los hiperparámetros del modelo quedaron de la siguiente manera: <br>

<p align="center">
  <img src="/imagenes/hiperparametros.jpg" alt="Hiperparametros" width="250">
</p>

### Visualizaciones

Para complementar los resultados arrojados por las metricas de evaluacion a continuacion se presentan las graficas que se crearon y sirvieron como primera aproximacion para revisar la fiabilidad del modelo.

1. **Predicción Mensual del Número de Viajes**
   ![predicciones](/imagenes/prediccion%20mensual%20d%20enumero%20de%20viajes%20en%20taxis.png)


2. **Componentes del Modelo**
   ![componentes](/imagenes/componentes%20de%20las%20series%20de%20tiempo.png)


3. **Comportamiento de metricas** <br>
    ![metricas](/imagenes/validacion%20cruzada.png)


4. **Datos reales y pronostico**
    ![Pronostico](/imagenes/historico%20y%20pronostico.png)

## Conclusiones Finales

El modelo generado con Prophet permitió realizar proyecciones robustas y detallada presentando un **MAPE** inferior al 10% y una **Cobertura** superior al 90% demostrando su capacidad para captar patrones estacionales y tendencias clave en el mercado de taxis. Con estos resultados se considera que las predicciones cubres en gran medida las variaciones de demanda y la flota estimada a partir de estas puede estar en capacidad de cubrirla. Este enfoque proporciona una base sólida para futuras decisiones basadas en datos y análisis financiero. El metodologia empleada en el modelo definitivo fue la siguiente.

![Modelo Definitivo](/imagenes/ModeloDefinitivo.png)

## Despliegue (Aplicacion Web)

Para desplegar los resultados del modelo obtenido se realizó una aplicación implementando Streamlit y programada en Python, garantizando una interfaz interactiva y accesible para los usuarios, permitiendo obtener resultados y métricas clave tanto en términos financieros como ambientales. <br>
Gracias a estas herramientas, es posible explorar y analizar en profundidad el mercado de taxis en la ciudad de Nueva York, proporcionando un análisis detallado de los datos disponibles. Podras encontrar las siguientes estimaciones:

- Precios de mercado de vehiculos
- Inversion inicial en flota de vehiculos
- Costo de combustible diaria y del periodo de analisis
- Costo anual de mantenimiento
- Emisiones de CO2
- Ingreso diario y del periodo de analisis

Puedes encontrar esta herramienta [aqui](https://nyc-taxis-predict.streamlit.app/) y todo el detalle de su implementacion en la carpeta [App](App).

<p align="center">
  <img src="/App/images/portada.jpg" alt="Portada aplicacion web" width="500">
</p>
