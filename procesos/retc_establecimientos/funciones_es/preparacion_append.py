import pandas as pd

input_path="out_preparacion/"
output_path="out_append/"
df_csv_append = pd.DataFrame()

#primer_archivo = "{}{}.csv".format(input_path, nombre)
#es_init = pd.read_csv(primer_archivo, sep="\t",low_memory=False, encoding='utf-8')

for archivo in range(2004,2023):
    actual = "{}{}.csv".format(input_path, archivo)
    es_actual = pd.read_csv(actual, sep="\t",low_memory=False, encoding='utf-8')
    df_csv_append = df_csv_append._append(es_actual, ignore_index=True)


outputname = "{}{}.csv".format(output_path, "2004-2022")
df_csv_append.to_csv(outputname, sep="\t", header=True, index=False)
 

