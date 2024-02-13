from bson import ObjectId
from pymongo import MongoClient
import pandas as pd
import logging
import datetime

from dbCon import *

ct = datetime.datetime.now()
cname = "logs_db/analisis_obtener_estado_municipio_mismo_nra_update_"+str(ct) + ".log"
logging.basicConfig(filename=cname, filemode='a', level=0, format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
rootLogger = logging.getLogger()
consoleHandler = logging.StreamHandler()
rootLogger.addHandler(consoleHandler)

    
logging.info("Se establece la conexión con la base de datos")
mc = getMongoClientSemarnatReader()
db = getDbCollectionSemarnat(mc, "semarnat")



input_path="output/03_Listado_nra_contador_de_estados_municipios_distintos.csv"
logging.info("Se lee el contenido del archivo {}".format(input_path))

df = pd.read_csv(input_path, low_memory=False, encoding='utf-8', sep=",")
columnassalida = {"nra":[],"estado":[], "municipio":[], "posicion":[],"total":[]} 
salida = pd.DataFrame(columnassalida)

datos_temp = []
for index, emisora in df.iterrows():

    try:
        logging.info("Obteniendo los estados/municipios del NRA: {}".format(emisora["nra"]))

        result = db.estab_2024_v6.aggregate(
            [
                {
                    '$match': {
                        'nra': emisora["nra"]
                    }
                }, {
                    '$group': {
                        '_id': {
                            'nra': '$nra', 
                            'estado': '$estado', 
                            'municipio': '$municipio'
                        }
                    }
                }, {
                    '$project': {
                        '_id': 0, 
                        'nra': '$_id.nra', 
                        'estado': '$_id.estado', 
                        'municipio': '$_id.municipio'
                    }
                }
            ]
        )
        posicion = 0
        for datos in result:
            posicion +=1
            datos_temp.append({
                "nra":datos["nra"],
                "estado":datos["estado"],
                "municipio":datos["municipio"],
                "posicion":posicion,
                "total":emisora["contador_comb"],
            })
            logging.info("nra: {}, estado: {}, municipio: {} {}/{} ".format(datos["nra"], datos["estado"], datos["municipio"], posicion, emisora["contador_comb"]))



        
    except Exception as e:
        logging.info("An exception occurred ::", e)
            #return False

new_df = pd.DataFrame.from_dict(datos_temp)
new_df.to_csv("04_nra_estados_municipios_distintos.csv", sep="\t", header=True, index=False)


