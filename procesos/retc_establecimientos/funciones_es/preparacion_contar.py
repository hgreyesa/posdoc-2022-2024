import pandas as pd

input_path="out_preparacion/"


for archivo in range(2004,2023):
    actual = "{}{}.csv".format(input_path, archivo)
    es_actual = pd.read_csv(actual, sep="\t",low_memory=False, encoding='utf-8')
    print("{}\t{}".format(archivo, len(es_actual.index)))
    #df_csv_append = df_csv_append._append(es_actual, ignore_index=True)


input_path="out_append/2004-2022.csv"
#actual = "{}{}.csv".format(input_path, archivo)
es_actual = pd.read_csv(input_path, sep="\t",low_memory=False, encoding='utf-8')
print("{}\t{}".format(input_path, len(es_actual.index)))