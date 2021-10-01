def RegresionLineal():
    from sklearn import linear_model #importación de librería para utilizar el modelo de regresión lineal
    from Combustible import df_combustible #Importación del dataset Consumo combustible

    #Columnas con relación lineal simple
    ENGINESIZE=df_combustible["ENGINESIZE"]
    CO2EMISSIONS=df_combustible["CO2EMISSIONS"]

    #se vectorizan las columnas
    X_train=ENGINESIZE.to_numpy()
    y_train=CO2EMISSIONS.to_numpy()
   
    lr = linear_model.LinearRegression()#Instancia del modelo de regresión lineal

    #Se transforman los arreglos a una sola columna
    X_train=X_train.reshape(-1,1)
    y_train=y_train.reshape(-1,1)

    #Se entrena el modelo
    lr.fit(X_train, y_train)

    coeficientea=lr.coef_ #Se obtiene la pendiente de la regresión
    coeficienteb=lr.intercept_ #Se obtiene el intercepto de la regresión
    return coeficientea,coeficienteb   