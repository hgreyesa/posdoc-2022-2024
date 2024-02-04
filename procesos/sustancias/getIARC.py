from pymongo import MongoClient
import pandas as pd
import os
import logging
import datetime

from dbCon import *

ct = datetime.datetime.now()
cname = "logs/sustancias_semarnat_iarc_"+str(ct) + ".log"
logging.basicConfig(filename=cname, filemode='a', level=0, format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
rootLogger = logging.getLogger()
consoleHandler = logging.StreamHandler()
rootLogger.addHandler(consoleHandler)

            
mc = getMongoClientSemarnatReader()
db = getDbCollectionSemarnat(mc, "semarnat")

#Se lee el listado de sustancas, se coloco la columna IARC con el valor por defecto 'No considerado'

logging.info("Se lee el listado de sustancas, se coloco la columna IARC con el valor por defecto 'No considerado'")
local = pd.read_csv("input/listado_sustancias_iarc.csv", sep="\t")

#Se recorre el contenido del dataframe por fila. Cada fila contiene la descripción de una sustancia
coniarc=0
contador=0
siniarc=0
for index, sustancia in local.iterrows():
    logging.info("Sustancia: {} CAS: {}".format(sustancia["sustancia"], sustancia["cas"]))

    result = db.emisiones_perfil.aggregate(
        [
            {
                '$match': {
                    'cas': sustancia["cas"]
                }
            }, {
                '$group': {
                    '_id': {
                        'cas': '$cas', 
                        'iarc': '$iarc'
                    }
                }
            }, {
                '$project': {
                    '_id': 0, 
                    'iarc': '$_id.iarc'
                }
            }
        ]
    )
    contador+=1

    try:
        record = result.next()
        logging.info("\tGrupo IARC:{}".format(record["iarc"]))
        sustancia["iarc"]= record["iarc"]
        coniarc +=1
        

    except StopIteration:
        logging.info("\tSustancia no considerada por la IARC")
        siniarc +=1
    
logging.info("Sustancias RETC con grupo IARC: {}".format(coniarc))
logging.info("Sustancias RETC sin grupo IARC: {}".format(siniarc))
logging.info("Total de sustancias RETC 2004-2022: {}".format(contador))



local.to_csv("output/sustancias_retc_iarc.csv", sep="\t", index=False)



