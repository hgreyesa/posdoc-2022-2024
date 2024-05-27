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
inputpath ="/home/reyes/dev/posdoc-2022-2024/databases/retc/emisiones/em_2012.csv"
output_path="out_ppr_1/"

# Encabezado del archivo original "NRA"	"Establecimiento"	"Sector"	"Entidad Federativa"	"Municipio"	"Grupo Sustancia"	"Sustancia"	"CAS"	"Unidad"	"Aire"	"Agua"	"Suelo"	"Reutilización"	"Reciclado"	"Coprocesamiento"	"Tratamiento"	"Disposición Final"	"Alcantarillado"	"Incineración"	"Otro"

es2012 = pd.read_csv(inputpath, sep="\t",low_memory=False, encoding='utf-8')
en = es2012.copy()


#Se agregan las columnas que faltan
es2012["anio"] = 2012
en["year"] = 2012
#Se renombran las columnas 
es2012.rename(columns = {'NRA':'nra'}, inplace = True)
es2012.rename(columns = {'Establecimiento':'nombre'}, inplace = True)
es2012.rename(columns = {'Sector':'sector'}, inplace = True)
es2012.rename(columns = {'Entidad Federativa':'estado'}, inplace = True)
es2012.rename(columns = {'Municipio':'municipio'}, inplace = True)
es2012.rename(columns = {'Grupo Sustancia':'gruposustancia'}, inplace = True)
es2012.rename(columns = {'Sustancia':'sustancia'}, inplace = True)
es2012.rename(columns = {'CAS':'cas'}, inplace = True)
es2012.rename(columns = {'Unidad':'unidad'}, inplace = True)
es2012.rename(columns = {'Aire':'em_aire'}, inplace = True)
es2012.rename(columns = {'Agua':'em_agua'}, inplace = True)
es2012.rename(columns = {'Suelo':'em_suelo'}, inplace = True)
es2012.rename(columns = {'Reutilización':'tr_reutilizacion'}, inplace = True)
es2012.rename(columns = {'Reciclado':'tr_reciclado'}, inplace = True)
es2012.rename(columns = {'Coprocesamiento':'tr_coprocesamiento'}, inplace = True)
es2012.rename(columns = {'Tratamiento':'tr_tratamiento'}, inplace = True)
es2012.rename(columns = {'Disposición Final':'tr_dispfinal'}, inplace = True)
es2012.rename(columns = {'Alcantarillado':'tr_alcantarillado'}, inplace = True)
es2012.rename(columns = {'Incineración':'tr_incineracion'}, inplace = True)
es2012.rename(columns = {'Otro':'tr_otros'}, inplace = True)

print("\tSe ordenan las columnas")
es2012 = es2012.reindex(sorted(es2012.columns), axis=1)

en.rename(columns = {
        "NRA"	:"nra",
        "Establecimiento"	:"establishmentname",
        "Sector"	:"sector",
        "Entidad Federativa"	:"entityname",
        "Municipio"	:"municipalityname",
        "Grupo Sustancia"	:"substancegroup",
        "CAS"	:"cas",
        "Sustancia"	:"substancename",
        "Unidad"	:"unit",
        "Aire"	:"air",
        "Agua"	:"water",
        "Suelo"	:"soil",
        "Reutilización"	:"sewageforreuse",
        "Reciclado"	:"recycling",
        "Coprocesamiento"	:"co-processing",
        "Tratamiento"	:"treatment",
        "Disposición Final"	:"finaldisposition",
        "Alcantarillado"	:"sewerage",
        "Incineración"	:"incineration",
        "Otro"	:"others",
}, inplace = True)
#print(es2012.columns)


en = en.reindex(columns=["year", "cas", "water", "air", "soil", "entityname", "substancegroup", "municipalityname", "establishmentname", "nra"
                             , "sector", "substancename", "sewerage", "co-processing", "finaldisposition", "incineration", "others", "recycling"
                             , "sewageforreuse", "treatment", "unit"])

outputname = "{}es_{}.csv".format(output_path, 2012)
outputname_en = "{}en_{}.csv".format(output_path, 2012)
es2012.to_csv(outputname, sep="\t", header=True, index=False)
en.to_csv(outputname_en, sep="\t", header=True, index=False)

#print(es2012.head())


