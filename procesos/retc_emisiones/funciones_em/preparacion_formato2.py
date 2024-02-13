import pandas as pd

#Este formato se aplica a dos años
listado = [2004, 2005]

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
    es["municipio"] = "Atributo no considerado en este año"
    es["gruposustancia"] = "Atributo no considerado en este año"

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

    print("\tSe ordenan las columnas")
    es = es.reindex(sorted(es.columns), axis=1)
    #print(es.columns)


    outputname = "{}{}.csv".format(output_path, archivo)
    es.to_csv(outputname, sep="\t", header=True, index=False)

    


