import pandas as pd

#Este formato se aplica a dos años
listado = [2004, 2005]

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
    es["scian"] = "Atributo no considerado en este año"
    es["descscian"] = "Atributo no considerado en este año"
    es["subsector"] = "Atributo no considerado en este año"
    es["claveambiental"] = "Atributo no considerado en este año"

    es.rename(columns = {
        "NRA":"nra",
        "Nombre":"establecimiento",
        "Sector":"sector",
        "Actividad principal":"actprincipal",
        "Parque o puerto industrial":"parqueindustrial",
        "Coordenada UTM X":"utmx",
        "Coordenada UTM Y":"utmy",
        "Latitud Norte":"latitudnorte",
        "Longitud Oeste":"longitudoeste",
        "Calle":"calle",
        "No. Exterior":"numexterior",
        "No. Interior":"numinterior",
        "Colonia":"colonia",
        "Localidad":"localidad",
        "Estado":"estado",
        "Delegación\Municipio":"municipio",
        "Código postal":"codigopostal",
        "Actividad principal SEMARNAT":"actsemarnat",
        "Entre calle 1":"entrec1",
        "Entre calle 2":"entrec2",
    }, inplace = True)

    print("\tSe ordenan las columnas")
    es = es.reindex(sorted(es.columns), axis=1)
    #print(es.columns)


    outputname = "{}{}.csv".format(output_path, archivo)
    es.to_csv(outputname, sep="\t", header=True, index=False)

    


