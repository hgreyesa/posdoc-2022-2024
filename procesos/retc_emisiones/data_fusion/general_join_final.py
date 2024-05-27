import pandas as pd
import os
import logging
import datetime




ct = datetime.datetime.now()
cname = "logs_db/data_fusion_final"+str(ct) + ".log"
logging.basicConfig(filename=cname, filemode='a', level=0, format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')
rootLogger = logging.getLogger()
consoleHandler = logging.StreamHandler()
rootLogger.addHandler(consoleHandler)


def checkPath(parent_dir):
    try:
        if not os.path.exists(parent_dir):
            logging.warning("El path: " + parent_dir + " no existe, se crea la carpeta")
            os.mkdir(parent_dir)
        else:
            logging.info("El path: " + parent_dir + " existe, no es necesario crearlo nuevamente")
                
    except OSError as error:
        logging.warning(error)  


def join_r():
    f= "input/emisiones.json"
    f2="input/establecimientos.json"

    logging.info("\tIniciando la lectura del archivo: " + f)
    #emisiones = pd.read_csv(f, encoding='utf-8')
    emisiones = pd.read_json(f, encoding='utf-8')

    logging.info("\tIniciando la lectura del archivo: " + f2)
    #emisoras = pd.read_csv(f2, encoding='utf-8')
    emisoras = pd.read_json(f2, encoding='utf-8')
    emisoras_emisores = emisiones.merge(emisoras, on=['anio', 'cve_ent', 'nra'], how='right')

    output_path="output/emisiones_emisoras_r.csv"
    output_path_json="output/emisiones_emisoras_r.json"
    logging.info("\tGuardando el archivo: "+ output_path )
    emisoras_emisores.to_csv(output_path, sep=",", header=True, index=False, encoding='utf-8')
    emisoras_emisores.to_json(output_path_json, indent=1, orient="records")

def join_l():
    f= "input/emisiones.json"
    f2="input/establecimientos.json"

    logging.info("\tIniciando la lectura del archivo: " + f)
    #emisiones = pd.read_csv(f, encoding='utf-8')
    emisiones = pd.read_json(f, encoding='utf-8')

    logging.info("\tIniciando la lectura del archivo: " + f2)
    #emisoras = pd.read_csv(f2, encoding='utf-8')
    emisoras = pd.read_json(f2, encoding='utf-8')
    emisoras_emisores = emisiones.merge(emisoras, on=['anio', 'cve_ent', 'nra'], how='left')

    output_path="output/emisiones_emisoras.csv"
    output_path_json="output/emisiones_emisoras.json"
    logging.info("\tGuardando el archivo: "+ output_path )
    emisoras_emisores.to_csv(output_path, sep=",", header=True, index=False, encoding='utf-8')
    emisoras_emisores.to_json(output_path_json, indent=1, orient="records")

def compare():
    foriginal= "input/emisiones.json"
    fjoin="output/emisiones_emisoras.json"

    logging.info("\tIniciando la lectura del archivo: " + foriginal)
    #emisoras = pd.read_csv(foriginal, encoding='utf-8')
    emisiones = pd.read_json(foriginal, encoding='utf-8')
    

    logging.info("\tIniciando la lectura del archivo: " + fjoin)
    #join = pd.read_csv(fjoin, encoding='utf-8')
    join = pd.read_json(fjoin, encoding='utf-8')


    df2 = emisiones.groupby(['anio'])['anio'].count()
    df2.to_csv("output/resumen_emissones", sep=",", header=True, index=False, encoding='utf-8')

    print(df2)

    df3 = join.groupby(['anio'])['anio'].count()
    df3.to_csv("output/resumen_join", sep=",", header=True, index=False, encoding='utf-8')

    print(df3)


def compare_r():
    foriginal= "input/emisiones.json"
    fjoin="output/emisiones_emisoras_r.json"

    logging.info("\tIniciando la lectura del archivo: " + foriginal)
    #emisoras = pd.read_csv(foriginal, encoding='utf-8')
    emisiones = pd.read_json(foriginal, encoding='utf-8')
    

    logging.info("\tIniciando la lectura del archivo: " + fjoin)
    #join = pd.read_csv(fjoin, encoding='utf-8')
    join = pd.read_json(fjoin, encoding='utf-8')


    df2 = emisiones.groupby(['anio'])['anio'].count()
    df2.to_csv("output/resumen_emissones_r.csv", sep=",", header=True, index=False, encoding='utf-8')

    print(df2)

    df3 = join.groupby(['anio'])['anio'].count()
    df3.to_csv("output/resumen_join_.csv", sep=",", header=True, index=False, encoding='utf-8')

    print(df3)

def generar_2018():
    foriginal= "input/emisiones.json"
    fjoin="output/emisiones_emisoras.json"



    logging.info("\tIniciando la lectura del archivo: " + foriginal)
    #emisoras = pd.read_csv(foriginal, encoding='utf-8')
    emisiones = pd.read_json(foriginal, encoding='utf-8')
    emisiones_2018 = emisiones.loc[emisiones["anio"]==2018]
    #emisiones_2018.to_json("output/emisiones_2018.json", indent=1, orient="records")

    print(emisiones_2018.keys())

    

    logging.info("\tIniciando la lectura del archivo: " + fjoin)
    #join = pd.read_csv(fjoin, encoding='utf-8')
    join = pd.read_json(fjoin, encoding='utf-8')
    join_2018 = join.loc[join["anio"]==2018]
    print(join_2018.keys())

    parts = join_2018[[
        'anio', 'cas', 'cve_ent', 'em_agua', 'em_aire', 'em_suelo',
       'gruposustancia', 'nra', 'sustancia', 'tr_alcantarillado',
       'tr_coprocesamiento', 'tr_dispfinal', 'tr_incineracion', 'tr_otros',
       'tr_reciclado', 'tr_reutilizacion', 'tr_tratamiento', 'unidad',
       'iarc_agent', 'iarc_group', 'iarc_info', 'iarc_volume', 'iarc_year',
       'dba_changes'
    ]]
    parts.to_json("output/join_2018.json", indent=1, orient="records")


    #diff_pd = pd.merge()

    #print(join_2018.compare(emisiones_2018))

    #age_sex = titanic[["Age", "Sex"]]


    #df = emisiones.merge(join, how='outer', indicator='union')
    #print(df[df.union=='left_only'])

def comparar_inner():
    foriginal= "input/emisiones.json"
    fjoin="output/emisiones_emisoras.json"

    logging.info("\tIniciando la lectura del archivo: " + foriginal)
    #emisoras = pd.read_csv(foriginal, encoding='utf-8')
    #emisiones = pd.read_json(foriginal, encoding='utf-8')
    emisiones_2018 = pd.read_json(foriginal, encoding='utf-8')

    emisiones_2018 = emisiones_2018[[
        'anio', 'cas', 'cve_ent', 
       'gruposustancia', 'nra', 'sustancia', 'unidad',
       'iarc_agent', 'iarc_group', 'iarc_info', 'iarc_volume', 'iarc_year',
       'dba_changes'
    ]]
    print(emisiones_2018.head())
    

    logging.info("\tIniciando la lectura del archivo: " + fjoin)
    #join = pd.read_csv(fjoin, encoding='utf-8')
    #join = pd.read_json(fjoin, encoding='utf-8')
    join_2018 =  pd.read_json(fjoin, encoding='utf-8')
    join_2018 = join_2018[[
        'anio', 'cas', 'cve_ent', 
       'gruposustancia', 'nra', 'sustancia', 'unidad',
       'iarc_agent', 'iarc_group', 'iarc_info', 'iarc_volume', 'iarc_year',
       'dba_changes'
    ]]
    print(join_2018.head())

    diff = emisiones_2018.merge(join_2018,indicator = True, how='right')
    print(diff)

    diff.to_csv("output/compare.csv", sep=",", header=True, index=False, encoding='utf-8')
    #print(emisiones_2018.keys())

    #diff = emisiones_2018.compare(join_2018, keep_equal=True, keep_shape = True)
    #print(diff)


   

join_r()
compare_r()

#logging.info("Iniciando el proceso de comparar_inner")
#comparar_inner()




    