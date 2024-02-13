from pymongo import MongoClient
import pandas as pd
import logging
import datetime

from dbCon import *

ct = datetime.datetime.now()
cname = "logs_db/establecimientos_get_esta_mun_"+str(ct) + ".log"
logging.basicConfig(filename=cname, filemode='a', level=0, format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
rootLogger = logging.getLogger()
consoleHandler = logging.StreamHandler()
rootLogger.addHandler(consoleHandler)

    


logging.info("Se establece la conexión con la base de datos")
mc = getMongoClientSemarnatWriter()
db = getDbCollectionSemarnat(mc, "semarnat")


input_path="datos_resumenes/estab_nra_mas_un_est_mun.csv"
logging.info("Se lee el contenido del archivo {}".format(input_path))

df = pd.read_csv(input_path, low_memory=False, encoding='utf-8', sep="\t")

columnassalida = {"nra":[],"estado":[], "municipio":[]}
salida = pd.DataFrame(columnassalida)


for index, estab in df.iterrows():
    logging.info("nra: {}".format(estab["nra"]))

    result = db.estab_2024_v4.aggregate(
        [
            {
                '$match': {
                    'nra': estab['nra']
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

    for datos in result:
        salida._append({
            "nra":datos["nra"],
            "estado":datos["estado"],
            "municipio":datos["municipio"],
        } , ignore_index = True)
        logging.info("nra: {}, estado: {}, municipio: {} ".format(datos["nra"], datos["estado"], datos["municipio"]))

salida.to_csv("out_resumennra/estados_municipios.csv", sep="\t", header=True, index=False)