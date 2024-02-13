#!/usr/bin/env python


from pymongo import MongoClient
import pandas as pd
import logging
import datetime
from dbCon import *

ct = datetime.datetime.now()
cname = "logs_db/establecimientos_colecion_esta_mun_"+str(ct) + ".log"
logging.basicConfig(filename=cname, filemode='a', level=0, format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
rootLogger = logging.getLogger()
consoleHandler = logging.StreamHandler()
rootLogger.addHandler(consoleHandler)


def getDbCollection(client, database):
    logging.info("Se obtiene la conexion a la base de datos: " + database)
    db = client[database]
    return db

def searchmuni():
    
    mc = getMongoClientWriter()
    db = getDbCollection(mc, "backupdenue")
    logging.info("Se obtienen las entidades: ")

    columnassalida = {"estado":[],"cve_ent":[], "municipio":[], "cve_mun":[]}
    salida = pd.DataFrame(columnassalida)

    entidades = db.Entidades.find().limit(1)

    for entidad in entidades:
        #data = []
        logging.info("----------------------------------------------")
        
        #logging.info("cve_entidad: " + str(entidad["cve_ent"]) + " " + entidad["entidad"])

        municipios = db.test.distinct("cve_mun", {"cve_ent": entidad["cve_ent"]})
        
        for cve_mun in municipios:
            mun = db.test.find({"cve_ent": entidad["cve_ent"], "cve_mun": cve_mun}, {"_id":0, "municipio":1}).limit(1)
            logging.info("entidad: {}, cve_ent:{}, municipio: {}, cve_mun: {}".format(entidad["entidad"], str(entidad["cve_ent"]).zfill(2), mun[0]["municipio"],str(cve_mun).zfill(3) ))
            
            salida._append({
                #"estado": entidad["entidad"],
                #"cve_ent": str(entidad["cve_ent"]).zfill(2),
                #"cve_mun": str(cve_mun).zfill(3),
                "municipio": mun[0]["municipio"]
            }, ignore_index = True)

    

    salida.to_csv("out_cve_ent_mun/estados_municipios.csv", sep="\t", header=True, index=False)
            
        #logging.info("Preparando la insersión de los municipios a " + str(entidad["cve_ent"]) + " " + str(entidad["entidad"]))
        
        #print(data)
        #jsonMuni = str(jsonify(data))
        #query = {"cve_ent": entidad["cve_ent"]}
        #newatt = {"$set": {"municipios": data}}
        
        #db.Entidades.update_one(query, newatt)
        #logging.info("Insersión de los municipios realizada a: " + str(entidad["cve_ent"]) + " " + str(entidad["entidad"]) )
    closeDB(mc)

searchmuni()

