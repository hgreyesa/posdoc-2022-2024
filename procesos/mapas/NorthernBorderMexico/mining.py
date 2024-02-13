import pandas as pd
import os
#import imageio
import branca
import branca.colormap as cm
import numpy as np 

import sys
import logging #logger
LOGER = logging.getLogger()

INPUT_DATA = "../../../inputs/" + "mining_directory_uaslp_cinvestav_db_2024-02-12.csv"#sys.argv[1] #"tm_labeled.csv"
OUTPUT_PATH = "output/" #sys.argv[2] #"./results/"
NAME = "denue_mining"#sys.argv[2] #"./results/"
LAT_COLUMN = "Latitude"#sys.argv[4] #"lat"
LON_COLUMN = "Longitude"#sys.argv[5] #"lon"





def plot_maps(df):

    locat= [df[LAT_COLUMN].median(), df[LON_COLUMN].median()]
    import folium
    map_layer = folium.Map(location=locat, zoom_start=6, control_scale=True,prefer_canvas=True)

    for index, location_info in df.iterrows():

        #color = colormap(location_info[v])
        html = "<h3>%s</h3><p>Stratum: %s</br>Entity: %s</br>Municipality:%s </br>Locality: %s </br> AGEB: %s</br> Registration dat: %s</br> NAICS Code: %s</br> NAICS Name: %s </br>Latitude: %s</br>Longitude: %s</p>" % (
            location_info["Name"],
            str(location_info["Stratum"]), 
            str(location_info["Entity"]), 
            location_info["Municipality"],
            location_info["Locality"],
            location_info["AGEB"],
            location_info["rdate"],
            location_info["NAICSCode"],
            location_info["NAICSName"],
            location_info["Latitude"],
            location_info["Longitude"],
        )

        
        #micolor = "green"
#
        #if(location_info["SEMAFORO"] == "Rojo") :
        #    micolor = "red"
        #elif location_info["SEMAFORO"] == "Amarillo":
        #    micolor = "yellow"
        
        iframe = folium.IFrame(html,width=300,height=200)
        popup = folium.Popup(iframe,max_width=300,max_height=200)
        t = folium.CircleMarker(location=[location_info[LAT_COLUMN],location_info[LON_COLUMN]],
                                radius=3,
                                fill=True,
                                #color=micolor,
                                #color=location_info["SEMAFORO"].lower(),
                                popup=popup,
                                #fill_color=color
                                ).add_to(map_layer)
    
    try:
        image_path = '%s%s.html'%(OUTPUT_PATH,NAME)
        LOGER.error("GUARDANDO")
        map_layer.save(image_path)
        del map_layer
        LOGER.error(image_path)

    except Exception as e:
        LOGER.error("================= NO SE PUDO GUARDAR =======================")




pozos = pd.read_csv(INPUT_DATA, sep=",")
plot_maps(pozos)

