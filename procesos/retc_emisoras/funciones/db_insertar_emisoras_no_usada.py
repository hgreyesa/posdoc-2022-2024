from pymongo import MongoClient
import pandas as pd
import logging
import datetime

from dbCon import *

ct = datetime.datetime.now()
cname = "logs_db/establecimientos_import_"+str(ct) + ".log"
logging.basicConfig(filename=cname, filemode='a', level=0, format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
rootLogger = logging.getLogger()
consoleHandler = logging.StreamHandler()
rootLogger.addHandler(consoleHandler)

    


logging.info("Se establece la conexión con la base de datos")
mc = getMongoClientSemarnatWriter()
db = getDbCollectionSemarnat(mc, "semarnat")

#Se obtienen las colecciones
collist = db.list_collection_names()
if "estab_2024_v2" not in collist:
    logging.info("Se crea la colección")
    db.create_collection("estab_2024_v2")


input_path="out_append/2004-2022.csv"
logging.info("Se lee el contenido del archivo {}".format(input_path))

df = pd.read_csv(input_path, low_memory=False, encoding='utf-8', sep="\t")

for index, emisora in df.iterrows():

    try:
        datos_emisora = {
            "actprincipal":emisora["actprincipal"],
            "actsemarnat":emisora["actsemarnat"],
            "anio":emisora["anio"],
            "calle":emisora["calle"],
            "claveambiental":emisora["claveambiental"],
            "codigopostal":emisora["codigopostal"],
            "colonia":emisora["colonia"],
            "descscian":emisora["descscian"],
            "entrec1":emisora["entrec1"],
            "entrec2":emisora["entrec2"],
            "establecimiento":emisora["establecimiento"],
            "estado":emisora["estado"],
            "latitudnorte":emisora["latitudnorte"],
            "localidad":emisora["localidad"],
            "longitudoeste":emisora["longitudoeste"],
            "municipio":emisora["municipio"],
            "nra":emisora["nra"],
            "numexterior":emisora["numexterior"],
            "numinterior":emisora["numinterior"],
            "parqueindustrial":emisora["parqueindustrial"],
            "scian":emisora["scian"],
            "sector":emisora["sector"],
            "subsector":emisora["subsector"],
            "utmx":emisora["utmx"],
            "utmy":emisora["utmy"],
        }
        result = db.estab_2024_v2.insert_one(datos_emisora)
        #return True
    except Exception as e:
        logging.info("An exception occurred ::", e)
        #return False



#result = db.estab_2024_v2.insert_many(documents)
#logging.info(f'\t{len(result.inserted_ids)} registros se añadieron correctamente')

#Esta versión tiene el inconveniente de que los vacios los coloca como NaN