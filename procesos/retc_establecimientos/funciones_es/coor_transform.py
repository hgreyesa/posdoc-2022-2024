from pymongo import MongoClient
import pandas as pd
import os
import logging
import datetime

from dbCon import *

ct = datetime.datetime.now()
cname = "logs_db/transform_DMS_to_DD"+str(ct) + ".log"
logging.basicConfig(filename=cname, filemode='a', level=0, format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
rootLogger = logging.getLogger()
consoleHandler = logging.StreamHandler()
rootLogger.addHandler(consoleHandler)

fjoin="datos_resumenes/estab_2024_v4_dd_dms.csv"
logging.info("Iniciando la lectura del archivo: " + fjoin)
df = pd.read_csv(fjoin, low_memory=False, encoding='utf-8', sep=",")

logging.info("\tAñadiendo las nuevas columnas lat, lng y calculada")
df["lat"] = 0.0
df["lng"] = 0.0
df["dmsformat"] = 0
df["dmsdefault"] = 0
#df["mapa"] = 0
contador = 0
calculados = 0
correctos = 0
incorrectos = 0
#mapa= 0



logging.info("Se establece la conexión con la base de datos")
mc = getMongoClientSemarnatWriter()
db = getDbCollectionSemarnat(mc, "semarnat")


logging.info("\tSe inicia el recorrido de los establecimientos")
for index, emisora in df.iterrows():

    newlat = 0.0
    newlon = 0.0
    contador += 1


    filteremi = { '_id': emisora["_id"]}

    logging.info("\t\tValores originales: " + str(contador) + "\tlat:\t" + str(emisora['latitudnorte']) + "\tlng:\t"+ str(emisora['longitudoeste']))
    #logging.info ("\t\t\tlat:\t" + str(emisora['latitudnorte']) + "\tlng:\t"+ str(emisora['longitudoeste']))
    try:
        lat = float(emisora['latitudnorte'])
        lng = float(emisora['longitudoeste'])
        newlat =str(emisora['latitudnorte'])
        newlon =str(emisora['longitudoeste']) 

        df._set_value(index,'dmsformat',0)
        #df._set_value(index,'mapa',0)
        emisora['dmsformat'] = 0
        #emisora['mapa'] = 1
        correctos += 1
        #mapa += 1
        emisora['lat'] = float(emisora['latitudnorte'])
        emisora['lng'] = float(emisora['longitudoeste'])

        df._set_value(index,'lat',lat)
        df._set_value(index,'lng',lng)
        logging.info("\t\t\tNo se requieren modificaciones")

        #newvalues = { "$set": { 
        #    'lat': float(emisora['latitudnorte']) ,
        #    'lng': float(emisora['longitudoeste']) ,
        #} }
#
        #result = db.dd_coor.update_one(filteremi,newvalues)

    except ValueError:
        lat = str(emisora['latitudnorte']).replace(" ", "")
        lng = str(emisora['longitudoeste']).replace(" ", "")

        if "0°0'0\"" in lat or "0°0'0\"" in lng or "°0'0\"" in lat or "°0'0\"" in lng or "º0'0\"" in lat or "º0'0\"" in lng or "°'\"" in lat or "°'\"" in lng:
            emisora['lat'] = 0;
            emisora['lng'] = 0;
            emisora['dmsformat'] = 1
            emisora['dmsdefault'] = 1
            #emisora['mapa'] = 0


            #df._set_value(index,'lat',lat)
            #df._set_value(index,'lng',lng)
            df._set_value(index,'dmsformat',1)
            df._set_value(index,'dmsdefault',1)
            #df._set_value(index,'mapa',0)
            incorrectos += 1

            #newvalues = { "$set": { 
            #    'lat': 0 ,
            #    'lng': 0 ,
            #    'calculada': 1,
            #    'dmsdefault': 1,
            #    'mapa':  0,
            #} }
#
            #result = db.dd_coor.update_one(filteremi,newvalues)
            logging.info("\t\t\tEs un valor por defecto")

        
        else:

            if "°" in lat or "°" in lng:

                logging.info("\t\t\tSe requieren modificaciones formato 1")
                lat = lat.replace("°", " ")
                lat = lat.replace("'", " ")
                lat = lat.replace("\"", " ")
                lng = lng.replace("°", " ")
                lng = lng.replace("'", " ")
                lng = lng.replace("\"", " ")
                arr1 = lat.split(" ")
                arr2 = lng.split(" ")

                emisora['dmsformat'] = 1
                #emisora['mapa'] = 1
                df._set_value(index,'dmsformat',1)
                #df._set_value(index,'mapa',1)


                #mapa += 1
                calculados += 1

                if (arr2[0].startswith('0.')):
                    arr2[0] = float(arr2[0])*100
                else:
                    arr2[0] = float(arr2[0])
                
                if (arr1[0].startswith('0.')):
                    arr1[0] = float(arr1[0])*100
                else: 
                    arr1[0] = float(arr1[0])

                
                if(float(arr2[0])>0 and float(arr1[0]) > 0):
                    newlat = 1 * ( int (arr1[0]) + float(arr1[1])/60 + float(arr1[2])/3600)
                    newlon = -1 * ( int(arr2[0]) + float(arr2[1])/60 + float(arr2[2])/3600)
                else:
                    newlat = 1 * ( int (arr1[0]) + float(arr1[1])/60 + float(arr1[2])/3600)
                    newlon = -1 * ( int(arr2[0]) + float(arr2[1])/60 + float(arr2[2])/3600)
                    newlon = newlon * -1
                emisora['lat'] = newlat
                emisora['lng'] = newlon
                
                df._set_value(index,'lat',newlat)
                df._set_value(index,'lng',newlon)

                #newvalues = { "$set": { 
                #    'lat': newlat,
                #    'lng': newlon ,
                #    'calculada': 1,
                #    #'dmsdefault': 0,
                #    'mapa':  1,
                #} }
                #result = db.dd_coor.update_one(filteremi,newvalues)
                logging.info("\t\t\t\tValores calculados: " + "\tlat:\t" + str(emisora['lat']) + "\tlng:\t"+ str(emisora['lng']))

            else: 
                if "º" in lat or "º" in lng:

                    logging.info("\t\t\tSe requieren modificaciones formato 2")
                    lat = lat.replace("º", " ")
                    lat = lat.replace("'", " ")
                    lat = lat.replace("\"", " ")
                    lng = lng.replace("º", " ")
                    lng = lng.replace("'", " ")
                    lng = lng.replace("\"", " ")
                    arr1 = lat.split(" ")
                    arr2 = lng.split(" ")
                    emisora['dmsformat'] = 1
                    #emisora['mapa'] = 1

                    df._set_value(index,'dmsformat',1)
                    #df._set_value(index,'mapa',1)
                    #mapa += 1
                    calculados += 1

                    if (arr2[0].startswith('0.')):
                        arr2[0] = float(arr2[0])*100
                    else:
                        arr2[0] = float(arr2[0])
                    
                    if (arr1[0].startswith('0.')):
                        arr1[0] = float(arr1[0])*100
                    else: 
                        arr1[0] = float(arr1[0])


                    
                    if(float(arr2[0])>0 and float(arr1[0]) > 0):
                        newlat = 1 * ( int (arr1[0]) + float(arr1[1])/60 + float(arr1[2])/3600)
                        newlon = -1 * ( int(arr2[0]) + float(arr2[1])/60 + float(arr2[2])/3600)
                    else:
                        newlat = 1 * ( int (arr1[0]) + float(arr1[1])/60 + float(arr1[2])/3600)
                        newlon = -1 * ( int(arr2[0]) + float(arr2[1])/60 + float(arr2[2])/3600)
                        newlon = newlon * -1

                    emisora['lat'] = newlat
                    emisora['lng'] = newlon


                    df._set_value(index,'lat',newlat)
                    df._set_value(index,'lng',newlon)

                    #newvalues = { "$set": { 
                    #    'lat': newlat,
                    #    'lng': newlon ,
                    #    'calculada': 1,
                    #    #'dmsdefault': 0,
                    #    'mapa':  1,
                    #} }
                    #result = db.dd_coor.update_one(filteremi,newvalues)


    
    
logging.info("RESUMEN:")
logging.info("\tregistros:" + str(contador))
logging.info("\tcorrectos:" + str(correctos)+"/"+ str(contador))
logging.info("\tcalculados:" + str(calculados) + "/"+ str(contador))
logging.info("\tincorrectos:" + str(incorrectos)+"/"+ str(contador))
#logging.info("\tmapa:" + str(mapa) +"/"+ str(contador))
mitotal = correctos + calculados + incorrectos
logging.info("\ttotal:" + str(mitotal) +"/"+ str(contador))




output_path = "out_dms_dd/coordinates_v3_test2.csv"
df.to_csv(output_path, encoding="utf-8", header=True, index=False)

#25.7586963,-100.1951198
       
