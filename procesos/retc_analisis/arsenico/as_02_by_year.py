from pymongo import MongoClient
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from dbCon import *


def init_df():
    columns = [
        "cas",
        "sustancia",
        "anio",
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
                "anio": 0,
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


def get_data():

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
        print("\tSe realiza el recorrido por año")
        for anio in range(2004,2023):
            print("\t\t{} {}".format(cas, anio))

            agg_result = db.retc_2004_2022_complete.aggregate(
                [
                    {
                        '$match': {
                            '$and': [
                                {
                                    'cas': cas
                                }, {
                                    'anio': anio
                                }
                            ]
                        }
                    }, {
                        '$group': {
                            '_id': {
                                'cas': '$cas', 
                                'sustancia': '$sustancia', 
                                'anio': '$anio'
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
                            'anio': '$_id.anio', 
                            'sustancia': '$_id.sustancia', 
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
                new_row["anio"] = data["anio"]
                new_row["sustancia"] = data["sustancia"]
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

        newcas = cas.replace("/","")
        output_name = "input/{}_{}_{}.csv".format("heatmap", "arsenico", newcas)

        new_df.to_csv(output_name, index=False)

        del new_df

        #print(cas)



def plot_v2(cas, newcas):
    inputpath ="input/heatmap_arsenico_{}.csv".format(newcas)
    df = pd.read_csv(inputpath, sep=",",low_memory=False, encoding='utf-8')

    #del df["cas"]

    sustancia_nombre = df["sustancia"].iloc[0]

    del df["cas"]
    del df["sustancia"]

    #del df['anio']
    df.set_index('anio', inplace=True)
    df['sum'] = df.sum(axis=1) 
    df = df.sort_values("sum", ascending=False)
    del df['sum']

    plt.figure(figsize=(40, 20))
    ax = sns.heatmap(df, annot=True, annot_kws={"size": 20}, fmt='g', cmap="Blues")
    #ax.collections[0].colorbar.set_label("Hello")
    cbar = ax.collections[0].colorbar
    cbar.ax.tick_params(labelsize=25)
    ax.collections[0].colorbar.set_label("Cantidad (Toneladas/Año)", size=25)
    #ax.collections[0].colorbar.labelsize(2)

    plt.xticks(size=25, rotation=1)
    plt.yticks(size=25, rotation=1)


    plt.ylabel('Año que aparece en el RETC', size=30)
    plt.xlabel('Tipo de emisión y transferencia', size=30)
    plt.title("Cantidad de Emisiones y transferencias\nregistradas en la base de datos del RETC para \n{}, número CAS: {}".format(sustancia_nombre, cas), size=30, fontweight="bold")
    #plt.suptitle("", size=30)

    sustancia_nombre = sustancia_nombre.replace("/","")
    sustancia_nombre = sustancia_nombre.replace(" ","_")
    sustancia_nombre = sustancia_nombre.replace("(","-")
    sustancia_nombre = sustancia_nombre.replace(")","-")

    plt.savefig("figs/{}_{}_{}_by_year.jpg".format("heatmap", sustancia_nombre, newcas))
#doall()

#plot_as()

#get_data()

num_cas = ["7440-38-2", "As", "S/C1"]

for cas in num_cas:

    newcas = cas.replace("/","")
    plot_v2(cas, newcas)
