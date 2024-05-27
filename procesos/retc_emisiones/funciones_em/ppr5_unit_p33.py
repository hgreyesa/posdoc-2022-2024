from pymongo import MongoClient
import logging
import datetime
from decimal import *
from dbCon import *

ct = datetime.datetime.now()
cname = "logs_db/emisiones_update_unit_"+str(ct) + ".log"
logging.basicConfig(filename=cname, filemode='a', level=0, format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
rootLogger = logging.getLogger()
consoleHandler = logging.StreamHandler()
rootLogger.addHandler(consoleHandler)

def convert_decimal(dict_item):
    # This function iterates a dictionary looking for types of Decimal and converts them to Decimal128
    # Embedded dictionaries and lists are called recursively.
    if dict_item is None: return None

    for k, v in list(dict_item.items()):
        if isinstance(v, dict):
            convert_decimal(v)
        elif isinstance(v, list):
            for l in v:
                convert_decimal(l)
        elif isinstance(v, Decimal):
            dict_item[k] = Decimal128(str(v))

    return dict_item

getcontext().prec = 15

def updateG2Kg_es():
    logging.info("Se establece la conexión con la base de datos")

    mc = getMongoClientSemarnatWriter()
    db = getDbCollectionSemarnat(mc, "semarnat")

    logging.info("Se obtienen los datos con unidad g/año")
    listado = db.dbppr_v1_es.find({"unidad": "g/año"}).limit(5)
    for emision in listado:
        logging.info("g/año")

        logging.info("id "+ str(emision["_id"])+ " NRA: " + str(emision["nra"]) + " cas " + emision["cas"] + " sustancia " + emision["sustancia"])


        agua =              Decimal(emision["em_agua"]) / Decimal(1000)  if emision["em_agua"] != 0 else 0
        aire =              Decimal(emision["em_aire"]) / Decimal(1000)  if emision["em_aire"] != 0 else 0
        suelo =             Decimal(emision["em_suelo"]) / Decimal(1000)  if emision["em_suelo"] != 0 else 0
        reutilizacion =     Decimal(emision["tr_reutilizacion"]) / Decimal(1000)  if emision["tr_reutilizacion"] != 0 else 0
        reciclado =         Decimal(emision["tr_reciclado"]) / Decimal(1000)  if emision["tr_reciclado"] != 0 else 0
        tratamiento =       Decimal(emision["tr_tratamiento"]) / Decimal(1000)  if emision["tr_tratamiento"] != 0 else 0
        coprocesamiento =   Decimal(emision["tr_coprocesamiento"]) / Decimal(1000)  if emision["tr_coprocesamiento"] != 0 else 0
        dispfinal =         Decimal(emision["tr_dispfinal"]) / Decimal(1000)  if emision["tr_dispfinal"] != 0 else 0
        alcantarillado =    Decimal(emision["tr_alcantarillado"]) / Decimal(1000)  if emision["tr_alcantarillado"] != 0 else 0
        incineracion =      Decimal(emision["tr_incineracion"]) / Decimal(1000)  if emision["tr_incineracion"] != 0 else 0
        otros =             Decimal(emision["tr_otros"]) / Decimal(1000)  if emision["tr_otros"] != 0 else 0
        

        logging.info("\tagua: " + str(emision["em_agua"]) + " new: " + str(agua) + "\taire: " + str(emision["em_aire"]) + " new: " + str(aire) + "\tsuelo: " + str(emision["em_suelo"]) + " new: "  + str(suelo)+ "\treutilizacion: " + str(emision["tr_reutilizacion"]) + " new: "  + str(reutilizacion)+ "\treciclado: " + str(emision["tr_reciclado"]) + " new: "  + str(reciclado)+ "\ttratamiento: " + str(emision["tr_tratamiento"]) + " new: "  + str(tratamiento)+ "\tcoprocesamiento: " + str(emision["tr_coprocesamiento"]) + " new: "  + str(coprocesamiento)+ "\tdispfinal: " + str(emision["tr_dispfinal"]) + " new: "  + str(dispfinal)+ "\talcantarillado: " + str(emision["tr_alcantarillado"]) + " new: "  + str(alcantarillado)+ "\tincineracion: " + str(emision["tr_incineracion"]) + " new: "  + str(incineracion)+ "\totros: " + str(emision["tr_otros"]) + " new: " + str(otros) )
        logging.info("\t actualizando los datos en la colección")

        #update = db.dbppr_v1_es.update_one(
        #    {
        #        "_id":emision["_id"]
        #    },
        #    {
        #    "$set": {
        #        "em_agua":convert_decimal(agua),
        #        "em_aire":convert_decimal(aire),
        #        "em_suelo":convert_decimal(suelo),
        #        "tr_reutilizacion":convert_decimal(reutilizacion),
        #        "tr_reciclado":convert_decimal(reciclado),
        #        "tr_tratamiento":convert_decimal(tratamiento),
        #        "tr_coprocesamiento":convert_decimal(coprocesamiento),
        #        "tr_dispfinal":convert_decimal(dispfinal),
        #        "tr_alcantarillado":convert_decimal(alcantarillado),
        #        "tr_incineracion":convert_decimal(incineracion),
        #        "tr_otros":convert_decimal(otros),
        #        #"tr_unidad":"kg/_año",
        #    }
        #    })
        #logging.info ("\t\tupdate response:" + str(update.raw_result))

def updateG2Kg_en():
    logging.info("Se establece la conexión con la base de datos")

    mc = getMongoClientSemarnatWriter()
    db = getDbCollectionSemarnat(mc, "semarnat")

    logging.info("Se obtienen los datos con unidad g/año")
    listado = db.dbppr_v1_es.find({"unidad": "g/año"})
    for emision in listado:
        logging.info("g/año")
        logging.info("id "+ str(emision["_id"])+ " NRA: " + str(emision["nra"]) + " cas " + emision["cas"] + " sustancia " + emision["sustancia"])


        agua =              Decimal(emision["em_agua"]) / Decimal(1000)  if emision["em_agua"] != 0 else 0
        aire =              Decimal(emision["em_aire"]) / Decimal(1000)  if emision["em_aire"] != 0 else 0
        suelo =             Decimal(emision["em_suelo"]) / Decimal(1000)  if emision["em_suelo"] != 0 else 0
        reutilizacion =     Decimal(emision["tr_reutilizacion"]) / Decimal(1000)  if emision["tr_reutilizacion"] != 0 else 0
        reciclado =         Decimal(emision["tr_reciclado"]) / Decimal(1000)  if emision["tr_reciclado"] != 0 else 0
        tratamiento =       Decimal(emision["tr_tratamiento"]) / Decimal(1000)  if emision["tr_tratamiento"] != 0 else 0
        coprocesamiento =   Decimal(emision["tr_coprocesamiento"]) / Decimal(1000)  if emision["tr_coprocesamiento"] != 0 else 0
        dispfinal =         Decimal(emision["tr_dispfinal"]) / Decimal(1000)  if emision["tr_dispfinal"] != 0 else 0
        alcantarillado =    Decimal(emision["tr_alcantarillado"]) / Decimal(1000)  if emision["tr_alcantarillado"] != 0 else 0
        incineracion =      Decimal(emision["tr_incineracion"]) / Decimal(1000)  if emision["tr_incineracion"] != 0 else 0
        otros =             Decimal(emision["tr_otros"]) / Decimal(1000)  if emision["tr_otros"] != 0 else 0
        

        logging.info("\tagua: " + str(emision["agua"]) + " new: " + str(agua) + "\taire: " + str(emision["aire"]) + " new: " + str(aire) + "\tsuelo: " + str(emision["suelo"]) + " new: "  + str(suelo)+ "\treutilizacion: " + str(emision["reutilizacion"]) + " new: "  + str(reutilizacion)+ "\treciclado: " + str(emision["reciclado"]) + " new: "  + str(reciclado)+ "\ttratamiento: " + str(emision["tratamiento"]) + " new: "  + str(tratamiento)+ "\tcoprocesamiento: " + str(emision["coprocesamiento"]) + " new: "  + str(coprocesamiento)+ "\tdispfinal: " + str(emision["dispfinal"]) + " new: "  + str(dispfinal)+ "\talcantarillado: " + str(emision["alcantarillado"]) + " new: "  + str(alcantarillado)+ "\tincineracion: " + str(emision["incineracion"]) + " new: "  + str(incineracion)+ "\totros: " + str(emision["otros"]) + " new: " + str(otros) )
        logging.info("\t actualizando los datos en la colección")

        update = db.dbppr_v1_es.update_one(
            {
                "_id":emision["_id"]
            },
            {
            "$set": {
                "em_agua":agua,
                "em_aire":aire,
                "em_suelo":suelo,
                "tr_reutilizacion":reutilizacion,
                "tr_reciclado":reciclado,
                "tr_tratamiento":tratamiento,
                "tr_coprocesamiento":coprocesamiento,
                "tr_dispfinal":dispfinal,
                "tr_alcantarillado":alcantarillado,
                "tr_incineracion":incineracion,
                "tr_otros":otros,
                #"tr_unidad":"kg/_año",
            }
            })
        logging.info ("\t\tupdate response:" + str(update.raw_result))

    listado = db.dbppr_v1_en.find({"unidad": "g/year"})
    for emision in listado:
        logging.info("g/year")
        logging.info("id "+ str(emision["_id"])+ " NRA: " + str(emision["nra"]) + " cas " + emision["cas"] + " sustancia " + emision["sustancia"])


        water =              Decimal(emision["water"]) / Decimal(1000)  if emision["water"] != 0 else 0
        air =              Decimal(emision["air"]) / Decimal(1000)  if emision["air"] != 0 else 0
        soil =             Decimal(emision["soil"]) / Decimal(1000)  if emision["soil"] != 0 else 0
        sewageforreuse =     Decimal(emision["sewageforreuse"]) / Decimal(1000)  if emision["sewageforreuse"] != 0 else 0
        recycling =         Decimal(emision["recycling"]) / Decimal(1000)  if emision["recycling"] != 0 else 0
        treatment =       Decimal(emision["treatment"]) / Decimal(1000)  if emision["treatment"] != 0 else 0
        coprocessing =   Decimal(emision["co-processing"]) / Decimal(1000)  if emision["co-processing"] != 0 else 0
        finaldisposition =         Decimal(emision["finaldisposition"]) / Decimal(1000)  if emision["finaldisposition"] != 0 else 0
        sewerage =    Decimal(emision["sewerage"]) / Decimal(1000)  if emision["sewerage"] != 0 else 0
        incineration =      Decimal(emision["incineration"]) / Decimal(1000)  if emision["incineration"] != 0 else 0
        others =             Decimal(emision["others"]) / Decimal(1000)  if emision["others"] != 0 else 0
        
        #logging.info("\tagua: " + str(emision["agua"]) + " new: " + str(agua) + "\taire: " + str(emision["aire"]) + " new: " + str(aire) + "\tsuelo: " + str(emision["suelo"]) + " new: "  + str(suelo)+ "\treutilizacion: " + str(emision["reutilizacion"]) + " new: "  + str(reutilizacion)+ "\treciclado: " + str(emision["reciclado"]) + " new: "  + str(reciclado)+ "\ttratamiento: " + str(emision["tratamiento"]) + " new: "  + str(tratamiento)+ "\tcoprocesamiento: " + str(emision["coprocesamiento"]) + " new: "  + str(coprocesamiento)+ "\tdispfinal: " + str(emision["dispfinal"]) + " new: "  + str(dispfinal)+ "\talcantarillado: " + str(emision["alcantarillado"]) + " new: "  + str(alcantarillado)+ "\tincineracion: " + str(emision["incineracion"]) + " new: "  + str(incineracion)+ "\totros: " + str(emision["otros"]) + " new: " + str(otros) )
        logging.info("\t actualizando los datos en la colección")

        update = db.dbppr_v1_es.update_one(
            {
                "_id":emision["_id"]
            },
            {
            "$set": {
                "water":water,
                "air":air,
                "soil":soil,
                "sewageforreuse":sewageforreuse,
                "recycling":recycling,
                "treatment":treatment,
                "co-processing":coprocessing,
                "finaldisposition":finaldisposition,
                "sewerage":sewerage,
                "incineration":incineration,
                "others":others,
                #"tr_unidad":"kg/_año",
            }
            })
        logging.info ("\t\tupdate response:" + str(update.raw_result))


def updateTon2Kg_es():
    logging.info("Se establece la conexión con la base de datos")

    mc = getMongoClientSemarnatWriter()
    db = getDbCollectionSemarnat(mc, "semarnat")

    logging.info("Se obtienen los datos con unidad Ton/año")
    listadoton = db.emisiones_retc_kg.find({"unidad": "Ton/año"})

    for emision in listadoton:

        logging.info("Ton/año")
        logging.info("id "+ str(emision["_id"])+ " NRA: " + str(emision["nra"]) + " cas " + emision["cas"] + " sustancia " + emision["sustancia"])

        agua =              Decimal(emision["em_agua"]) * Decimal(1000)  if emision["em_agua"] != 0 else 0
        aire =              Decimal(emision["em_aire"]) * Decimal(1000)  if emision["em_aire"] != 0 else 0
        suelo =             Decimal(emision["em_suelo"]) * Decimal(1000)  if emision["em_suelo"] != 0 else 0
        reutilizacion =     Decimal(emision["tr_reutilizacion"]) * Decimal(1000)  if emision["tr_reutilizacion"] != 0 else 0
        reciclado =         Decimal(emision["tr_reciclado"]) * Decimal(1000)  if emision["tr_reciclado"] != 0 else 0
        tratamiento =       Decimal(emision["tr_tratamiento"]) * Decimal(1000)  if emision["tr_tratamiento"] != 0 else 0
        coprocesamiento =   Decimal(emision["tr_coprocesamiento"]) * Decimal(1000)  if emision["tr_coprocesamiento"] != 0 else 0
        dispfinal =         Decimal(emision["tr_dispfinal"]) * Decimal(1000)  if emision["tr_dispfinal"] != 0 else 0
        alcantarillado =    Decimal(emision["tr_alcantarillado"]) * Decimal(1000)  if emision["tr_alcantarillado"] != 0 else 0
        incineracion =      Decimal(emision["tr_incineracion"]) * Decimal(1000)  if emision["tr_incineracion"] != 0 else 0
        otros =             Decimal(emision["tr_otros"]) * Decimal(1000)  if emision["tr_otros"] != 0 else 0

        #logging.info("\tagua: " + str(emision["agua"]) + " new: " + str(agua) + "\taire: " + str(emision["aire"]) + " new: " + str(aire) + "\tsuelo: " + str(emision["suelo"]) + " new: "  + str(suelo)+ "\treutilizacion: " + str(emision["reutilizacion"]) + " new: "  + str(reutilizacion)+ "\treciclado: " + str(emision["reciclado"]) + " new: "  + str(reciclado)+ "\ttratamiento: " + str(emision["tratamiento"]) + " new: "  + str(tratamiento)+ "\tcoprocesamiento: " + str(emision["coprocesamiento"]) + " new: "  + str(coprocesamiento)+ "\tdispfinal: " + str(emision["dispfinal"]) + " new: "  + str(dispfinal)+ "\talcantarillado: " + str(emision["alcantarillado"]) + " new: "  + str(alcantarillado)+ "\tincineracion: " + str(emision["incineracion"]) + " new: "  + str(incineracion)+ "\totros: " + str(emision["otros"]) + " new: " + str(otros) )
        
        logging.info("\t actualizando los datos en la colección")

        update = db.emisiones_retc_kg.update_one(
            {
                "_id":emision["_id"]
            },
            {
            "$set": {
                "em_agua":agua,
                "em_aire":aire,
                "em_suelo":suelo,
                "tr_reutilizacion":reutilizacion,
                "tr_reciclado":reciclado,
                "tr_tratamiento":tratamiento,
                "tr_coprocesamiento": coprocesamiento,
                "tr_dispfinal":dispfinal,
                "tr_alcantarillado":alcantarillado,
                "tr_incineracion":incineracion,
                "tr_otros":otros,
                #"unidad":"kg/año",
            }
            })

        logging.info ("\t\tupdate response:" + str(update.raw_result))

def updateTon2Kg_en():
    logging.info("Se establece la conexión con la base de datos")

    mc = getMongoClientSemarnatWriter()
    db = getDbCollectionSemarnat(mc, "semarnat")

    logging.info("Se obtienen los datos con unidad Ton/año")
    listadoton = db.emisiones_retc_kg.find({"unidad": "Ton/año"})

    for emision in listadoton:

        logging.info("Ton/año")
        logging.info("id "+ str(emision["_id"])+ " NRA: " + str(emision["nra"]) + " cas " + emision["cas"] + " sustancia " + emision["sustancia"])

        water =              Decimal(emision["water"]) * Decimal(1000)  if emision["water"] != 0 else 0
        air =              Decimal(emision["air"]) * Decimal(1000)  if emision["air"] != 0 else 0
        soil =             Decimal(emision["soil"]) * Decimal(1000)  if emision["soil"] != 0 else 0
        sewageforreuse =     Decimal(emision["sewageforreuse"]) * Decimal(1000)  if emision["sewageforreuse"] != 0 else 0
        recycling =         Decimal(emision["recycling"]) * Decimal(1000)  if emision["recycling"] != 0 else 0
        treatment =       Decimal(emision["treatment"]) * Decimal(1000)  if emision["treatment"] != 0 else 0
        coprocessing =   Decimal(emision["co-processing"]) * Decimal(1000)  if emision["co-processing"] != 0 else 0
        finaldisposition =         Decimal(emision["finaldisposition"]) * Decimal(1000)  if emision["finaldisposition"] != 0 else 0
        sewerage =    Decimal(emision["sewerage"]) * Decimal(1000)  if emision["sewerage"] != 0 else 0
        incineration =      Decimal(emision["incineration"]) * Decimal(1000)  if emision["incineration"] != 0 else 0
        others =             Decimal(emision["others"]) * Decimal(1000)  if emision["others"] != 0 else 0

        #logging.info("\tagua: " + str(emision["agua"]) + " new: " + str(agua) + "\taire: " + str(emision["aire"]) + " new: " + str(aire) + "\tsuelo: " + str(emision["suelo"]) + " new: "  + str(suelo)+ "\treutilizacion: " + str(emision["reutilizacion"]) + " new: "  + str(reutilizacion)+ "\treciclado: " + str(emision["reciclado"]) + " new: "  + str(reciclado)+ "\ttratamiento: " + str(emision["tratamiento"]) + " new: "  + str(tratamiento)+ "\tcoprocesamiento: " + str(emision["coprocesamiento"]) + " new: "  + str(coprocesamiento)+ "\tdispfinal: " + str(emision["dispfinal"]) + " new: "  + str(dispfinal)+ "\talcantarillado: " + str(emision["alcantarillado"]) + " new: "  + str(alcantarillado)+ "\tincineracion: " + str(emision["incineracion"]) + " new: "  + str(incineracion)+ "\totros: " + str(emision["otros"]) + " new: " + str(otros) )
        
        logging.info("\t actualizando los datos en la colección")

        update = db.emisiones_retc_kg.update_one(
            {
                "_id":emision["_id"]
            },
            {
            "$set": {
                "water":water,
                "air":air,
                "soil":soil,
                "sewageforreuse":sewageforreuse,
                "recycling":recycling,
                "treatment":treatment,
                "co-processing": coprocessing,
                "finaldisposition":finaldisposition,
                "sewerage":sewerage,
                "incineration":incineration,
                "others":others,
                #"unidad":"kg/año",
            }
            })

        logging.info ("\t\tupdate response:" + str(update.raw_result))

updateG2Kg_es()
#updateG2Kg_en()
#updateTon2Kg_es()
#updateTon2Kg_en()
