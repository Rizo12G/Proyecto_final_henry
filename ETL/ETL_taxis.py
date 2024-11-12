import pandas as pd
import numpy as np

print('Se inició el ETL')

# Carga archivo
taxis = pd.read_parquet('C:\\Users\\Carolina\\Documents\\Proyecto_final_henry\\ETL\\taxis.parquet')
print('Se cargó el archivo')

# Borra duplicados
taxis.drop(taxis[taxis.duplicated()].index, inplace=True)
print('Se borraron los duplicados')

# Borra columnas sin info
taxis.drop(columns=['ehail_fee','VendorID'], inplace=True)
print('Se borraron las columnas innecesarias')

# Llena vacios
## Con moda
l_mod = ['RatecodeID','store_and_fwd_flag','payment_type',
         'trip_type','congestion_surcharge','Airport_fee']

for i in l_mod:
    mod = taxis[i].mode().iloc[0]
    taxis[i] = taxis[i].fillna(mod)
print('Se hicieron los reemplazos con la moda')

## Con media
taxis['passenger_count'] = taxis['passenger_count'].fillna(taxis['passenger_count'].mean()).astype(int)
print('Se hicieron los reemplazos con el promedio')

# Tratamiento de  errores
## Reemplazo
mod = taxis['RatecodeID'].mode().iloc[0]
taxis['RatecodeID'] = taxis['RatecodeID'].apply(lambda x : mod if x == 99 else x)

taxis['passenger_count'] = taxis['passenger_count'].apply(lambda x : 1 if x == 0 else x)

taxis['payment_type'] = taxis['payment_type'].apply(lambda x : x + 1)
print('Se hicieron los reeemplazos de valores inusuales')

## Eliminacion
taxis.drop(taxis[~((taxis['tpep_dropoff_datetime'].dt.year==2023)|
                   (taxis['tpep_dropoff_datetime'].dt.year==2024)|
                   (taxis['tpep_pickup_datetime'].dt.year==2023)|
                   (taxis['tpep_pickup_datetime'].dt.year==2024))].index, inplace=True)
print('Se eliminaron las fechas fuera del periodo')

# Intercambio
taxis['pickup_datetime'] = np.minimum(taxis['tpep_dropoff_datetime'], taxis['tpep_pickup_datetime'])
taxis['dropoff_datetime'] = np.maximum(taxis['tpep_dropoff_datetime'], taxis['tpep_pickup_datetime'])

taxis.drop(columns=['tpep_pickup_datetime','tpep_dropoff_datetime'], inplace=True)
print('Se corrigieron las fechas')

# Creacion de variable 'duration'
taxis['duration'] = taxis['dropoff_datetime'] - taxis['pickup_datetime']
taxis['duration'] = taxis['duration'].dt.total_seconds() / 60
print('Se creó la columna "duration"')

# Manejo de neagtivos
l_abs = ['fare_amount','extra','mta_tax','tip_amount','tolls_amount',
         'total_amount','improvement_surcharge','congestion_surcharge','Airport_fee']

for i in l_abs:
    taxis[i] = abs(taxis[i])
print('Se transformaron los negativos')

tot = taxis.shape[0]

# Manejo de Outliers
# Valores discretos
def out_def (col):
    '''
    Funcion que identifica todos los valores con menos del 1% de registros
        Parametros:
            col (str): Nombre de la columna
        Retorno: Lista con los valores correspondientes (list)
    '''
    l = []
    for index, row in taxis[col].value_counts().to_frame().iterrows():
        if row['count'] < tot*0.01:
            l.append(index)
    return l

l_out1 = ['passenger_count','improvement_surcharge','congestion_surcharge','Airport_fee']
for i in l_out1:
    l = out_def(i)
    taxis.drop(taxis[taxis[i].isin(l)].index, inplace=True)
print('Se eliminaron los Outliers discretos')

#Valores continuos
def outliers (col):
    '''
    Funcion que calcula el limite maximo segun BoxPlot
        Parametros:
            col (str): Nombre de la columna
        Retorno: Limite maximo (float)
    '''
    Q3 = float(taxis[col].quantile(0.75))
    Q1 = float(taxis[col].quantile(0.25))
    RIC = Q3 - Q1

    Max = Q3 + 1.5*RIC

    return Max

l_out2 = ['fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount', 'total_amount', 'trip_distance','duration']
for i in l_out2:

  m = outliers(i)
  taxis.drop(taxis[taxis[i]>m].index, inplace=True)
print('Se eliminaron los Outliers continuos')

taxis.to_parquet('C:\\Users\\Carolina\\Documents\\Proyecto_final_henry\\clean_data\\taxis_def.parquet')
print('Se exportó el archivo')