import pandas as pd #Importación de librería pandas para la lectura del archivo y manejo del dataframe
#Carga del dataset
df_combustible = pd.read_csv('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/FuelConsumptionCo2.csv')
#Conversión del dataframe en diccionario para el posterior uso del método GET del servidor
ConsumosCombustibles = df_combustible.to_dict(orient='records')