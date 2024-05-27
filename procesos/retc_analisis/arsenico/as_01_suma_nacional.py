import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#plt.figure(figsize=(10,9))

name = "suma_emisiones_por_ton_1"
#name = "suma_emisiones_por_cas"
df = pd.read_csv("{}.csv".format(name))


df.set_index('cas', inplace=True)
df['sum'] = df.sum(axis=1) 
df = df.sort_values("sum", ascending=False)

del df['sum']


fig,ax = plt.subplots(figsize=(40,20))


ax = sns.heatmap(df, annot=True, annot_kws={"size": 20}, fmt='g', cmap="Blues")


cbar = ax.collections[0].colorbar
cbar.ax.tick_params(labelsize=25)
ax.collections[0].colorbar.set_label("Cantidad (Toneladas/Año)", size=25)


plt.xticks(size=25, rotation=1)
plt.yticks(size=25, rotation=1)




plt.ylabel('Números CAS registrados para Arsénico', size=30)
plt.xlabel('Tipo de emisión o transferencia', size=30)
plt.title("Emisiones y transferencias de Arsénico a nivel nacional\nregistradas en el RETC agrupadas por número CAS", size=30, fontweight="bold")


fig.subplots_adjust(
    #top=0.981,
    #bottom=0.049,
    left=0.1,
    right=1,
    #hspace=0.2,
    wspace=0.99
)

plt.savefig('figs/heatmap_arsenico_2004-2022.jpg')