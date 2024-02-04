import os
import pandas as pd
import logging
import datetime



#ct = datetime.datetime.now()
#cname = "logs_preparacion/formato2_"+str(ct) + ".log"
#logging.basicConfig(filename=cname, filemode='a', level=0, format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
#rootLogger = logging.getLogger()
#consoleHandler = logging.StreamHandler()
#rootLogger.addHandler(consoleHandler)
#

#Este formato solo se aplica a un año
inputpath ="/home/reyes/dev/posdoc-2022-2024/databases/retc/emisoras/es_2012.csv"
output_path="out_preparacion/"


es2012 = pd.read_csv(inputpath, sep="\t",low_memory=False, encoding='utf-8')


#Se agregan las columnas que faltan		
	
es2012["anio"] = 2012
es2012["utmx"] = "Atributo no considerado en este año"
es2012["utmy"] = "Atributo no considerado en este año"
es2012["actsemarnat"] = "Atributo no considerado en este año"
es2012["subsector"] = "Atributo no considerado en este año"

#Se renombran las columnas 
es2012.rename(columns = {'NRA':'nra'}, inplace = True)
es2012.rename(columns = {'Establecimiento':'establecimiento'}, inplace = True)
es2012.rename(columns = {'Sector':'sector'}, inplace = True)
es2012.rename(columns = {'Número SCIAN':'scian'}, inplace = True)
es2012.rename(columns = {'SCIAN':'descscian'}, inplace = True)
es2012.rename(columns = {'Clave Ambiental':'claveambiental'}, inplace = True)
es2012.rename(columns = {'Actividad Principal':'actprincipal'}, inplace = True)
es2012.rename(columns = {'Nombre Parque Industrial':'parqueindustrial'}, inplace = True)
es2012.rename(columns = {'Latitud Norte':'latitudnorte'}, inplace = True)
es2012.rename(columns = {'Longitud Oeste':'longitudoeste'}, inplace = True)
es2012.rename(columns = {'Calle':'calle'}, inplace = True)
es2012.rename(columns = {'Número Exterior':'numexterior'}, inplace = True)
es2012.rename(columns = {'Número Interior':'numinterior'}, inplace = True)
es2012.rename(columns = {'Entre Calle 1':'entrec1'}, inplace = True)
es2012.rename(columns = {'Entre Calle 2':'entrec2'}, inplace = True)
es2012.rename(columns = {'Colonia':'colonia'}, inplace = True)
es2012.rename(columns = {'Localidad':'localidad'}, inplace = True)
es2012.rename(columns = {'Municipio':'municipio'}, inplace = True)
es2012.rename(columns = {'Entidad Federativa':'estado'}, inplace = True)
es2012.rename(columns = {'Código Postal':'codigopostal'}, inplace = True)

print("\tSe ordenan las columnas")
es2012 = es2012.reindex(sorted(es2012.columns), axis=1)
#print(es2012.columns)

outputname = "{}{}.csv".format(output_path, 2012)
es2012.to_csv(outputname, sep="\t", header=True, index=False)

#print(es2012.head())


