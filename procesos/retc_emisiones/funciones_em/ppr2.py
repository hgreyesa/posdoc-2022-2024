import pandas as pd

input_path="out_ppr_1/"
output_path="out_ppr_2/"
df_csv_es_append = pd.DataFrame()
df_csv_en_append = pd.DataFrame()

#primer_archivo = "{}{}.csv".format(input_path, nombre)
#es_init = pd.read_csv(primer_archivo, sep="\t",low_memory=False, encoding='utf-8')

for archivo in range(2004,2023):
    actual = "{}es_{}.csv".format(input_path, archivo)
    actual_en = "{}en_{}.csv".format(input_path, archivo)
    es_actual = pd.read_csv(actual, sep="\t",low_memory=False, encoding='utf-8')
    en_actual = pd.read_csv(actual_en, sep="\t",low_memory=False, encoding='utf-8')
    df_csv_es_append = df_csv_es_append._append(es_actual, ignore_index=True)
    df_csv_en_append = df_csv_en_append._append(en_actual, ignore_index=True)




outputname = "{}es_{}.csv".format(output_path, "2004-2022")
outputname_en = "{}en_{}.csv".format(output_path, "2004-2022")
df_csv_es_append.to_csv(outputname, sep="\t", header=True, index=False)
df_csv_en_append.to_csv(outputname_en, sep="\t", header=True, index=False)
 

