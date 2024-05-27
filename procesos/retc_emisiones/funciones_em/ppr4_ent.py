from bson import ObjectId
from pymongo import MongoClient
import pandas as pd
import logging
import datetime

from dbCon import *

ct = datetime.datetime.now()
cname = "logs_db/establecimientos_update_nombre_estados_"+str(ct) + ".log"
logging.basicConfig(filename=cname, filemode='a', level=0, format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
rootLogger = logging.getLogger()
consoleHandler = logging.StreamHandler()
rootLogger.addHandler(consoleHandler)

    


logging.info("Se establece la conexión con la base de datos")
mc = getMongoClientSemarnatWriter()
db = getDbCollectionSemarnat(mc, "semarnat")




try:

    logging.info("Se agrega el campo cve_ent:")
    result = db.dbppr_v1_es.update_many({},{"$set": {"cve_ent":"00"}})
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))

    


    input_path="categorias/dbppr_v1_es_estados_list.csv"
    logging.info("Se lee el contenido del archivo {}".format(input_path))

    df = pd.read_csv(input_path, low_memory=False, encoding='utf-8', sep="\t")


    for index, emisora in df.iterrows():
        logging.info("\tActualizando el cve_ent del estado de {}".format(emisora["nombre1"]))
        

        result = db.dbppr_v1_es.update_many(
            #Se localiza la emisoras por el nombre del estado
            {
                "estado":emisora["nombre1"]
            },
            #Proceso de actualizacion
            {
                #Listado de parámetros por actualizar
                "$set":{
                    "estado":emisora["nombre2"],
                    "cve_ent":str(emisora["cve_ent"]).zfill(2)
                }
            }
        )


        logging.info("\t\tF1 localizados: {}".format(result.matched_count))
        logging.info("\t\tF1 actualizados: {}".format(result.modified_count))
        
        result = db.dbppr_v1_es.update_many(
            #Se localiza la emisoras por el nombre del estado
            {
                "estado":emisora["nombre2"]
            },
            #Proceso de actualizacion
            {
                #Listado de parámetros por actualizar
                "$set":{
                    #"estado":emisora["nombre2"],
                    "cve_ent":str(emisora["cve_ent"]).zfill(2)
                }
            }
        )

        logging.info("\t\tF2 localizados: {}".format(result.matched_count))
        logging.info("\t\tF2 actualizados: {}".format(result.modified_count))


        result = db.dbppr_v1_en.update_many(
            #Se localiza la emisoras por el nombre del estado
            {
                "entityname":emisora["nombre1"]
            },
            #Proceso de actualizacion
            {
                #Listado de parámetros por actualizar
                "$set":{
                    "entityname":emisora["nombre2"],
                    "cve_ent":str(emisora["cve_ent"])
                }
            }
        )
        

        logging.info("\t\tF1 en localizados: {}".format(result.matched_count))
        logging.info("\t\tF1 en actualizados: {}".format(result.modified_count))

        result = db.dbppr_v1_en.update_many(
            #Se localiza la emisoras por el nombre del estado
            {
                "entityname":emisora["nombre2"]
            },
            #Proceso de actualizacion
            {
                #Listado de parámetros por actualizar
                "$set":{
                    #"estado":emisora["nombre2"],
                    "cve_ent":str(emisora["cve_ent"]).zfill(2)
                }
            }
        )

        logging.info("\t\tF2 en localizados: {}".format(result.matched_count))
        logging.info("\t\tF2 en actualizados: {}".format(result.modified_count))

    


except Exception as e:
        logging.info("An exception occurred ::", e)


#result = db.estab_2024_v2.insert_many(documents)
#logging.info(f'\t{len(result.inserted_ids)} registros se añadieron correctamente')

#Esta versión tiene el inconveniente de que los vacios los coloca como NaN