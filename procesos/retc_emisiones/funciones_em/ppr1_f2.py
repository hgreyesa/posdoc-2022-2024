import pandas as pd

#Este formato se aplica a dos años
listado = [2004, 2005]

inputpath ="/home/reyes/dev/posdoc-2022-2024/databases/retc/emisiones/"
output_path="out_ppr_1/"

for archivo in listado:
    #print("{}es_{}.csv".format(inputpath,archivo))
    filename = "{}em_{}.csv".format(inputpath,archivo)
    print(filename)

    #Se lee el archivo original    
    es = pd.read_csv(filename, sep="\t",low_memory=False, encoding='utf-8')
    en = es.copy()


    #Se agregan las columnas faltantes
    es["anio"] = archivo
    es["municipio"] = "*"
    es["gruposustancia"] = "*"


    en["year"] = archivo
    en["municipalityname"] = "*"
    en["substancegroup"] = "*"

    es.rename(columns = {
        "NRA"	:"nra",
        "Nombre"	:"nombre",
        "Sector"	:"sector",
        "Estado"	:"estado",
        "No. CAS"	:"cas",
        "Descripción"	:"sustancia",
        "Unidad"	:"unidad",
        "Aire"	:"em_aire",
        "Agua"	:"em_agua",
        "Suelo"	:"em_suelo",
        "Reuso"	:"tr_reutilizacion",
        "Reciclado"	:"tr_reciclado",
        "Coprocesamiento"	:"tr_coprocesamiento",
        "Tratamiento"	:"tr_tratamiento",
        "Disposición final"	:"tr_dispfinal",
        "Incineración"	:"tr_incineracion",
        "Alcantarillado"	:"tr_alcantarillado",
        "Otros"	:"tr_otros",
    }, inplace = True)

    en.rename(columns = {
        "NRA"	:"nra",
        "Nombre"	:"establishmentname",
        "Sector"	:"sector",
        "Estado"	:"entityname",
        #"MUNICIPIO"	:"municipalityname",
        "No. CAS"	:"cas",
        "Descripción"	:"substancename",
        "Unidad"	:"unit",
        "Aire"	:"air",
        "Agua"	:"water",
        "Suelo"	:"soil",
        "Reuso"	:"sewageforreuse",
        "Reciclado"	:"recycling",
        "Coprocesamiento"	:"co-processing",
        "Tratamiento"	:"treatment",
        "Disposición final"	:"finaldisposition",
        "Alcantarillado"	:"sewerage",
        "Incineración"	:"incineration",
        "Otros"	:"others",
    }, inplace = True)

    print("\tSe ordenan las columnas")
    es = es.reindex(sorted(es.columns), axis=1)
    en = en.reindex(columns=["year", "cas", "water", "air", "soil", "entityname", "substancegroup", "municipalityname", "establishmentname", "nra"
                             , "sector", "substancename", "sewerage", "co-processing", "finaldisposition", "incineration", "others", "recycling"
                             , "sewageforreuse", "treatment", "unit"])
    #print(es.columns)


    outputname = "{}es_{}.csv".format(output_path, archivo)
    outputname_en = "{}en_{}.csv".format(output_path, archivo)
    es.to_csv(outputname, sep="\t", header=True, index=False)
    en.to_csv(outputname_en, sep="\t", header=True, index=False)

    

    


