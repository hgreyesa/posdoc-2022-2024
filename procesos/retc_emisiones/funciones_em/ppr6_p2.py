from pymongo import MongoClient
import pandas as pd
import os
import logging
import datetime

from dbCon import *

ct = datetime.datetime.now()
cname = "logs_db/emisiones_add_iarc_cat_compuestos_"+str(ct) + ".log"
logging.basicConfig(filename=cname, filemode='a', level=0, format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
rootLogger = logging.getLogger()
consoleHandler = logging.StreamHandler()
rootLogger.addHandler(consoleHandler)

def updateSustancias():
    logging.info("Se establece la conexión con la base de datos semarnat")

    mc = getMongoClientSemarnatWriter()
    db = getDbCollectionSemarnat(mc, "semarnat")


    input_path="categorias/dbppr_v6_compuestos.csv"
    logging.info("Se lee el contenido del archivo {}".format(input_path))

    df = pd.read_csv(input_path, low_memory=False, encoding='utf-8', sep="\t")
    
    logging.info("Iniciando el recorrdido de los cas con cambios")

    for index, cambio in df.iterrows():

        logging.info("\tSe obtienen los datos IARC de la sustancia {} con CAS ({}). Con los retc CAS ({},{}) de los compuestos".format(cambio["sustancia"], cambio["cas"], cambio["cas1"], cambio["cas2"]))
        sustancia_iarc = db.sustancias_iarc_list.find_one({"cas":cambio["cas"]})

        #print("\t\t"+listadoIarc["agent"])
        update = db.dbppr_v5.update_many({"cas":cambio["cas1"]},{"$set": {"iarc_agent":sustancia_iarc["agent"], "iarc_group":sustancia_iarc["group"], "iarc_volume":sustancia_iarc["volume"],"iarc_year":sustancia_iarc["year"],"iarc_info":sustancia_iarc["additional_information"]}})
        logging.info("\t\tRegistros localizados ({}): {}".format(update.matched_count, cambio["cas1"]))
        logging.info("\t\tRegistros actualizados ({}): {}".format(update.modified_count, cambio["cas1"]))

        update = db.dbppr_v5.update_many({"cas":cambio["cas2"]},{"$set": {"iarc_agent":sustancia_iarc["agent"], "iarc_group":sustancia_iarc["group"], "iarc_volume":sustancia_iarc["volume"],"iarc_year":sustancia_iarc["year"],"iarc_info":sustancia_iarc["additional_information"]}})
        logging.info("\t\tRegistros localizados ({}): {}".format(update.matched_count, cambio["cas2"]))
        logging.info("\t\tRegistros actualizados ({}): {}".format(update.modified_count, cambio["cas2"]))
        #logging.info ("\t\tupdate response:" + str(update.raw_result))
    
    #for sustancia in listadoIarc:
    #    result = db.dbppr_v5.count_documents({"cas":sustancia["cas"]})
    #    logging.info("\tCantidad de emisiones de {} con CAS ({}): {}".format(sustancia["agent"], sustancia["cas"], result))
#
    #    if (result > 0):
    #        logging.info("\tIniciando la actualización de etiqueta IARC {} para la sustancia {}".format(sustancia["group"], sustancia["agent"]))
#
    #        update = db.dbppr_v5.update_many({"cas":sustancia["cas"]},{"$set": {"iarc_agent":sustancia["agent"], "iarc_group":sustancia["group"], "iarc_volume":sustancia["volume"],"iarc_year":sustancia["year"],"iarc_info":sustancia["additional_information"]}})
#
    #        logging.info("\tRegistros localizados: {}".format(update.matched_count))
    #        logging.info("\tRegistros actualizados: {}".format(update.modified_count))
    #        logging.info ("\tupdate response:" + str(update.raw_result))
#
    #    else:
    #        logging.info ("\t\tLa sustancia: " + sustancia["cas"] + "\t" + sustancia["agent"] + " no se encuentra en la base de datos del retc")

updateSustancias()
