import pandas as pd


inputpath ="/home/reyes/dev/posdoc-2022-2024/databases/retc/emisiones/em_2017.csv"


#Se lee el archivo original    
es = pd.read_csv(inputpath, sep="\t",low_memory=False, encoding='utf-8')

print(es.columns)