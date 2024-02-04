## [Calidad del agua en Mexico](https://www.gob.mx/conagua/articulos/calidad-del-agua) acuiferos superficiales y subterraneos

## Datos disponibles

La base de datos correspondientes a los indicadores caldiad del agua es dividido en dos categorías distintas:

1. **Indicadores de calidad del agua subterránea**

   En 2022 la red de agua subterránea estuvo constituida por 775 sitios. El análisis de calidad del agua para estos sitios considera 14 parámetros indicadores fisicoquímicos y microbiológicos: Fluoruros (Fluo), Coliformes fecales (CF), Nitrógeno de Nitratos (N_NO3), Arsénico Total (As_Tot), Cadmio Total (Cd_Tot), Cromo Total (Cr_Tot), Mercurio Total (Hg_Tot), Plomo Total (Pb_Tot), Alcalinidad (Alc_Tot), Conductividad eléctrica (Cond_elec), Dureza Total (Dur_Tot), Sólidos Disueltos Totales (SDT), Hierro Total (Fe_Tot) y Manganeso Total (Mn_Tot)). Con base en estos parámetros se califica el cumplimiento o el incumplimiento de la calidad del agua destinada para uso potable, de consumo o en riego agrícola.

   Asimismo, se estableció un semáforo de calidad del agua subterránea: verde cuando hay cumplimiento de los 14 parámetros indicadores. Amarillo cuando se incumple en uno o más de los siguientes parámetros: Alcalinidad total, Conductividad eléctrica, Dureza total, Sólidos Disueltos Totales, Hierro Total y Manganeso Total. Rojo cuando se incumple en uno o más de los siguientes parámetros: Fluoruros, Coliformes fecales, Nitrógeno de Nitratos, Arsénico Total, Cadmio Total, Cromo Total, Mercurio Total y Plomo Total. Con base en ello, en 2022 se calificaron en verde el 42.5% de los sitios, el 18.6% de los sitios en amarillo y el 39% de los sitios en rojo.

   Los datos puden ser descargados en formato de hoja de calculo y comprimidos:

   * Enlaces para el año 2022

     * [Hoja de calculo](https://files.conagua.gob.mx/conagua/generico/sequia/Calidad_del_Agua_Subterranea_a.xlsx)

       * Localización del archivo: /databases/conagua/data/Calidad_del_Agua_Subterranea_a.xlsx
       * Hash SHA256: f8c449099018ef7697d8ef9e13fba587e5c4e231b336df9af5e96416e520b662

     * [Archivo comprimido](https://files.conagua.gob.mx/conagua/generico/sequia/Calidad_del_Agua_Subterranea_a.zip)

       * Localización del archivo: /databases/conagua/data/Calidad_del_Agua_Subterranea_a.zip

       * Hash SHA256: 4be4f4f708db035db116b1bc3d80c104459aff2f0e7185f099f1ad500ae314c4

         

   * Enlaces para el periodo correspondiente al periodo 2012-2022

     * [Hoja de calculo](https://files.conagua.gob.mx/conagua/generico/sequia/Calidad_del_Agua_Subterranea_p.xlsx)
       * Localización del archivo: /databases/conagua/data/Calidad_del_Agua_Subterranea_p.xlsx
       * Hash SHA256: f6f7610b5477c8c475d75816857950b08bb046976b9ffd79a41db111a53b8ec
     * [Archivo comprimido](https://files.conagua.gob.mx/conagua/generico/sequia/Calidad_del_Agua_Subterranea_p.zip)
       * Localización del archivo: /databases/conagua/data/Calidad_del_Agua_Subterranea_p.zip
       * Hash SHA256: 61e48f01d21f067c859dc8c09c5502a8f5952d342e641358307411993f352803

   Los campos considerados en la descripción de la base de datos son los siguientes:

   | CLAVE                      | Clave del sitio de monitoreo                                 | Texto    | A - Z                                                        |
   | -------------------------- | ------------------------------------------------------------ | -------- | ------------------------------------------------------------ |
   | SITIO                      | Nombre del sitio de muestreo                                 | Texto    | A - Z                                                        |
   | ID_ORGANISMO_DE_CUENCA     | Identificador de Organismo de Cuenca                         | Numerico | Entero                                                       |
   | NOMBRE_ORGANISMO_DE_CUENCA | Nombre del Organismo de Cuenca de agua donde se localiza el sitio de monitoreo | Texto    | A - Z                                                        |
   | ID_ESTADO                  | Identificador de Estado                                      | Numerico | Entero                                                       |
   | NOMBRE_ESTADO              | Estado donde se encuentra el sitio de muestreo               | Texto    | A - Z                                                        |
   | ID_MUNICIPIO               | Identificador de Municipio                                   | Numerico | Entero                                                       |
   | NOMBRE_MUNICIPIO           | Municipio donde se encuentra el sitio de muestreo            | Texto    | A - Z                                                        |
   | ID_ACUIFERO                | Identificador de Acuífero                                    | Numerico | Entero                                                       |
   | ACUIFERO                   | Acu¡fero donde se encuentra el sitio de muestreo             | Texto    | A - Z                                                        |
   | SUBTIPO                    | Subtipo de cuerpo de agua donde se encuentra el sitio de muestreo | Texto    | A - Z                                                        |
   | LONGITUD                   | Coordenada de longitud                                       | Numerico | 6 decimales                                                  |
   | LATITUD                    | Coordenada de latitud                                        | Numerico | 6 decimales                                                  |
   | PERIODO                    | Año o periodo en que se realizo el muestreo                  | Texto    | 2012 - actual                                                |
   | ALC_mg/L                   | Valor de Alcalinidad Total, en miligramos por litro          | Texto    | 1 decimal, ND                                                |
   | AS_TOT_mg/L                | Valor de Arsenico Total, en miligramos por litro             | Texto    | 3 decimales, ND                                              |
   | CD_TOT_mg/L                | Valor de Cadmio Total, en miligramos por litro               | Texto    | 3 decimales, ND                                              |
   | COLI_FEC_NMP/100_mL        | Valor de Coliformes Fecales, en Numero Mas Probable por 100 mililitros | Texto    | 1 decimal, ND                                                |
   | CONDUCT_mS/cm              | Valor de Conductividad en microSiemens por centimetro        | Texto    | 1 decimal, ND                                                |
   | CR_TOT_mg/L                | Valor de Cromo Total, en miligramos por litro                | Texto    | 3 decimales, ND                                              |
   | DUR_mg/L                   | Valor de Dureza Total, en miligramos por litro               | Texto    | 1 decimal, ND                                                |
   | FE_TOT_mg/L                | Valor de Hierro Total, en miligramos por litro               | Texto    | 3 decimales, ND                                              |
   | FLUORUROS_mg/L             | Valor de Fluoruros Totales (F-), en miligramos por litro     | Texto    | 1 decimal, ND                                                |
   | HG_TOT_mg/L                | Valor de Mercurio Total, en miligramos por litro             | Texto    | 4 decimales, ND                                              |
   | MN_TOT_mg/L                | Valor de Manganeso Total, en miligramos por litro            | Texto    | 3 decimales, ND                                              |
   | N_NO3_mg/L                 | Valor de Nitrogeno de Nitratos, en miligramos por litro      | Texto    | 3 decimales, ND                                              |
   | PB_TOT_mg/L                | Valor de Plomo Total, en miligramos por litro                | Texto    | 3 decimales, ND                                              |
   | SDT_M_mg/L                 | Valor de Solidos Disueltos Totales-Medidos, en miligramos por litro | Texto    | 1 decimal, ND                                                |
   | SDT_mg/L                   | Valor de Solidos Disueltos Totales, en miligramos por litro  | Texto    | 1 decimal, ND                                                |
   | CALIDAD_ALC                | Clasificacion de la calidad del agua de acuerdo con el indicador Alcalinidad Total | Texto    | Baja, Media, Alta, Indeseable, Indeseable como fuente de abastecimiento |
   | CALIDAD_AS                 | Clasificacion de la calidad del agua de acuerdo con el indicador Arsenico Total | Texto    | Potable - Excelente, Apta como FAAP, No Apta como FAAP       |
   | CALIDAD_CD                 | Clasificacion de la calidad del agua de acuerdo con el indicador Cadmio Total | Texto    | Potable - Excelente, No apta como FAAP                       |
   | CALIDAD_COLI_FEC           | Clasificacion de la calidad del agua de acuerdo con el indicador Coliformes Fecales | Texto    | Potable - Excelente, Buena calidad, Aceptable, Contaminada, Fuertemente contaminada |
   | CALIDAD_CONDUC             | Clasificacion de la calidad del agua de acuerdo con el indicador Conductividad | Texto    | Excelente para riego, Buena para riego, Permisible para riego, Dudosa para riego, Indeseable para riego |
   | CALIDAD_CR                 | Clasificacion de la calidad del agua de acuerdo con el indicador Cromo Total | Texto    | Potable - Excelente, No apta como FAAP                       |
   | CALIDAD_DUR                | Clasificacion de la calidad del agua de acuerdo con el indicador Dureza Total | Texto    | Potable - Suave, Potable - Moderadamente suave, Potable - Dura, Muy dura e indeseable usos industrial y domestico |
   | CALIDAD_FE                 | Clasificacion de la calidad del agua de acuerdo con el indicador Hierro Total | Texto    | Potable - Excelente, Sin efectos en la salud - Puede dar color al agua |
   | CALIDAD_FLUO               | Clasificacion de la calidad del agua de acuerdo con el indicador Fluoruros Totales | Texto    | Baja, Media, Potable - Optima, Alta                          |
   | CALIDAD_HG                 | Clasificacion de la calidad del agua de acuerdo con el indicador Mercurio Total | Texto    | Potable - Excelente, No apta como FAAP                       |
   | CALIDAD_MN                 | Clasificacion de la calidad del agua de acuerdo con el indicador Manganeso Total | Texto    | Potable - Excelente, Sin efectos en la salud - Puede dar color al agua, Puede afectar la salud |
   | CALIDAD_N_NO3              | Clasificacion de la calidad del agua de acuerdo con el indicador Nitrogeno de Nitratos | Texto    | Potable - Excelente,  Potable - Buena calidad, No Apta como FAAP |
   | CALIDAD_PB                 | Clasificacion de la calidad del agua de acuerdo con el indicador Plomo Total | Texto    | Potable - Excelente, No apta como FAAP                       |
   | CALIDAD_SDT_ra             | Clasificacion de la calidad del agua de acuerdo con el indicador de los Solidos  Disueltos Totales (Riego agricola) | Texto    | Excelente para riego, Cultivos sensibles o Cultivos con manejo especial, Cultivos tolerantes, Indeseable para riego |
   | CALIDAD_SDT_salin          | Clasificacion de la calidad del agua de acuerdo con el indicador de los Solidos  Disueltos Totales (Salinizacion) | Texto    | Dulce, Ligeramente salobres, Salina, Salobre                 |
   | CUMPLE_CON_ALC             | Indica si cumple con la calidad de Baja, Media, o Alta para el Indicador Alcalinidad Total | Texto    | SI, NO, ND                                                   |
   | CUMPLE_CON_AS              | Indica si cumple con la calidad de Potable - Excelente o Apta como FAAP, para el Indicador Arsenico Total | Texto    | SI, NO, ND                                                   |
   | CUMPLE_CON_CD              | Indica si cumple con la calidad de Potable - Excelente, para el Indicador Cadmio Total | Texto    | SI, NO, ND                                                   |
   | CUMPLE_CON_CF              | Indica si cumple con la calidad de Potable - Excelente, o Buena calidad, Aceptable, para el Indicador Coliformes Fecales | Texto    | SI, NO, ND                                                   |
   | CUMPLE_CON_COND            | Indica si cumple con la calidad de Excelente para riego, Buena para riego, o Permisible para riego, para el Indicador Conductividad | Texto    | SI, NO, ND                                                   |
   | CUMPLE_CON_CR              | Indica si cumple con la calidad de Potable - Excelente, para el Indicador Cromo Total | Texto    | SI, NO, ND                                                   |
   | CUMPLE_CON_DUR             | Indica si cumple con la calidad de Potable - Suave, Potable - Moderadamente suave, o Potable - Dura, para el Indicador Dureza Total | Texto    | SI, NO, ND                                                   |
   | CUMPLE_CON_FE              | Indica si cumple con la calidad de Potable - Excelente, para el Indicador Hierro Total | Texto    | SI, NO, ND                                                   |
   | CUMPLE_CON_FLUO            | Indica si cumple con la calidad de Baja, Media, o Potable - Optima, para el Indicador Fluoruros Totales | Texto    | SI, NO, ND                                                   |
   | CUMPLE_CON_HG              | Indica si cumple con la calidad de Potable - Excelente, para el Indicador Mercurio Total | Texto    | SI, NO, ND                                                   |
   | CUMPLE_CON_MN              | Indica si cumple con la calidad de Potable - Excelente, para el Indicador Manganeso Total | Texto    | SI, NO, ND                                                   |
   | CUMPLE_CON_NO3             | Indica si cumple con la calidad de Potable - Excelente o Potable - Buena calidad, para el Indicador Nitrogeno de Nitratos | Texto    | SI, NO, ND                                                   |
   | CUMPLE_CON_PB              | Indica si cumple con la calidad de Potable - Excelente, para el Indicador Plomo Total | Texto    | SI, NO, ND                                                   |
   | CUMPLE_CON_SDT_ra          | Indica si cumple con la calidad de Excelente para riego, Cultivos sensibles o Cultivos con manejo especial, para el Indicador SDT (Riego agr¡cola) | Texto    | SI, NO, ND                                                   |
   | CUMPLE_CON_SDT_salin       | Indica si cumple con la calidad de Potable - Dulce  o Ligeramente salobres, para el Indicador Solidos Disueltos Totales (Salinizaci¢n) | Texto    | SI, NO, ND                                                   |
   | CONTAMINANTES              | Contaminantes  presentes en incumplimiento (Contaminados)    | Texto    | ALC, CONDUC, SDT_ra,SDT_salin, FLUO, DT, AS,NO3, DT, CF, NO3, AS, CD, CR, PB, MN, FE |
   | SEMAFORO                   | Indica el nivel de contaminacion de acuerdo a los contaminantes presentes | Texto    | Verde, Amarillo, Rojo                                        |

2. **Indicadores de la calidad del agua superficial a nivel nacional.**

   En 2022 la red de agua superficial estuvo constituida por 1,723 sitios. El análisis de la calidad del agua superficial consideró 8 parámetros indicadores: Demanda Bioquímica de Oxígeno a cinco días (DBO5), Demanda Química de Oxígeno (DQO), Sólidos Suspendidos Totales (SST), Coliformes fecales (CF), *Escherichia coli*, (E_COLI), Enterococos fecales (ENTEROC_FEC), porcentaje de saturación de Oxígeno Disuelto (OD%) y Toxicidad aguda (TOX). Con base en estos indicadores, se obtuvo una calificación de excelente para el 43.3% de los sitios con base en el parámetro DBO5; 23.4% con base en la DQO; 50.2% con SST; 17.5% con CF; 34.4% con E_COLI; 80.2% con ENTEROC_FEC y 43% con OD%. El 93.2% de los sitios no presentaron Toxicidad aguda.

   Asimismo, se utilizó el semáforo de calidad del agua superficial que considera 3 colores: verde, cuando hay cumplimiento de los 8 indicadores; amarillo cuando se incumple uno o más de los siguientes parámetros: E_COLI, CF, SST y OD%; rojo cuando existe incumplimiento en uno o más de los siguientes parámetros: DBO5, DQO, TOX y ENTEROC_FEC. De esta manera, el 26.1% de los sitios se calificaron en verde; el 45.2% de los sitios se calificaron en amarillo y el 28.7% de los sitios se calificaron en rojo.

   Los datos puden ser descargados en formato de hoja de calculo y comprimidos:

   * Enlaces para el año 2022
     * [Hoja de calculo](https://files.conagua.gob.mx/conagua/generico/sequia/Calidad_del_Agua_Superficial_a.xlsx)
       * Localización del archivo: /databases/conagua/data/Calidad_del_Agua_Superficial_a.xlsx
       * Hash SHA256: e66405e05cb1306f82442c1bed0339a69f12ecff6d1436af7e2166722417192e
     * [Archivo comprimido](https://files.conagua.gob.mx/conagua/generico/sequia/Calidad_del_Agua_Superficial_a.zip)
       * Localización del archivo: /databases/conagua/data/Calidad_del_Agua_Superficial_a.zip
       * Hash SHA256: 4472b81fcab315104efef0da0274b50fdebab0613495cd7eb0f1c31e72e23606
   * Enlaces para el periodo correspondiente al periodo 2012-2022
     * [Hoja de calculo](https://files.conagua.gob.mx/conagua/generico/sequia/Calidad_del_Agua_Superficial_p.xlsx)
       * Localización del archivo: /databases/conagua/data/Calidad_del_Agua_Superficial_p.xlsx
       * Hash SHA256: 2b9f74fbe2328915fdddbf127138100be3101493e24a9610b451a96973d987a
     * [Archivo comprimido](https://files.conagua.gob.mx/conagua/generico/sequia/Calidad_del_Agua_Superficial_p.zip)
       * Localización del archivo: /databases/conagua/data/Calidad_del_Agua_Superficial_p.zip
       * Hash SHA256: 94ef1f4fb92381244fda1897b5a0f84b321f72a51723cddd9bc6faf298a49a06

   Los campos considerados en la descripción de la base de datos son los siguientes:

   | **CAMPO**              | **DESCRIPCION**                                              | **TIPO** | **VALOR_POSIBLE**                                            |
   | ---------------------- | ------------------------------------------------------------ | -------- | ------------------------------------------------------------ |
   | CLAVE                  | Clave del sitio de monitoreo                                 | Texto    | A - Z                                                        |
   | SITIO                  | Nombre del sitio de muestreo                                 | Texto    | A - Z                                                        |
   | ID_ ORG_CUENCA         | Numero de identificacion del Organismo de Cuenca de agua donde se localiza el sitio de monitoreo | Numerico | Entero                                                       |
   | ORGANISMO_DE_CUENCA    | Nombre del Organismo de Cuenca de agua donde se localiza el sitio de monitoreo | Texto    | A - Z                                                        |
   | ID_ESTADO              | Numero de identificacion del Estado donde se encuentra el sitio de muestreo | Numerico | Entero                                                       |
   | ESTADO                 | Estado donde se encuentra el sitio de muestreo               | Texto    | A - Z                                                        |
   | MUNICIPIO              | Municipio donde se encuentra el sitio de muestreo            | Texto    | A - Z                                                        |
   | CUENCA                 | Nombre de la cuenca donde se localiza el sitio de monitoreo  | Texto    | A - Z                                                        |
   | CUERPO_DE_AGUA         | Nombre del cuerpo de agua donde se localiza el sitio de monitoreo | Texto    | A - Z                                                        |
   | TIPO                   | Tipo de cuerpo de agua donde se encuentra el sitio de muestreo | Texto    | A - Z                                                        |
   | SUBTIPO                | Subtipo de cuerpo de agua donde se encuentra el sitio de muestreo | Texto    | A - Z                                                        |
   | LONGITUD               | Coordenada de longitud                                       | Numerico | 6 decimales                                                  |
   | LATITUD                | Coordenada de latitud                                        | Numerico | 6 decimales                                                  |
   | PERIODO                | Año en que se realizo el muestreo                            | Texto    | 2012 - actual                                                |
   | CF_NMP100mL            | Valor de los Coliformes Fecales, en numero mas probable por cien mililitros | Texto    | 1 decimal, ND                                                |
   | DBO_mg/L               | Valor de la Demanda Bioquimica de Oxigeno, en miligramos por litro | Texto    | 1 decimal, ND                                                |
   | DQO_mg/L               | Valor de la Demanda Quimica de Oxigeno, en miligramos por litro | Texto    | 1 decimal, ND                                                |
   | E_COLI_NMP_100mL       | Valor de Escherichia coli, en numero mas probable por cien mililitros | Texto    | 1 decimal, ND                                                |
   | ENTEROC_NMP_100mL      | Valor de Enterococos fecales, en numero mas probable por cien mililitros | Texto    | 1 decimal, ND                                                |
   | OD_PORC                | Valor de Porcentaje de saturacion de oxigeno disuelto, en cuerpos loticos | Texto    | 1 decimal, ND                                                |
   | OD_PORC_FON            | Valor de Porcentaje de saturacion de oxigeno disuelto en fondo | Texto    | 1 decimal, ND                                                |
   | OD_PORC_MED            | Valor de Porcentaje de saturacion de oxigeno disuelto medio  | Texto    | 1 decimal, ND                                                |
   | OD_PORC_SUP            | Valor de Porcentaje de saturacion de oxigeno disuelto superficial | Texto    | 1 decimal, ND                                                |
   | SST_mg/L               | Valor de los Solidos Suspendidos Totales, en miligramos por litro | Texto    | 1 decimal, ND                                                |
   | TOX_D_48_FON_UT        | Valor de Toxicidad, Dafnia magna 48 horas, de fondo, Unidades de Toxicidad | Texto    | 1 decimal, ND                                                |
   | TOX_D_48_SUP_UT        | Valor de Toxicidad, Dafnia magna 48 horas, superficial, Unidades de Toxicidad | Texto    | 1 decimal, ND                                                |
   | TOX_D_48_UT            | Valor de Toxicidad, Dafnia magna, 48 horas, Unidades de Toxicidad, en cuerpos loticos | Texto    | 1 decimal, ND                                                |
   | TOX_FIS_FON_15_UT      | Valor de Toxicidad, Vibrio Fisheri, 15 minutos, en fondo, Unidades de Toxicidad | Texto    | 1 decimal, ND                                                |
   | TOX_FIS_SUP_15_UT      | Valor de Toxicidad, Vibrio Fisheri, 15 minutos, superficial, Unidades de Toxicidad | Texto    | 1 decimal, ND                                                |
   | TOX_V_15_UT            | Valor de Toxicidad, Vibrio Fisheri, 15 minutos, Unidades de Toxicidad, en cuerpos loticos | Texto    | 1 decimal, ND                                                |
   | CALIDAD_COLI_FEC       | Clasificacion de la calidad del agua de acuerdo con el indicador Coliformes Fecales | Texto    | Excelente, Buena calidad, Aceptable, Contaminada, Fuertemente contaminada |
   | CALIDAD_DBO            | Clasificacion de la calidad del agua de acuerdo con el indicador Demanda Bioquimica de Oxigeno | Texto    | Excelente, Buena calidad, Aceptable, Contaminada, Fuertemente contaminada |
   | CALIDAD_DQO            | Clasificacion de la calidad del agua de acuerdo con el indicador Demanda Quimica de Oxigeno | Texto    | Excelente, Buena calidad, Aceptable, Contaminada, Fuertemente contaminada |
   | CALIDAD_E_COLI         | Clasificacion de la calidad del agua de acuerdo con el indicador Escherichia coli | Texto    | Excelente, Buena calidad, Aceptable, Contaminada, Fuertemente contaminada |
   | CALIDAD_ENTEROC        | Clasificacion de la calidad del agua de acuerdo con el indicador Enterococos fecales | Texto    | Excelente, Buena calidad, Contaminada, Fuertemente contaminada |
   | CALIDAD_OD_PORC        | Clasificacion de la calidad del agua de acuerdo con el indicador Porcentaje de saturaci¢n de oxigeno disuelto | Texto    | Excelente, Buena calidad, Aceptable, Contaminada, Fuertemente contaminada |
   | CALIDAD_OD_PORC_FON    | Clasificacion de la calidad del agua de acuerdo con el indicador Porcentaje de saturacion de oxigeno disuelto, en fondo | Texto    | Excelente, Buena calidad, Aceptable, Contaminada, Fuertemente contaminada |
   | CALIDAD_OD_PORC_MED    | Clasificacion de la calidad del agua de acuerdo con el indicador Porcentaje de saturacion de oxigeno disuelto, medio | Texto    | Excelente, Buena calidad, Aceptable, Contaminada, Fuertemente contaminada |
   | CALIDAD_OD_PORC_SUP    | Clasificacion de la calidad del agua de acuerdo con el indicador Porcentaje de saturaci¢n de Oxigeno disuelto, superficial | Texto    | Excelente, Buena calidad, Aceptable, Contaminada, Fuertemente contaminada |
   | CALIDAD_SST            | Clasificacion de la calidad del agua de acuerdo con el indicador Solidos Suspendidos Totales | Texto    | Excelente, Buena calidad, Aceptable, Contaminada, Fuertemente contaminada |
   | CALIDAD_TOX_D_48       | Clasificacion de la calidad del agua de acuerdo con el indicador Toxicidad, Dafnia magna, 48 horas | Texto    | No toxico, Toxicidad baja, Toxicidad moderada, Toxicidad alta |
   | CALIDAD_TOX_D_48_FON   | Clasificacion de la calidad del agua de acuerdo con el indicador, Toxicidad, Dafnia magna 48 horas, en fondo | Texto    | No toxico, Toxicidad baja, Toxicidad moderada, Toxicidad alta |
   | CALIDAD_TOX_D_48_SUP   | Clasificacion de la calidad del agua de acuerdo con el indicador de Toxicidad, Dafnia magna 48 horas, superficial | Texto    | No toxico, Toxicidad baja, Toxicidad moderada, Toxicidad alta |
   | CALIDAD_TOX_FIS_FON_15 | Clasificacion de la calidad del agua de acuerdo con el indicador Toxicidad, Vibrio Fisheri, 15 minutos, en fondo | Texto    | No toxico, Toxicidad baja, Toxicidad moderada, Toxicidad alta |
   | CALIDAD_TOX_FIS_SUP_15 | Clasificacion de la calidad del agua de acuerdo con el indicador de Toxicidad, Vibrio Fisheri, 15 minutos, superficial | Texto    | No toxico, Toxicidad baja, Toxicidad moderada, Toxicidad alta |
   | CALIDAD_TOX_V_15       | Clasificacion de la calidad del agua de acuerdo con el indicador Toxicidad, Vibrio Fisheri, 15 minutos | Texto    | No toxico, Toxicidad baja, Toxicidad moderada, Toxicidad alta |
   | CUMPLE_CON_COLI_FEC    | Indica si cumple con la calidad de Excelente, Buena calidad o Aceptable, para el Indicador Coliformes Fecales | Texto    | SI, NO, ND                                                   |
   | CUMPLE_CON_DBO         | Indica si cumple con la calidad de Excelente, Buena calidad o Aceptable, para el Indicador Demanda Bioquimica de Oxigeno | Texto    | SI, NO, ND                                                   |
   | CUMPLE_CON_DQO         | Indica si cumple con la calidad de Excelente, Buena calidad o Aceptable, para el Indicador Demanda Quimica de Oxigeno | Texto    | SI, NO, ND                                                   |
   | CUMPLE_CON_E_COLI      | Indica si cumple con la calidad de Excelente, Buena calidad o Aceptable, para el Indicador Escherichia coli | Texto    | SI, NO, ND                                                   |
   | CUMPLE_CON_ENTEROC     | Indica si cumple con la calidad de Excelente o Buena calidad, para el Indicador Enterococos fecales | Texto    | SI, NO, ND                                                   |
   | CUMPLE_CON_OD          | Indica si cumple con la calidad de Excelente, Buena calidad o Aceptable, para el Indicador Porcentaje de saturaci¢n de Oxigeno disuelto | Texto    | SI, NO, ND                                                   |
   | CUMPLE_CON_SST         | Indica si cumple con la calidad de Excelente, Buena calidad o Aceptable, para el Indicador Solidos Suspendidos Totales | Texto    | SI, NO, ND                                                   |
   | CUMPLE_CON_TOX         | Indica si cumple con la calidad de No toxico, Toxicidad baja, o Toxicidad moderada, para el Indicador Toxicidad aguda | Texto    | SI, NO, ND                                                   |
   | CONTAMINANTES          | Contaminantes  presentes en incumplimiento (Contaminados)    | Texto    | DBO,DQO,SST,CF,E_COLI,ENT_FEC, OD%S,OD%M,OD%F,TOX_S,TOX_F, TOX_L |
   | SEMAFORO               | Indica el nivel de contaminacion de acuerdo a los contaminantes presentes | Texto    | Verde, Amarillo, Rojo                                        |
   | GRUPO                  | Grupo del cuerpo de agua                                     | Texto    | LOTICO, LENTICO, COSTERO                                     |
   | ND                     | No Disponible                                                |          |                                                              |