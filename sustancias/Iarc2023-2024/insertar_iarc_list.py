
import numpy as np
from pymongo import MongoClient
import pandas as pd
import numpy as np
import logging
import datetime

from dbCon import *

ct = datetime.datetime.now()
cname = "logs/db_insertar_iarc_sustancias_"+str(ct) + ".log"
logging.basicConfig(filename=cname, filemode='a', level=0, format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
rootLogger = logging.getLogger()
consoleHandler = logging.StreamHandler()
rootLogger.addHandler(consoleHandler)


logging.info("Se establece la conexión con la base de datos")
mc = getMongoClientSemarnatWriter()
db = getDbCollectionSemarnat(mc, "semarnat")

#Se obtienen las colecciones
collist = db.list_collection_names()
if "estab_2024_v4" not in collist:
    logging.info("Se crea la colección")
    db.create_collection("estab_2024_v4")


input_path="input/iarc_2023-2024.csv"
logging.info("Se lee el contenido del archivo {}".format(input_path))

df = pd.read_csv(input_path, low_memory=False, encoding='utf-8', sep=",")
#Se borran los datos no necesarios
#df["dbmod"] = 0
#df["dbdescmod"] = ""
df = df.replace(np.nan, "")
logging.info("Se convierte el contenido leído en un diccionario")
documents = df.to_dict(orient='records')
result = db.sustancias_iarc_list.insert_many(documents)
logging.info(f'\t{len(result.inserted_ids)} registros se añadieron correctamente')

#Esta versión tiene el inconveniente de que los vacios los coloca como NaN