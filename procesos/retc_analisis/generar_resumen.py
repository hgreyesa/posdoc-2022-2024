import pandas as pd



inputpath ="/home/reyes/backup/retc20042022fusionada/retc_2004_2022_complete.csv"
joined = pd.read_csv(inputpath, sep=",",low_memory=False, encoding='utf-8')
#data = pd.read_csv("", encoding='utf-8',sep=",", low_memory=False),

new_columns = joined.columns

print(new_columns)

to_analize = joined[[
    "anio", "cve_ent","cve_mun",'estado', 'municipio', 'localidad', 'nra', 'sector', 'sustancia', 'unidad', 'iarc_group',
    'em_agua', 'em_aire', 'em_suelo', 
    'tr_alcantarillado', 'tr_coprocesamiento', 'tr_dispfinal', 'tr_incineracion', 'tr_otros', 'tr_reciclado', 'tr_reutilizacion', 'tr_tratamiento',
    'enentidad', 'enmexico', 'enmunicipio'
]]



print(to_analize.head())