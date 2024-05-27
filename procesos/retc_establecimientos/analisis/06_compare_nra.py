#from bson import ObjectId
#from pymongo import MongoClient
import pandas as pd
import logging
import datetime
from difflib import SequenceMatcher

#from dbCon import *

def similar(str1, str2):
    return SequenceMatcher(None, str1, str2).ratio()

ct = datetime.datetime.now()
cname = "logs_db/analisis_comparar_nra_todos_"+str(ct) + ".log"
logging.basicConfig(filename=cname, filemode='a', level=0, format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
rootLogger = logging.getLogger()
consoleHandler = logging.StreamHandler()
rootLogger.addHandler(consoleHandler)

    


input_path="output/01_Listado_nra_unicos.csv"
logging.info("Se lee el contenido del archivo {}".format(input_path))

df = pd.read_csv(input_path, low_memory=False, encoding='utf-8', sep=",")
#df_2 = pd.read_csv(input_path, low_memory=False, encoding='utf-8', sep=",")
columnassalida = {"nra":[],"pag_1":[],"nra_comp":[],"pag_2":[], "similitud":[]} 
salida = pd.DataFrame(columnassalida)
datos_temp = []
row_count = len(df)
for index, nra_1 in df.iterrows():
    index_init = index+1
    index_end = index+10
    logging.info("Recorriendo el listado: {}".format(nra_1["nra"]))
    for index_2, nra_2 in df.loc[index_init:index_end].iterrows():
        if nra_1["nra"][0:3] in nra_2["nra"]:
            res = similar(nra_1["nra"], nra_2["nra"])
            enlace = "https://rnca.tamps.cinvestav.mx/verificacion/nra/nombresestablecimientos.php?nra={}"
            if res > 0.9:
                logging.info("Resultado comparación {} vs {}: {}".format(nra_1["nra"], nra_2["nra"], res))
                datos_temp.append({
                    "nra":nra_1["nra"],
                    "pag_1":enlace.format(nra_1["nra"]),
                    "nra_comp":nra_2["nra"],
                    "pag_2":enlace.format(nra_2["nra"]),
                    "similitud":res,
                })

new_df = pd.DataFrame.from_dict(datos_temp)
new_df.to_csv("07_nra_similitud_24_03_12_v2.csv", sep="\t", header=True, index=False)
           

#nl MTY 
#CDMX aTCAPOTZALCO
#CDMX cUAUTEMOc
#puebla centro
#contadores 