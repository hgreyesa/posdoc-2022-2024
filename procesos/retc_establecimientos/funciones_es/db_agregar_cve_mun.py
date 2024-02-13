from bson import ObjectId
from pymongo import MongoClient
import pandas as pd
import logging
import datetime

from dbCon import *

ct = datetime.datetime.now()
cname = "logs_db/establecimientos_update_cve_municipios_"+str(ct) + ".log"
logging.basicConfig(filename=cname, filemode='a', level=0, format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
rootLogger = logging.getLogger()
consoleHandler = logging.StreamHandler()
rootLogger.addHandler(consoleHandler)

    

cantidad_modificaciones = 0

logging.info("Se establece la conexión con la base de datos")
mc = getMongoClientSemarnatWriter()
db = getDbCollectionSemarnat(mc, "semarnat")

#estab_2024_v6_modificaciones_mun


input_path="datos_resumenes/estab_2024_v6_cve_est_mun.csv"
logging.info("Se lee el contenido del archivo {}".format(input_path))

df = pd.read_csv(input_path, low_memory=False, encoding='utf-8', sep=",")


logging.info("Se agrega la columna cve_mun")
try:
    result = db.estab_2024_v6.update_many({},{"$set": {"cve_mun":"000"}})
    print("\tRegistros localizados: {}".format(result.matched_count))
    print("\tRegistros actualizados: {}".format(result.modified_count))
except Exception as e:
    logging.info("An exception occurred ::", e)

logging.info("Se inicia el proceso de inserción de los valores del cve_mun")

for index, datos in df.iterrows():
    try:

        logging.info("Actualizando las datos del estado {} y municipio {} ".format(datos["entidad"], datos["municipio"]))


        #num.zfill(3)

        result = db.estab_2024_v6.update_many(
            #Se localiza la emisoras por el nombre del estado
            {
                "cve_ent":str(datos["cve_ent"]).zfill(2),
                "municipio":datos["municipio"]
            },
            #Proceso de actualizacion
            {
                #Listado de parámetros por actualizar
                "$set":{
                    "cve_mun":str(datos["cve_mun"]).zfill(3),
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