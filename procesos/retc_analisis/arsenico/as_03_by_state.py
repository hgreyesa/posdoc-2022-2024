from pymongo import MongoClient
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from dbCon import *


def init_df():
    columns = [
        "cas",
        "sustancia",
        "Clave Entidad",
        "Entidad",
        "Aire",
        "Agua",
        "Suelo",
        "Alcant.",
        "Coproc.",
        "Disp. F.",
        "Inciner.",
        "Otros",
        "Reciclado",
        "Reutiliza.",
        "Tratamien."]
    
    df_data = pd.DataFrame(columns=columns)
    return df_data

def init_row(cas):
    new_row = {
                "cas": cas,
                "sustancia": "",
                "Clave Entidad": 0,
                "Entidad": "",
                "Aire": 0,
                "Agua": 0,
                "Suelo": 0,
                "Alcant.": 0,
                "Coproc.": 0,
                "Disp. F.": 0,
                "Inciner.": 0,
                "Otros": 0,
                "Reciclado": 0,
                "Reutiliza.": 0,
                "Tratamien.": 0
    }
    return new_row

def draw_plot(df, cas, anio):
    #del df['anio']
    df.set_index('cas', inplace=True)
    df['sum'] = df.sum(axis=1) 
    df = df.sort_values("sum", ascending=False)
    del df['sum']

    plt.figure(figsize=(40, 20))
    ax = sns.heatmap(df, annot=True, annot_kws={"size": 20}, fmt='g', cmap="Blues")
    cbar = ax.collections[0].colorbar
    cbar.ax.tick_params(labelsize=25)

    plt.xticks(size=25, rotation=1)
    plt.yticks(size=25, rotation=1)


    plt.ylabel('Cantidad de Emisiones y Transferencias (Toneladas/Año) registradas', size=30)
    plt.xlabel('Tipo de emisión y transferencia', size=30)
    plt.title("Emisiones y transferencias de Arsénico ({}) registradas en el RETC\nrealizadas en el año {}".format(cas,anio), size=30)
    #plt.suptitle("", size=30)

    plt.savefig("figs/{}_{}_{}_{}.jpg".format("heatmap", "arsenico", cas, anio))

def get_data_by_state():

    print("Se crea el dataframe")
    df_data = init_df()

    print("Se crear el arreglo de cas")
    num_cas = ["7440-38-2", "As", "S/C1"]

    print("Se realiza la conexión con la base de datos")
    mc = getMongoClientSemarnatReader()
    db = getDbCollectionSemarnat(mc, "semarnat")

    print("Se inicia el recorrido por sustancia")
    for cas in num_cas:
        print("\tSe crear el row para el cas {}".format(cas))
        new_row = init_row(cas)
        print("\tSe realiza el recorrido por clave entidad")
        #for anio in range(2004,2023):
        for cve_ent in range(1, 33):
            print("\t\t{} {}".format(cas, cve_ent))

            agg_result = db.retc_2004_2022_complete.aggregate(
                [
                    {
                        '$match': {
                            '$and': [
                                {
                                    'cas': cas
                                }, {
                                    'cve_ent': cve_ent
                                }
                            ]
                        }
                    }, {
                        '$group': {
                            '_id': {
                                'cas': '$cas', 
                                'sustancia': '$sustancia', 
                                'cve_ent': '$cve_ent',
                                'entidad': '$estado',
                            }, 
                            'aire': {
                                '$sum': '$em_aire'
                            }, 
                            'agua': {
                                '$sum': '$em_agua'
                            }, 
                            'suelo': {
                                '$sum': '$em_suelo'
                            }, 
                            'alcantarillado': {
                                '$sum': '$tr_alcantarillado'
                            }, 
                            'coprocesamiento': {
                                '$sum': '$tr_coprocesamiento'
                            }, 
                            'dispfinal': {
                                '$sum': '$tr_dispfinal'
                            }, 
                            'incineracion': {
                                '$sum': '$tr_incineracion'
                            }, 
                            'otros': {
                                '$sum': '$tr_otros'
                            }, 
                            'reciclado': {
                                '$sum': '$tr_reciclado'
                            }, 
                            'reutilizacion': {
                                '$sum': '$tr_reutilizacion'
                            }, 
                            'tratamiento': {
                                '$sum': '$tr_tratamiento'
                            }
                        }
                    }, {
                        '$project': {
                            '_id': 0, 
                            'cas': '$_id.cas', 
                            'sustancia': '$_id.sustancia', 
                            'cve_ent': '$_id.cve_ent', 
                            'entidad': '$_id.entidad', 
                            'aire': {
                                '$divide': [
                                    '$aire', 1000
                                ]
                            }, 
                            'agua': {
                                '$divide': [
                                    '$agua', 1000
                                ]
                            }, 
                            'suelo': {
                                '$divide': [
                                    '$suelo', 1000
                                ]
                            }, 
                            'alcantarillado': {
                                '$divide': [
                                    '$alcantarillado', 1000
                                ]
                            }, 
                            'coprocesamiento': {
                                '$divide': [
                                    '$coprocesamiento', 1000
                                ]
                            }, 
                            'dispfinal': {
                                '$divide': [
                                    '$dispfinal', 1000
                                ]
                            }, 
                            'incineracion': {
                                '$divide': [
                                    '$incineracion', 1000
                                ]
                            }, 
                            'otros': {
                                '$divide': [
                                    '$otros', 1000
                                ]
                            }, 
                            'reciclado': {
                                '$divide': [
                                    '$reciclado', 1000
                                ]
                            }, 
                            'reutilizacion': {
                                '$divide': [
                                    '$reutilizacion', 1000
                                ]
                            }, 
                            'tratamiento': {
                                '$divide': [
                                    '$tratamiento', 1000
                                ]
                            }
                        }
                    }
                ]
            )

           

            for data in agg_result:
                new_row["cas"] = data["cas"]
                new_row["sustancia"] = data["sustancia"]
                new_row["Clave Entidad"] = data["cve_ent"]
                new_row["Entidad"] = data["entidad"]
                new_row["Aire"] = data["aire"]
                new_row["Agua"] = data["agua"]
                new_row["Suelo"] = data["suelo"]
                new_row["Alcant."] = data["alcantarillado"]
                new_row["Coproc."] = data["coprocesamiento"]
                new_row["Disp. F."] = data["dispfinal"]
                new_row["Inciner."] = data["incineracion"]
                new_row["Otros"] = data["otros"]
                new_row["Reciclado"] = data["reciclado"]
                new_row["Reutiliza."] = data["reutilizacion"]
                new_row["Tratamien."] = data["tratamiento"]
                df_data.loc[len(df_data.index)] = new_row


    
        new_df = df_data[(df_data["cas"]==cas)]
            

        #draw_plot(new_df, cas, anio)

        newcas = cas.replace("/","_")
        output_name = "input/{}_{}_{}_by_entidad.csv".format("heatmap", "arsenico", newcas)

        new_df.to_csv(output_name, index=False)

        del new_df

        #print(cas)


def plot_as():
    inputpath ="input/heatmap_arsenico_7440-38-2.csv"
    df = pd.read_csv(inputpath, sep=",",low_memory=False, encoding='utf-8')

    #del df["cas"]

    cas = df["cas"].iloc[0]

    del df["cas"]

    df.set_index('anio', inplace=True)
    df['sum'] = df.sum(axis=1) 
    df = df.sort_values("sum", ascending=False)
    del df['sum']

    print(df.columns)

    grid_kws = {"height_ratios": (.9, .02), "hspace": .20}

    f, (ax, cbar_ax) = plt.subplots(2, gridspec_kw=grid_kws, figsize=(30,12))

    sns.set_theme(font_scale=30)
    
    ax = sns.heatmap(df, ax=ax,
    cbar_ax=cbar_ax,
    annot=True, annot_kws={"size": 20}, fmt='g', cmap="Blues",
    cbar_kws={"orientation": "horizontal","label": "Cantidad de Emisiones y Transferencias (Toneladas/Año)"}
    )

    cbar = ax.collections[0].colorbar
    cbar.ax.tick_params(labelsize=20)

    ax.figure.axes[-1].xaxis.label.set_size(20)
    ax.figure.axes[0].xaxis.label.set_size(20)


    ax.set_title("Emisiones y transferencias de Arsénico ({})\nregistradas en el RETC".format(cas), 
       fontsize=30, fontweight="bold")
    
 
    ax.set_xlabel('Tipo de emision o transferencia', fontsize = 25)
    ax.set_ylabel('Año', fontsize = 25)

    ax.set_xticklabels(list(df.columns), size = 25, rotation=1)
    ax.set_yticklabels(list(df.index), size = 25, rotation=1)

    plt.savefig("figs/{}_{}_{}.jpg".format("heatmap", "arsenico", cas))

def plot_v2(cas, newcas):
    inputpath ="input/heatmap_arsenico_{}_by_entidad.csv".format(newcas)
    df = pd.read_csv(inputpath, sep=",",low_memory=False, encoding='utf-8')

    sustancia_nombre = df["sustancia"].iloc[0]

    del df["cas"]
    del df["sustancia"]
    del df["Clave Entidad"]


    #del df['anio']
    df.set_index('Entidad', inplace=True)
    df['sum'] = df.sum(axis=1) 
    df = df.sort_values("sum", ascending=False)
    del df['sum']

    #plt.figure(figsize=(40, 20))
    fig,ax = plt.subplots(figsize=(40,20))
    ax = sns.heatmap(df, annot=True, annot_kws={"size": 20}, fmt='g', cmap="Blues")
    #ax.collections[0].colorbar.set_label("Hello")
    cbar = ax.collections[0].colorbar
    cbar.ax.tick_params(labelsize=25)
    ax.collections[0].colorbar.set_label("Cantidad (Toneladas/Año)", size=25)
    #ax.collections[0].colorbar.labelsize(2)

    plt.xticks(size=25, rotation=1)
    plt.yticks(size=25, rotation=1)


    plt.ylabel('Entidad', size=30)
    plt.xlabel('Tipo de emisión y transferencia', size=30)
    #plt.title("Emisiones y transferencias de Arsénico ({})\nregistradas en el RETC\npor entidad".format(cas), size=30, fontweight="bold")
    plt.title("Cantidad de Emisiones y transferencias\nregistradas en la base de datos del RETC para \n{}, número CAS: {}".format(sustancia_nombre, cas), size=30, fontweight="bold")

    #plt.suptitle("", size=30)

    fig.subplots_adjust(
        #top=0.981,
        #bottom=0.049,
        left=0.18,
        right=1,
        #hspace=0.2,
        wspace=0.99
    )

    sustancia_nombre = sustancia_nombre.replace("/","")
    sustancia_nombre = sustancia_nombre.replace(" ","_")
    sustancia_nombre = sustancia_nombre.replace("(","-")
    sustancia_nombre = sustancia_nombre.replace(")","-")

    plt.savefig("figs/{}_{}_{}_by_entidad.jpg".format("heatmap", sustancia_nombre, newcas))

#get_data_by_state()


num_cas = ["7440-38-2", "As", "S/C1"]

for cas in num_cas:
    newcas = cas.replace("/","_")
    plot_v2(cas, newcas)

#cas = "S/C1"
#newcas = cas.replace("/","_")
#plot_v2(cas, newcas)
