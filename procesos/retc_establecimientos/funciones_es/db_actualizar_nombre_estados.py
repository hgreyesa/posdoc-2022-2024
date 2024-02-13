from bson import ObjectId
from pymongo import MongoClient
import pandas as pd
import logging
import datetime

from dbCon import *

ct = datetime.datetime.now()
cname = "logs_db/establecimientos_update_nombre_estados_"+str(ct) + ".log"
logging.basicConfig(filename=cname, filemode='a', level=0, format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
rootLogger = logging.getLogger()
consoleHandler = logging.StreamHandler()
rootLogger.addHandler(consoleHandler)

    


logging.info("Se establece la conexión con la base de datos")
mc = getMongoClientSemarnatWriter()
db = getDbCollectionSemarnat(mc, "semarnat")




try:

    logging.info("Se agrega el campo cve_ent:")
    result = db.estab_2024_v6.update_many({},{"$set": {"cve_ent":"00"}})
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))

    logging.info("Actualizando el cve_ent del estado de Aguascalientes:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"AGUASCALIENTES"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Aguascalientes",
                "cve_ent":"01"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))
    
    #BAJA CALIFORNIA
    logging.info("Actualizando el cve_ent del estado de Baja California:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"BAJA CALIFORNIA"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Baja California",
                "cve_ent":"02"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))
    #BAJA CALIFORNIA SUR
    logging.info("Actualizando el cve_ent del estado de Baja California Sur:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"BAJA CALIFORNIA SUR"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Baja California Sur",
                "cve_ent":"03"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))

    #CAMPECHE
    logging.info("Actualizando el cve_ent del estado de Campeche:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"CAMPECHE"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Campeche",
                "cve_ent":"04"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))

    #COAHUILA
    logging.info("Actualizando el cve_ent del estado de Coahuila de Zaragoza:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"COAHUILA"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Coahuila de Zaragoza",
                "cve_ent":"05"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))

    #COLIMA
    logging.info("Actualizando el cve_ent del estado de Colima:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"COLIMA"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Colima",
                "cve_ent":"06"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))

    #CHIAPAS
    logging.info("Actualizando el cve_ent del estado de Chiapas:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"CHIAPAS"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Chiapas",
                "cve_ent":"07"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))

    #CHIHUAHUA
    logging.info("Actualizando el cve_ent del estado de Chihuahua:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"CHIHUAHUA"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Chihuahua",
                "cve_ent":"08"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))

    #DISTRITO FEDERAL
    logging.info("Actualizando el cve_ent del estado de Ciudad de México:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"DISTRITO FEDERAL"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Ciudad de México",
                "cve_ent":"09"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))

    #DURANGO
    logging.info("Actualizando el cve_ent del estado de Durango:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"DURANGO"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Durango",
                "cve_ent":"10"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))

    #GUANAJUATO
    logging.info("Actualizando el cve_ent del estado de Guanajuato:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"GUANAJUATO"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Guanajuato",
                "cve_ent":"11"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))

    #GUERRERO
    logging.info("Actualizando el cve_ent del estado de Guerrero:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"GUERRERO"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Guerrero",
                "cve_ent":"12"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))

    #HIDALGO
    logging.info("Actualizando el cve_ent del estado de Hidalgo:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"HIDALGO"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Hidalgo",
                "cve_ent":"13"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))
    #JALISCO
    logging.info("Actualizando el cve_ent del estado de Jalisco:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"JALISCO"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Jalisco",
                "cve_ent":"14"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))
    #MEXICO
    logging.info("Actualizando el cve_ent del estado de México:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"MEXICO"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"México",
                "cve_ent":"15"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))

    #MICHOACAN
    logging.info("Actualizando el cve_ent del estado de Michoacán de Ocampo:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"MICHOACAN"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Michoacán de Ocampo",
                "cve_ent":"16"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))

    #MORELOS
    logging.info("Actualizando el cve_ent del estado de Morelos:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"MORELOS"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Morelos",
                "cve_ent":"17"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))

    #NAYARIT
    logging.info("Actualizando el cve_ent del estado de Nayarit:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"NAYARIT"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Nayarit",
                "cve_ent":"18"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))

    #NUEVO LEON
    logging.info("Actualizando el cve_ent del estado de Nuevo León:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"NUEVO LEON"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Nuevo León",
                "cve_ent":"19"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))

    #OAXACA
    logging.info("Actualizando el cve_ent del estado de Oaxaca:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"OAXACA"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Oaxaca",
                "cve_ent":"20"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))
    #PUEBLA
    logging.info("Actualizando el cve_ent del estado de Puebla:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"PUEBLA"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Puebla",
                "cve_ent":"21"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))

    #QUERETARO
    logging.info("Actualizando el cve_ent del estado de Querétaro:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"QUERETARO"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Querétaro",
                "cve_ent":"22"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))

    #QUINTANA ROO
    logging.info("Actualizando el cve_ent del estado de Quintana Roo:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"QUINTANA ROO"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Quintana Roo",
                "cve_ent":"23"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))

    #SAN LUIS POTOSI
    logging.info("Actualizando el cve_ent del estado de San Luis Potosí:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"SAN LUIS POTOSI"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"San Luis Potosí",
                "cve_ent":"24"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))

    #SINALOA
    logging.info("Actualizando el cve_ent del estado de Sinaloa:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"SINALOA"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Sinaloa",
                "cve_ent":"25"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))

    #SONORA
    logging.info("Actualizando el cve_ent del estado de Sonora:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"SONORA"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Sonora",
                "cve_ent":"26"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))

    #TABASCO
    logging.info("Actualizando el cve_ent del estado de Tabasco:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"TABASCO"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Tabasco",
                "cve_ent":"27"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))

    #TAMAULIPAS
    logging.info("Actualizando el cve_ent del estado de Tamaulipas:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"TAMAULIPAS"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Tamaulipas",
                "cve_ent":"28"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))

    #TLAXCALA
    logging.info("Actualizando el cve_ent del estado de Tlaxcala:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"TLAXCALA"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Tlaxcala",
                "cve_ent":"29"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))
    #VERACRUZ
    logging.info("Actualizando el cve_ent del estado de VERACRUZ:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"VERACRUZ"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Veracruz de Ignacio de la Llave",
                "cve_ent":"30"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))
    #YUCATAN
    logging.info("Actualizando el cve_ent del estado de Yucatán:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"YUCATAN"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Yucatán",
                "cve_ent":"31"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))

    #ZACATECAS
    logging.info("Actualizando el cve_ent del estado de Zacatecas:")


    result = db.estab_2024_v6.update_many(
        #Se localiza la emisoras por el nombre del estado
        {
            "estado":"ZACATECAS"
        },
        #Proceso de actualizacion
        {
            #Listado de parámetros por actualizar
            "$set":{
                "estado":"Zacatecas",
                "cve_ent":"32"
            }
        }
    )
    logging.info("\tRegistros localizados: {}".format(result.matched_count))
    logging.info("\tRegistros actualizados: {}".format(result.modified_count))

    

except Exception as e:
        logging.info("An exception occurred ::", e)


#result = db.estab_2024_v2.insert_many(documents)
#logging.info(f'\t{len(result.inserted_ids)} registros se añadieron correctamente')

#Esta versión tiene el inconveniente de que los vacios los coloca como NaN