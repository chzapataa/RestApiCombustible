from flask import Flask #Importación de librería para la construcción del API REST
from flask import jsonify #Importación del método que convierte objetos a json
from Combustible import ConsumosCombustibles #Importación del dataset Consumo combustible
from Regresion import RegresionLineal

app = Flask(__name__) # nombre del módulo o paquete

@app.route('/ConsumoCombustible') #Método GET
def ListarConsumoCombustible(): #Función que devuelve el listado completo de consumo de combustible  
    return jsonify(ConsumosCombustibles) 

@app.route('/ConsumoCombustible/<string:MAKE>') #Método GET, el usuario puede consultar por una marca
def ConsumoCombustiblexMarca(MAKE):
    #Itera los elementos de la lista y trae las marcas que el usuario indique
    Marcas=[item for item in ConsumosCombustibles if item['MAKE'] == MAKE]  
    if len(Marcas)>0: #Si el usuario ingresa una marca que no existe
        return jsonify(Marcas)
    return ({"Mensaje":"Marca no encontrada"})    

@app.route('/RegresionLineal')
def FRegresionLineal(): #Función que devuelve la pendiente y la intersección de la regresión lineal
    respuesta=RegresionLineal()
    coeficientea="".join(map(str, respuesta[0])) #conversión del array a string para ser enviado en formato json
    coeficienteb="".join(map(str, respuesta[1]))
    return jsonify({"Message:":"Valor de la pendiente o coeficiente a y el valor de la interseccion o coeficiente b respectivamente es:",
    "coeficiente a":coeficientea,
    "coeficiente b":coeficienteb})

if __name__ == '__main__':
    app.run(debug=True) #debug=true para que cualquier cambio rienicie el servidor  
                        #puerto por defecto: 5000