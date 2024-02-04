from pymongo import MongoClient
import pandas as pd
import os
import logging
import datetime

from dbCon import *

ct = datetime.datetime.now()
cname = "logs/sub_semarnat_iarc_"+str(ct) + ".log"
logging.basicConfig(filename=cname, filemode='a', level=0, format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
rootLogger = logging.getLogger()
consoleHandler = logging.StreamHandler()
rootLogger.addHandler(consoleHandler)


mc = getMongoClientSemarnatReader()
db = getDbCollectionSemarnat(mc, "semarnat")

local = pd.read_csv("listado_sustancias_iarc_completo.csv", sep="\t")

i = 0
for index, sustancia in local.iterrows():
    print("Sustancia:" + sustancia["cas"] + " " + sustancia["sustancia"])
    result = db.cama_subs_silentspringinstitute.aggregate(
        [
            {
                '$match': {
                    'cas': sustancia["cas"] 
                }
            }, {
                '$project': {
                    '_id': 0, 
                    'category': 1,
                    'name': 1,
                    #'source': 1,
                    'url': 1,
                }
            }
        ]
    )
    i += 1

    try:
        record = result.next()
        print("\tCas encontrado")
        sustancia["silentsprint"]= record["category"]
        sustancia["ssi_nombre"]= record["name"]
        sustancia["ssi_url"]= record["url"]

    except StopIteration:
        print("\tCas no encontrado!")
    


local.to_csv("listado_sustancias_iarc_ssi.csv", sep="\t", index=False)



