from pymongo import MongoClient
import pandas as pd
import os
import logging
import datetime

from dbCon import *

ct = datetime.datetime.now()
cname = "logs_db/emisiones_add_iarc_cat_"+str(ct) + ".log"
logging.basicConfig(filename=cname, filemode='a', level=0, format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
rootLogger = logging.getLogger()
consoleHandler = logging.StreamHandler()
rootLogger.addHandler(consoleHandler)

def updateSustancias():
    logging.info("Se establece la conexión con la base de datos semarnat")

    mc = getMongoClientSemarnatWriter()
    db = getDbCollectionSemarnat(mc, "semarnat")

    logging.info("Se obtiene el listado de sustancias de la iarc de la coleccion sustancias_iarc_list")
    listadoIarc = db.sustancias_iarc_list.find({})
    
    for sustancia in listadoIarc:
        result = db.dbppr_v5.count_documents({"cas":sustancia["cas"]})
        logging.info("\tCantidad de emisiones de {} con CAS ({}): {}".format(sustancia["agent"], sustancia["cas"], result))

        if (result > 0):
            logging.info("\tIniciando la actualización de etiqueta IARC {} para la sustancia {}".format(sustancia["group"], sustancia["agent"]))

            update = db.dbppr_v5.update_many({"cas":sustancia["cas"]},{"$set": {"iarc_agent":sustancia["agent"], "iarc_group":sustancia["group"], "iarc_volume":sustancia["volume"],"iarc_year":sustancia["year"],"iarc_info":sustancia["additional_information"]}})

            logging.info("\tRegistros localizados: {}".format(update.matched_count))
            logging.info("\tRegistros actualizados: {}".format(update.modified_count))
            logging.info ("\tupdate response:" + str(update.raw_result))

        else:
            logging.info ("\t\tLa sustancia: " + sustancia["cas"] + "\t" + sustancia["agent"] + " no se encuentra en la base de datos del retc")

updateSustancias()
