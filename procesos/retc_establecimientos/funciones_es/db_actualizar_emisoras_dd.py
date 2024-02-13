from bson import ObjectId
from pymongo import MongoClient
import pandas as pd
import logging
import datetime

from dbCon import *

ct = datetime.datetime.now()
cname = "logs_db/establecimientos_update_dd_"+str(ct) + ".log"
logging.basicConfig(filename=cname, filemode='a', level=0, format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
rootLogger = logging.getLogger()
consoleHandler = logging.StreamHandler()
rootLogger.addHandler(consoleHandler)

    


logging.info("Se establece la conexión con la base de datos")
mc = getMongoClientSemarnatWriter()
db = getDbCollectionSemarnat(mc, "semarnat")




input_path="out_dms_dd/coordinates_v3_test2.csv"
logging.info("Se lee el contenido del archivo {}".format(input_path))

df = pd.read_csv(input_path, low_memory=False, encoding='utf-8', sep=",")

for index, emisora in df.iterrows():

    try:
        logging.info("Actualizando las coordenadas de la emisora: {}".format(emisora["_id"]))

        result = db.estab_2024_v5.update_one(
            #Se localiza la emisoras por el id
            {
                "_id":ObjectId(emisora["_id"])
            },
            #Proceso de actualizacion
            {
                #Listado de parámetros por actualizar
                "$set":{
                    "lat":float(emisora["lat"]),	
                    "lng":float(emisora["lng"]),	
                    "dmsformat":int(emisora["dmsformat"]),	
                    "dmsdefault":int(emisora["dmsdefault"])
                }
            }
        )
        print("Registros actualizados: {}".format(result.matched_count))
        #result = db.estab_2024_v5.find({"_id": ObjectId(emisora["_id"])})
        #
        #arr = list(result)
        #print(arr)

        
    except Exception as e:
        logging.info("An exception occurred ::", e)
        #return False



#result = db.estab_2024_v2.insert_many(documents)
#logging.info(f'\t{len(result.inserted_ids)} registros se añadieron correctamente')

#Esta versión tiene el inconveniente de que los vacios los coloca como NaN