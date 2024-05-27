import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#plt.figure(figsize=(10,9))

inputpath ="/home/reyes/productos_rnca/2024/retc/analisis/arsenico/periodocompleto/"
name = "suma_emisiones_por_ton_1"

df = pd.read_csv("{}{}.csv".format(inputpath, name))


df.set_index('cas', inplace=True)
df['sum'] = df.sum(axis=1) 
df = df.sort_values("sum", ascending=False)

del df['sum']

#partitions = 5
#dfs = np.array_split(df, partitions)
#cmap = sns.cm.rocket_r
plt.figure(figsize=(50, 20))
#sns.heatmap(df, annot=True,vmax=8252476,vmin=0, annot_kws={"size": 10}, fmt=".2") #8252475.37622382
ax = sns.heatmap(df, annot=True, annot_kws={"size": 20}, fmt='g', cmap="Blues") #8252475.37622382

cbar = ax.collections[0].colorbar
# here set the labelsize by 20
cbar.ax.tick_params(labelsize=30)

#sns.heatmap(df, annot=True,vmax=13460,vmin=0, annot_kws={"size": 16, 'rotation': 90})

sns.color_palette("flare", as_cmap=True)


#plt.xticks(size=20,rotation=90)
plt.xticks(size=20, rotation=1)
plt.yticks(size=25, rotation=1)




plt.ylabel('Emisiones (Toneladas/Año) reportadas por cada CAS de Arsénico', size=30)
plt.xlabel('Tipo de emisión y transferencia', size=30)
plt.title("Emisiones y transferencias de Arsénico a nivel nacional\nagrupadas por número CAS", size=30)
#plt.suptitle("", size=30)

plt.savefig('heatmap_emisiones_arsenico_2004-2022.jpg')