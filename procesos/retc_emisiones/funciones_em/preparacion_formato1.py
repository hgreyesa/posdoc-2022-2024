import pandas as pd

#Este formato se aplica a dos años
listado = [2006, 2007, 2008, 2009, 2010, 2011,
           2013, 2014, 2015, 2016,
           2017, 2018, 2019, 2020, 2021, 2022]

inputpath ="/home/reyes/dev/posdoc-2022-2024/databases/retc/emisiones/"
output_path="out_preparacion/"

for archivo in listado:
    #print("{}es_{}.csv".format(inputpath,archivo))
    filename = "{}em_{}.csv".format(inputpath,archivo)
    print(filename)

    #Se lee el archivo original    
    es = pd.read_csv(filename, sep="\t",low_memory=False, encoding='utf-8')

    #Se agregan las columnas faltantes
    es["anio"] = archivo
    es["gruposustancia"] = "Atributo no considerado en este año"

    es.rename(columns = {
        "NRA"	:"nra",
        "NOMBRE"	:"nombre",
        "SECTOR"	:"sector",
        "ESTADO"	:"estado",
        "MUNICIPIO"	:"municipio",
        "CAS"	:"cas",
        "SUSTANCIA"	:"sustancia",
        "UNIDAD"	:"unidad",
        "AIRE"	:"em_aire",
        "AGUA"	:"em_agua",
        "SUELO"	:"em_suelo",
        "REUTILIZACIÓN"	:"tr_reutilizacion",
        "RECICLADO"	:"tr_reciclado",
        "COPROCESAMIENTO"	:"tr_coprocesamiento",
        "TRATAMIENTO"	:"tr_tratamiento",
        "DISPOSICIÓN\nFINAL"	:"tr_dispfinal",
        "ALCANTARILLADO"	:"tr_alcantarillado",
        "INCINERACIÓN"	:"tr_incineracion",
        "OTROS"	:"tr_otros",
    }, inplace = True)

    #print("\tSe ordenan las columnas")
    es = es.reindex(sorted(es.columns), axis=1)
    print(es.columns)

    outputname = "{}{}.csv".format(output_path, archivo)
    es.to_csv(outputname, sep="\t", header=True, index=False)
 


