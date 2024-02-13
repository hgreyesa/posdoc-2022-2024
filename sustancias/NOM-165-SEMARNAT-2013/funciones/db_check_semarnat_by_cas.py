from bson import ObjectId
from pymongo import MongoClient
import pandas as pd
import logging
import datetime

from dbCon import *

ct = datetime.datetime.now()
cname = "sustancias_nom_check_semarnat_list_by_nra_"+str(ct) + ".log"
logging.basicConfig(filename=cname, filemode='a', level=0, format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
rootLogger = logging.getLogger()
consoleHandler = logging.StreamHandler()
rootLogger.addHandler(consoleHandler)

    

cantidad_modificaciones = 0

logging.info("Se establece la conexión con la base de datos")
mc = getMongoClientSemarnatWriter()
db = getDbCollectionSemarnat(mc, "semarnat")

#estab_2024_v6_modificaciones_mun


input_path="cas_semarnat.csv"
logging.info("Se lee el contenido del archivo {}".format(input_path))

df = pd.read_csv(input_path, low_memory=False, encoding='utf-8', sep=",")


datos_salida =[]
logging.info("Se inicia el proceso de consulta de grupos de las sustancias por cas")

for index, datos in df.iterrows():
    try:

        logging.info("Localizando las datos del cas {} ".format(datos["cas"]))

        result = db.subs_semarnat_iarc_ssi.find(
            {
                "cas":str(datos["cas"])
            }
        )

        #print("\tRegistros localizados: {}".format(len(result)))
        for sus in result:
            if(len(sus) > 0):

                datos_salida.append(
                    {
                        "cas":datos["cas"],
                        "grupo":sus["grupo"],
                    }
                )
            else:
                datos_salida.append(
                        {
                            "cas":datos["cas"],
                            "grupo":"",
                        }
                    )


    except Exception as e:
        logging.info("An exception occurred ::", e)

salida = pd.DataFrame.from_dict(datos_salida)
salida.to_csv("reyes_test.csv", sep="\t", header=True, index=False)

#https://www.dof.gob.mx/nota_detalle.php?codigo=5281372&fecha=05/12/2012#gsc.tab=0
