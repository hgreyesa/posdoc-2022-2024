from bson import ObjectId
from numpy import NaN
from pymongo import MongoClient
import pandas as pd
import logging
import datetime

from dbCon import *

ct = datetime.datetime.now()
cname = "logs_db/establecimientos_update_unit_default_0_"+str(ct) + ".log"
logging.basicConfig(filename=cname, filemode='a', level=0, format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
rootLogger = logging.getLogger()
consoleHandler = logging.StreamHandler()
rootLogger.addHandler(consoleHandler)

    


logging.info("Se establece la conexión con la base de datos")
mc = getMongoClientSemarnatWriter()
db = getDbCollectionSemarnat(mc, "semarnat")


try:

    input_path="categorias/dbppr_v1_es_units_replaceNaN.csv"
    logging.info("Se lee el contenido del archivo {}".format(input_path))

    df = pd.read_csv(input_path, low_memory=False, encoding='utf-8', sep="\t")


    for index, emisora in df.iterrows():
        logging.info("\tActualizando la unidad a 0 para NaN en {} {}".format(emisora["nombre"], emisora["name"]))
        

        result = db.dbppr_v1_es.update_many(
            #Se localiza la emisoras por el nombre del estado
            {
                emisora["nombre"]: NaN
            },
            #Proceso de actualizacion
            {
                #Listado de parámetros por actualizar
                "$set":{
                     emisora["nombre"]:0
                }
            }
        )


        logging.info("\t\tF1 es localizados: {}".format(result.matched_count))
        logging.info("\t\tF1 es actualizados: {}".format(result.modified_count))
        

        result = db.dbppr_v1_en.update_many(
            #Se localiza la emisoras por el nombre del estado
            {
                emisora["name"]: NaN
            },
            #Proceso de actualizacion
            {
                #Listado de parámetros por actualizar
                "$set":{
                   emisora["name"]: 0
                }
            }
        )
        

        logging.info("\t\tF1 en localizados: {}".format(result.matched_count))
        logging.info("\t\tF1 en actualizados: {}".format(result.modified_count))

       
    
except Exception as e:
        logging.info("An exception occurred ::", e)


#result = db.estab_2024_v2.insert_many(documents)
#logging.info(f'\t{len(result.inserted_ids)} registros se añadieron correctamente')

#Esta versión tiene el inconveniente de que los vacios los coloca como NaN