import pandas as pd

#Este formato se aplica a dos años
listado = [2006, 2007, 2008, 2009, 2010, 2011,
           2013, 2014, 2015, 2016]

inputpath ="/home/reyes/dev/posdoc-2022-2024/databases/retc/emisoras/"
output_path="out_preparacion/"

for archivo in listado:
    #print("{}es_{}.csv".format(inputpath,archivo))
    filename = "{}es_{}.csv".format(inputpath,archivo)
    print(filename)

    #Se lee el archivo original    
    es = pd.read_csv(filename, sep="\t",low_memory=False, encoding='utf-8')

    #Se agregan las columnas faltantes
    es["anio"] = archivo
    es["actsemarnat"] = "Atributo no considerado en este año"
    es["entrec1"] = "Atributo no considerado en este año"
    es["entrec2"] = "Atributo no considerado en este año"

    es.rename(columns = {
        "NRA":"nra",
        "NOMBRE":"establecimiento",
        "SCIAN":"scian",
        "DESCRIPCIÓN SCIAN":"descscian",
        "SECTOR":"sector",
        "CLAVE\nAMBIENTAL":"claveambiental",
        "SUBSECTOR":"subsector",
        "PRINCIPAL ACTIVIDAD PRODUCTIVA":"actprincipal",
        "PARQUE INDUSTRIAL":"parqueindustrial",
        "COORDENADA \nUTM X":"utmx",
        "COORDENADA \nUTM Y":"utmy",
        "LATITUD \nNORTE":"latitudnorte",
        "LONGITUD \nOESTE":"longitudoeste",
        "CALLE":"calle",
        "NÚM. EXT":"numexterior",
        "NÚM. INT":"numinterior",
        "COLONIA":"colonia",
        "LOCALIDAD":"localidad",
        "ESTADO":"estado",
        "MUNICIPIO":"municipio",
        "C.P.":"codigopostal",
    }, inplace = True)

    #print("\tSe ordenan las columnas")
    es = es.reindex(sorted(es.columns), axis=1)
    print(es.columns)

    outputname = "{}{}.csv".format(output_path, archivo)
    es.to_csv(outputname, sep="\t", header=True, index=False)

segundoListado = [2017, 2018, 2019, 2020, 2021, 2022]
for archivo in segundoListado:
    #print("{}es_{}.csv".format(inputpath,archivo))
    filename = "{}es_{}.csv".format(inputpath,archivo)
    #print(filename)

    #Se lee el archivo original    
    es = pd.read_csv(filename, sep="\t",low_memory=False, encoding='utf-8')

    #Se agregan las columnas faltantes
    es["anio"] = archivo
    es["actsemarnat"] = "Atributo no considerado en este año"
    es["entrec1"] = "Atributo no considerado en este año"
    es["entrec2"] = "Atributo no considerado en este año"

    es.rename(columns = {
        "NRA":"nra",
        "NOMBRE":"establecimiento",
        "SCIAN":"scian",
        "DESCRIPCIÓN SCIAN":"descscian",
        "SECTOR":"sector",
        "CLAVE\nAMBIENTAL":"claveambiental",
        "SUBSECTOR":"subsector",
        "PRINCIPAL ACTIVIDAD PRODUCTIVA":"actprincipal",
        "PARQUE INDUSTRIAL":"parqueindustrial",
        "COORDENADA\nUTM X":"utmx",
        "COORDENADA\nUTM Y":"utmy",
        "LATITUD NORTE":"latitudnorte",
        "LONGITUD \nOESTE":"longitudoeste",
        "CALLE":"calle",
        "NÚM. EXT":"numexterior",
        "NÚM. INT":"numinterior",
        "COLONIA":"colonia",
        "LOCALIDAD":"localidad",
        "ESTADO":"estado",
        "MUNICIPIO":"municipio",
        "C.P.":"codigopostal",
    }, inplace = True)

    #print("\tSe ordenan las columnas")
    es = es.reindex(sorted(es.columns), axis=1)
    print(es.columns)


    outputname = "{}{}.csv".format(output_path, archivo)
    es.to_csv(outputname, sep="\t", header=True, index=False)
    


