import pandas as pd

#Este formato se aplica a dos años
listado = [2006, 2007, 2008, 2009, 2010, 2011,
           2013, 2014, 2015, 2016,
           2017, 2018, 2019, 2020, 2021, 2022]

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
    en["year"] = archivo
    es["gruposustancia"] = "*"
    en["substancegroup"] = "*"

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

    en.rename(columns = {
        "NRA"	:"nra",
        "NOMBRE"	:"establishmentname",
        "SECTOR"	:"sector",
        "ESTADO"	:"entityname",
        "MUNICIPIO"	:"municipalityname",
        "CAS"	:"cas",
        "SUSTANCIA"	:"substancename",
        "UNIDAD"	:"unit",
        "AIRE"	:"air",
        "AGUA"	:"water",
        "SUELO"	:"soil",
        "REUTILIZACIÓN"	:"sewageforreuse",
        "RECICLADO"	:"recycling",
        "COPROCESAMIENTO"	:"co-processing",
        "TRATAMIENTO"	:"treatment",
        "DISPOSICIÓN\nFINAL"	:"finaldisposition",
        "ALCANTARILLADO"	:"sewerage",
        "INCINERACIÓN"	:"incineration",
        "OTROS"	:"others",
    }, inplace = True)

    #print("\tSe ordenan las columnas")
    es = es.reindex(sorted(es.columns), axis=1)
    en = en.reindex(columns=["year", "cas", "water", "air", "soil", "entityname", "substancegroup", "municipalityname", "establishmentname", "nra"
                             , "sector", "substancename", "sewerage", "co-processing", "finaldisposition", "incineration", "others", "recycling"
                             , "sewageforreuse", "treatment", "unit"])
    print(es.columns)

    outputname = "{}es_{}.csv".format(output_path, archivo)
    outputname_en = "{}en_{}.csv".format(output_path, archivo)
    es.to_csv(outputname, sep="\t", header=True, index=False)
    en.to_csv(outputname_en, sep="\t", header=True, index=False)
 


