import pandas as pd
from os import scandir



#input_path = "../../../inputs/border/"
input_path = "/home/reyes/dev/posdoc-2022-2024/inputs/border/"
output_path="output/"


#files = [f for f in os.listdir(input_path) if os.path.isfile(f)]

files = [arch.name for arch in scandir(input_path) if arch.is_file()]
df_csv_append = pd.DataFrame()

#primer_archivo = "{}{}.csv".format(input_path, nombre)
#es_init = pd.read_csv(primer_archivo, sep="\t",low_memory=False, encoding='utf-8')

for archivo in files:
    #print(archivo)
    actual = "{}{}".format(input_path, archivo)
    es_actual = pd.read_csv(actual, sep=",",low_memory=False, encoding='utf-8')
    df_csv_append = df_csv_append._append(es_actual, ignore_index=True)


outputname = "{}border_pollutant{}.csv".format(output_path, "border_pollutant")
df_csv_append.to_csv(outputname, sep=",", header=True, index=False)
 

