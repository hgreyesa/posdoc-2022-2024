from bson import ObjectId
from pymongo import MongoClient
import pandas as pd
import logging
import datetime

from dbCon import *

ct = datetime.datetime.now()
cname = "logs_db/establecimientos_update_nombre_municipios_"+str(ct) + ".log"
logging.basicConfig(filename=cname, filemode='a', level=0, format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
rootLogger = logging.getLogger()
consoleHandler = logging.StreamHandler()
rootLogger.addHandler(consoleHandler)

    

cantidad_modificaciones = 0
logging.info("Se establece la conexión con la base de datos")
mc = getMongoClientSemarnatWriter()
db = getDbCollectionSemarnat(mc, "semarnat")

#estab_2024_v6_modificaciones_mun


input_path="datos_resumenes/estab_2024_v6_modificaciones_mun.csv"
logging.info("Se lee el contenido del archivo {}".format(input_path))

df = pd.read_csv(input_path, low_memory=False, encoding='utf-8', sep="\t")

logging.info("Se corrigen los nombres de los municipios con inconsistencias")
for index, datos in df.iterrows():
    try:

        logging.info("Actualizando las datos del municipio {} por {} del estado de {}:".format(datos["mun"], datos["mod"],datos["estado"]))


        #num.zfill(3)

        result = db.estab_2024_v6.update_many(
            #Se localiza la emisoras por el nombre del estado
            {
                "estado":datos["estado"],
                "municipio":datos["mun"]
            },
            #Proceso de actualizacion
            {
                #Listado de parámetros por actualizar
                "$set":{
                    "municipio":datos["mod"],
                    #"cve_mun":"01"
                }
            }
        )
        print("\tRegistros localizados: {}".format(result.matched_count))
        print("\tRegistros actualizados: {}".format(result.modified_count))
        cantidad_modificaciones += result.modified_count

    except Exception as e:
        logging.info("An exception occurred ::", e)
        

print("\tTodal de actualizaciones realizadas: {}".format(cantidad_modificaciones))
