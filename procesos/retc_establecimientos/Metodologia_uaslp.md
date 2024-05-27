# Metodología para la generación de la base de datos de las emisoras de sustancias RETC

## Recolección de datos

Los datos fueron adquiridos desde la página del RETC

## Revisión de las columnas por archivo

Se descargaron los archivos del 2004 al 2022. Cada archivo contiene los detalles de las emisoras que reportaron emisiones al registro del RETC.

Se detecto que existen tres formatos diferentes en los archivos. Cada formato contiene diferente número de atributos (columnas) y en algunos casos un nombre distinto para el mismo atributo. A continuación se listan los atributos para cada formato:

1. Periodo de 16 años comprendido por los periodos de 2006 a 2011 (6 años) y de 2013 a 2022 (10 años)
2. Periodo de 2 años comprendido por los años 2004 y 2005
3. Periodo comprendido por los registros del año 2012

| Formato 1 (2006-2011 y 2013-2022) | Formato 2 (2004-2005)        | Formato 3 (2012)         |
| --------------------------------- | ---------------------------- | ------------------------ |
| Año                               | Año                          | Año                      |
| NRA                               | NRA                          | NRA                      |
| NOMBRE                            | Nombre                       | Establecimiento          |
| SCIAN                             |                              | Número SCIAN             |
| DESCRIPCIÓN SCIAN                 |                              | SCIAN                    |
| SECTOR                            | Sector                       | Sector                   |
| CLAVE AMBIENTAL                   |                              | Clave Ambiental          |
| SUBSECTOR                         |                              |                          |
| PRINCIPAL ACTIVIDAD PRODUCTIVA    | Actividad principal          | Actividad Principal      |
| PARQUE INDUSTRIAL                 | Parque o puerto industrial   | Nombre Parque Industrial |
| COORDENADA  UTM X                 | Coordenada UTM X             |                          |
| COORDENADA  UTM Y                 | Coordenada UTM Y             |                          |
| LATITUD  NORTE                    | Latitud Norte                | Latitud Norte            |
| LONGITUD  OESTE                   | Longitud Oeste               | Longitud Oeste           |
| CALLE                             | Calle                        | Calle                    |
| NÚM. EXT                          | No. Exterior                 | Número Exterior          |
| NÚM. INT                          | No. Interior                 | Número Interior          |
| COLONIA                           | Colonia                      | Colonia                  |
| LOCALIDAD                         | Localidad                    | Localidad                |
| ESTADO                            | Estado                       | Entidad Federativa       |
| MUNICIPIO                         | Delegación\Municipio         | Municipio                |
| C.P.                              | Código postal                | Código Postal            |
|                                   | Actividad principal SEMARNAT |                          |
|                                   |                              | Entre Calle 1            |
|                                   |                              | Entre Calle 2            |

Para mantener una consistencia en la base de datos, se opto por adicionar las columnas no consideradas en los formatos y colocar como valor por defecto "Atributo no considerado en este año". Adicionalmente se opto por realizar el cambio de nombres de los atributos para mantener una base de datos homogénea.

| Formato 1 (2006-2011 y 2013-2022) | Formato 2 (2004-2005) | Formato 3 (2012) |
| --------------------------------- | --------------------- | ---------------- |
| anio                              | anio                  | anio             |
| nra                               | nra                   | nra              |
| establecimiento                   | establecimiento       | establecimiento  |
| scian                             | **scian**             | scian            |
| descscian                         | **descscian**         | descscian        |
| sector                            | sector                | sector           |
| claveambiental                    | **claveambiental**    | claveambiental   |
| subsector                         | **subsector**         | **subsector**    |
| actprincipal                      | actprincipal          | actprincipal     |
| parqueindustrial                  | parqueindustrial      | parqueindustrial |
| utmx                              | utmx                  | **utmx**         |
| utmy                              | utmy                  | **utmy**         |
| latitudnorte                      | latitudnorte          | latitudnorte     |
| longitudoeste                     | longitudoeste         | longitudoeste    |
| calle                             | calle                 | calle            |
| numexterior                       | numexterior           | numexterior      |
| numinterior                       | numinterior           | numinterior      |
| colonia                           | colonia               | colonia          |
| localidad                         | localidad             | localidad        |
| estado                            | estado                | estado           |
| municipio                         | municipio             | municipio        |
| codigopostal                      | codigopostal          | codigopostal     |
| **actsemarnat**                   | actsemarnat           | **actsemarnat**  |
| **entrec1**                       | **entrec1**           | entrec1          |
| **entrec2**                       | **entrec2**           | entrec2          |

Se ordenan los nombres de las columnas para hacer una fusión más sencilla:

| Attributos ordenados |
| -------------------- |
| actprincipal         |
| actsemarnat          |
| anio                 |
| calle                |
| claveambiental       |
| codigopostal         |
| colonia              |
| descscian            |
| entrec1              |
| entrec2              |
| establecimiento      |
| estado               |
| latitudnorte         |
| localidad            |
| longitudoeste        |
| municipio            |
| nra                  |
| numexterior          |
| numinterior          |
| parqueindustrial     |
| scian                |
| sector               |
| subsector            |
| utmx                 |
| utmy                 |



## Proceso de preparación

A continuación se muestra la cantidad de emisoras (filas) registradas por archivo csv (año):

|    Año    | Cantidad de emisoras en el csv |
| :-------: | :----------------------------: |
|   2004    |              1714              |
|   2005    |              2452              |
|   2006    |              2734              |
|   2007    |              2445              |
|   2008    |              2463              |
|   2009    |              2341              |
|   2010    |              2599              |
|   2011    |              2765              |
|   2012    |              3160              |
|   2013    |              3589              |
|   2014    |              2236              |
|   2015    |              2526              |
|   2016    |              2569              |
|   2017    |              2660              |
|   2018    |              2852              |
|   2019    |              2943              |
|   2020    |              2909              |
|   2021    |              2934              |
|   2022    |              3017              |
| **Total** |           **50908**            |



Después de la integración, se cuenta con **50,908** establecimientos

### Resumen parcial de las emisoras

Como primera etapa de análisis se realiza un conteo de las apariciones de un Número de Registro Ambiental para cada año en el periodo comprendido desde el año 2004 al 2022. 

#### Detección de inconsistencias en el conteo de registros por año

Lo esperado es que una emisoras identificada por un NRA solo cuente con un registro por año. Al consultar la cantidad de registros de establecimientos se detectó que hay dos registros que no cumplen este comportamiento. A los registros que no cumplen con el comportamiento esperado se le considera como una inconsistencia del registro de datos. A continuación de listan los dos casos en los que se puede observar esta situación: 

| nra          | anio | cantidad_reportes |
| ------------ | ---- | ----------------- |
| DMOMA1900611 | 2018 | 2                 |
| MTM7X0803712 | 2018 | 2                 |



## Modificaciones a la base de datos

Con el objetivo de llevar un control de los cambios realizados sobre la base de datos inicial se agregaron dos nuevos atributos:

* **dbmod**: Indica si el operador de la base de datos realizó alguna modificación del contenido de la base de datos original.
* **dbdescmod**: Describe de manera breve el cambio realizado por el administrados de la base de datos.

Estos atributos permiten a los usuarios saber que parte del registro fue actualizado.

### Corrección en el contenido coordenadas en formato Grados, Minutos y segundos (DMS)

Las coordenadas de los establecimientos vienen en dos formtos:

1. Grados, Minutos y Segundos (DMS, por sus siglas en inglés)
2. Grados decimales (DD, por sus siglas en inglés)

Algunos de los programas utilizados para ubicar una posición en un mapa mediante la latitud y longitud requieren que el formato sea DD. Por esta razón se ejecuto una función que realiza la transformación de la latitud norte y la longitud oeste de formato DMS a formato DD.

### Errores en el contenido de las coordenadas DMS

Se realizó un análisis del contenido de los atributos latitud norte y longitud oeste se detectaron diversos errores de captura registrados los datos insertados en la base de datos. Estos errores están presentes desde los archivos descargados desde el SINAT de la Semarnat. A continuación se presenta un listado con algunas de las consistencias detectadas:

| Latitud       | Longitud      | Comentario                                                   |
| ------------- | ------------- | ------------------------------------------------------------ |
| 25º 42 46.97" | 100º 20 7.29" | Hace falta el símbolo de minutos '. NRA QUI5I1903911 2004    |
| 25º 42 46.97" | 100º 20 7.29" | Hace falta el símbolo de minutos '. 2007                     |
| 25º 42 46.97" | 100º 20 7.29" | Hace falta el símbolo de minutos '. 2008                     |
| 25º 42 46.97" | 100º 20 7.29" | Hace falta el símbolo de minutos '. 2009                     |
| 25º52'18.88"  | 100º'13'39.1" | Tenia el símbolo grado y minuto en juntos en la longitud oeste. Se removió el símbolo extra. IVP7X1901211 2006 |
| 25º52'18.88"  | 100º'13'39.1" | Se tiene el símbolo grado y minuto en juntos. 2007           |
| 25º52'18.88"  | 100º'13'39.1" | Se tiene el símbolo grado y minuto en juntos. IVP7X1901211 2008 |
| 25ª42'46.97"  | 100º20'07.29" | Tiene el símbolo ª en vez de grados. Se cambio por º RMW7N1901211 2006. |

Sin embargo, para que las transformaciones se realicen con éxito es necesario realizar la corrección de datos con errores detectados.

#### Búsqueda de inconsistencias.

Como ya se identificaron las inconsistencias, es necesario hacer consultas a la base de datos para que actualizar el valor de los registros con errores. A continuación se listan los parámetros de búsqueda utilizados para localizar los registros con errores en los atributos de latitud norte y longitud oeste.

```
#Filtro para obtener los registros de la primera excepción 
{nra:"QUI5I1903911", $and:[{anio:{$gte:2004}}, {anio:{$lt:2010}}]}
##Filtro para obtener los registros de la segunda excepción 
{nra:"IVP7X1901211", longitudoeste: /º'/}

##Filtro para obtener los registros de la tercera excepción 
{_id: ObjectId('65bec4d7675c397043f16772')}
{latitudnorte: /ª/}

```

#### Corrección de inconsistencias

Para modificar el contenido de la base de datos se utilizó la herramienta MongoDB Compass que, mediante una interfaz gráfica, permite filtrar y actualizar los datos. 

### Transformación de coordenadas en formato DMS a formato DD

Una vez corregidos los datos,  se realiza la trasformación de las coordenadas. Para trabajar con los datos fuera de línea, se obtiene un csv con los datos de las coordenadas. A continuación se muestra el filtro usado parra obtener solo los datos requeridos

#### Resultado de la transformación

El resumen de la transformación es el siguiente

| Descripción                                                  | Número de establecimientos detectados |
| ------------------------------------------------------------ | :------------------------------------ |
| Establecimientos con coordenadas en formato DD. No requiere transformación (ddformat) | 3697                                  |
| Establecimientos con coordenadas en formato DMS. Requiere transformación (dmsformat) | 46842                                 |
| Establecimientos con coordenadas en formato DMS pero que contenían un valor que no puede ser transformado (dmsdefault) | 369                                   |
| **Total**                                                    | **50908**                             |



#### Se genero la bd estab_2024_v5

### Modificaciones y cambios aplicados a los Estados y Municipios

El contenido de los estados y municipios registrados en la base de datos contienen diferentes formatos para un mismo valor, a continuación se listan algunos ejmplos: (Todo en mayúsculas, como nombre propio, sin acentos, con acentos, con abreviaturas, con espacios de más )

| Descripción del formato                                      | Ejemplo                                             |
| ------------------------------------------------------------ | --------------------------------------------------- |
| Todo el texto en mayúsculas                                  | AGUASCALIENTES                                      |
| Primer letra en mayúsculas                                   | Aguascalientes                                      |
| Valores sin acentos                                          | Juchitan de Zaragoza                                |
| Valores con el acento adecuado                               | Juchitán de Zaragoza                                |
| Un atributo es representado por dos diferentes valores       | Valor 1: Tlaltizapan Valor 2: Tlaltizapán de Zapata |
| Un atributo es presentado por un valor con abreviatura y otros sin las mismas. | Valor 1: Dr. Arroyo Valor 2: Doctor Arroyo          |

Con el objetivo de colocar todos los nombres de las entidades federativas y municipios se decidió realizar los siguientes procesos:

* Homogeneizar los nombres de las entidades federativas como nombres propios:

  | Nombre de las entidades federativas |
  | ----------------------------------- |
  | Aguascalientes                      |
  | Baja California                     |
  | Baja California Sur                 |
  | Campeche                            |
  | Coahuila de Zaragoza                |
  | Colima                              |
  | Chiapas                             |
  | Chihuahua                           |
  | Ciudad de México                    |
  | Durango                             |
  | Guanajuato                          |
  | Guerrero                            |
  | Hidalgo                             |
  | Jalisco                             |
  | México                              |
  | Michoacán de Ocampo                 |
  | Morelos                             |
  | Nayarit                             |
  | Nuevo León                          |
  | Oaxaca                              |
  | Puebla                              |
  | Querétaro                           |
  | Quintana Roo                        |
  | San Luis Potosí                     |
  | Sinaloa                             |
  | Sonora                              |
  | Tabasco                             |
  | Tamaulipas                          |
  | Tlaxcala                            |
  | Veracruz de Ignacio de la Llave     |
  | Yucatán                             |
  | Zacatecas                           |

* Actualizar los nombres de los municipios, agregando los acentos a los que lo requieren.
* Agregar la clave de entidad correspondiente a cada registro
* Agregar la clave de municipio correspondiente a cada registro

Para obtener y actualizar los datos de los estados y municipios se utilizó el contenido de la base de datos del DENUE.

#### Proceso para homogeneizar los nombres de los estados.

Actualmente se el nombre de los estados se encuentra estados en dos formatos (mayúsculas y minúsculas) en la base de datos. Se procede a homogeneizar el nombre de los estados. Con el objetivo de colocar todos los nombres de las entidades federativas, se decidió colocar los nombres de las mismas como nombres propios. 

#### Proceso para homogeneizar los nombres de los municipios.

Se genero un listado con todos los cambios que debían realizarse para colocar el nombre adecuado a los municipios.

* Se corrigió el nombre de los municipios
* Se agrego la clave de identidad para cada municipio.

#### Se genero la bd estab_2024_v6

Adicional a la corrección de los nombres de los Municipios y actualizar el nombre de algunos estados se agregaron los campos.

* cve_ent
* cve_mun

## Análisis del contenido de la base de datos del RETC



### Detección de NRA con distintos estados o municipios

Como resultado se obtuvo un listado con:

| NRA distintos registrados en la base de datos | 10021 |
| --------------------------------------------- | ----- |

Se genero un listado con todos los NRA con el estado y municipio que están registrados.

Se obtuvo un listado con **10156** NRA. En este listado cada uno de los NRA tiene el estado y el municipio al que corresponde.

Debido a que el NRA contiene los datos del estado y el municipio no es posible que un mismo NRA tenga datos correspondientes a otra ubicación. A continuación se muestran los NRA y la cantidad de Estado/Municipio registrados.

Como resultado se obtuvo un listado de 132 establecimientos (NRA) con más de un estado o municipio. A continuación se presenta el listado.

| NRA           | Cantidad de Estado o Municipios Distintos |
| ------------- | ----------------------------------------- |
| PEP100501812  | 3                                         |
| PEP100707417  | 3                                         |
| AME2604200008 | 3                                         |
| PEP10301311G  | 2                                         |
| AER5V1505111  | 2                                         |
| TGN192403711  | 2                                         |
| PREMH3019311  | 2                                         |
| WMP5Q2201111  | 2                                         |
| CDE8A0901611  | 2                                         |
| PEP102803218  | 2                                         |
| IJD8C0502711  | 2                                         |
| PASLX2700411  | 2                                         |
| EANEE1512111  | 2                                         |
| MOFK90400312  | 2                                         |
| NMEAE2601311  | 2                                         |
| MMA143205611  | 2                                         |
| PEP100706212  | 2                                         |
| CFEAD1001211  | 2                                         |
| UMEND1900611  | 2                                         |
| LTM5Y1512111  | 2                                         |
| DMC7T2903911  | 2                                         |
| PEP102700617  | 2                                         |
| MOFK90400314  | 2                                         |
| PMIUA3105011  | 2                                         |
| GOPAY2201611  | 2                                         |
| AUT1902600005 | 2                                         |
| CFEAD2601711  | 2                                         |
| PEP100501311  | 2                                         |
| SIT8A2902211  | 2                                         |
| DDM0400300043 | 2                                         |
| PGPM90803712  | 2                                         |
| CIC742300811  | 2                                         |
| PEP103013118  | 2                                         |
| DQU5W1512111  | 2                                         |
| CME5J1102811  | 2                                         |
| PEP100400211  | 2                                         |
| HNAMC1100511  | 2                                         |
| PEP2701400048 | 2                                         |
| NCS100400311  | 2                                         |
| PMETW0400311  | 2                                         |
| CME1X1104411  | 2                                         |
| OCI2700400001 | 2                                         |
| ZME5S1407011  | 2                                         |
| CFEAD2606111  | 2                                         |
| PREM91700611  | 2                                         |
| PREM91412011  | 2                                         |
| VRALJ1306911  | 2                                         |
| MTEKE0900211  | 2                                         |
| BMU2P0502211  | 2                                         |
| TIS7T2402811  | 2                                         |
| AARKE1901911  | 2                                         |
| RMCMB1512111  | 2                                         |
| OXA8A1505711  | 2                                         |
| GCMBJ300861E  | 2                                         |
| PEP10270082H  | 2                                         |
| PEP1027002AC  | 2                                         |
| PEP103002811  | 2                                         |
| SAMLJ0101111  | 2                                         |
| BMUBT0801911  | 2                                         |
| PAS9M2803211  | 2                                         |
| PREN83011514  | 2                                         |
| PEP103018112  | 2                                         |
| CRO691300312  | 2                                         |
| BMUB31903911  | 2                                         |
| PEP103013114  | 2                                         |
| CNL5E2201111  | 2                                         |
| TME9M2201411  | 2                                         |
| CFEAD1000714  | 2                                         |
| EDMK92700311  | 2                                         |
| PEP10270141K  | 2                                         |
| CME9I0502711  | 2                                         |
| MPAND1512111  | 2                                         |
| EMCZU1901211  | 2                                         |
| RBE8V0803716  | 2                                         |
| IPCMG3018911  | 2                                         |
| CMER30802011  | 2                                         |
| MISUA3003911  | 2                                         |
| GMB121001911  | 2                                         |
| PEP10280321N  | 2                                         |
| PRO361512111  | 2                                         |
| AEEBU0900712  | 2                                         |
| IPAMC3004411  | 2                                         |
| FAI9K0502711  | 2                                         |
| PEPM93017411  | 2                                         |
| APAKE1901911  | 2                                         |
| IMA7Q1512111  | 2                                         |
| TMEMD1900611  | 2                                         |
| CME2701400018 | 2                                         |
| GBW5Y0900711  | 2                                         |
| IDPBB1900911  | 2                                         |
| PRE671307612  | 2                                         |
| UME9M0100111  | 2                                         |
| PEP100400214  | 2                                         |
| GSP0400300053 | 2                                         |
| ANJ5P1409711  | 2                                         |
| BFO8L1512111  | 2                                         |
| BMS5T0900311  | 2                                         |
| CEIM03004811  | 2                                         |
| PEP102700612  | 2                                         |
| SMSLU2700411  | 2                                         |
| SFA521512111  | 2                                         |
| KOB7N1900111  | 2                                         |
| MEX9M1901211  | 2                                         |
| TME1F1512111  | 2                                         |
| PEA7J0900211  | 2                                         |
| MME5Q0502711  | 2                                         |
| PEP102700218  | 2                                         |
| P&GZU1512111  | 2                                         |
| LCM9L0900711  | 2                                         |
| CRY5K1104411  | 2                                         |
| DDM0400300024 | 2                                         |
| CIN6T0503011  | 2                                         |
| PYT7J0501011  | 2                                         |
| PFR5Q1512112  | 2                                         |
| IAI0500400004 | 2                                         |
| PEP102700818  | 2                                         |
| PREM93008511  | 2                                         |
| CCO7Q1512111  | 2                                         |
| FCH742800411  | 2                                         |
| CIT2M3010211  | 2                                         |
| EME7S1904611  | 2                                         |
| PEP3005400002 | 2                                         |
| PEPM92803811  | 2                                         |
| MAL231512111  | 2                                         |
| MAG5I0502311  | 2                                         |
| FMO9G1512111  | 2                                         |
| CFEAD2300521  | 2                                         |
| PEPR93002811  | 2                                         |
| PEP100704811  | 2                                         |
| PEP100400213  | 2                                         |
| FMA910100511  | 2                                         |
| BDM5T1512111  | 2                                         |

A continuación se obtuvieron el listado de NRA con las combinaciones detectadas. 



Con estos datos podemos resumir que:

| Combinaciones                     | Cantidad de NRA |
| --------------------------------- | --------------- |
| NRA con un Estado/Muniipio        | 7185            |
| NRA con más de un Estado/Muniipio | 2836            |
| **Total**                         | **10021**       |

A continuación se muestran los datos de los NRA con más de un estado. Como se puede observar existen establecimientos que no están en el estado que les corresponde, o que por error de captura se uso un NRA incorrecto.

| nra               | estado                              | municipio                    | posicion | total |
| ----------------- | ----------------------------------- | ---------------------------- | -------- | ----- |
| PEP100501812      | Coahuila de Zaragoza                | Zaragoza                     | 1        | 3     |
| PEP100501812      | Coahuila de Zaragoza                | Monclova                     | 2        | 3     |
| **PEP100501812**  | **Tamaulipas**                      | **Reynosa**                  | **3**    | **3** |
| PEP100707417      | Chiapas                             | Reforma                      | 1        | 3     |
| PEP100707417      | Chiapas                             | Juárez                       | 2        | 3     |
| PEP100707417      | Chiapas                             | Ostuacán                     | 3        | 3     |
| AME2604200008     | Sonora                              | Cajeme                       | 1        | 3     |
| **AME2604200008** | **Michoacán de Ocampo**             | **Copándaro**                | **2**    | **3** |
| AME2604200008     | Sonora                              | Navojoa                      | 3        | 3     |
| PEP10301311G      | Veracruz de Ignacio de la Llave     | Cerro Azul                   | 1        | 2     |
| PEP10301311G      | Veracruz de Ignacio de la Llave     | Poza Rica de Hidalgo         | 2        | 2     |
| AER5V1505111      | México                              | Toluca                       | 1        | 2     |
| AER5V1505111      | México                              | Lerma                        | 2        | 2     |
| **TGN192403711**  | **Veracruz de Ignacio de la Llave** | **Tantoyuca**                | **1**    | **2** |
| TGN192403711      | San Luis Potosí                     | Tamazunchale                 | 2        | 2     |
| PREMH3019311      | Veracruz de Ignacio de la Llave     | Medellín de Bravo            | 1        | 2     |
| PREMH3019311      | Veracruz de Ignacio de la Llave     | Veracruz                     | 2        | 2     |
| WMP5Q2201111      | Querétaro                           | Querétaro                    | 1        | 2     |
| WMP5Q2201111      | Querétaro                           | El Marqués                   | 2        | 2     |
| CDE8A0901611      | Ciudad de México                    | Venustiano Carranza          | 1        | 2     |
| CDE8A0901611      | Ciudad de México                    | Miguel Hidalgo               | 2        | 2     |
| PEP102803218      | Tamaulipas                          | Reynosa                      | 1        | 2     |
| PEP102803218      | Tamaulipas                          | Miguel Alemán                | 2        | 2     |
| IJD8C0502711      | Coahuila de Zaragoza                | Ramos Arizpe                 | 1        | 2     |
| IJD8C0502711      | Nuevo León                          | Los Herreras                 | 2        | 2     |
| PASLX2700411      | Tabasco                             | Jalpa de Méndez              | 1        | 2     |
| PASLX2700411      | Tabasco                             | Centro                       | 2        | 2     |
| EANEE1512111      | México                              | Cuautitlán Izcalli           | 1        | 2     |
| EANEE1512111      | México                              | Cuautitlán                   | 2        | 2     |
| MOFK90400312      | Campeche                            | Carmen                       | 1        | 2     |
| MOFK90400312      | Campeche                            | Campeche                     | 2        | 2     |
| NMEAE2601311      | Sonora                              | Hermosillo                   | 1        | 2     |
| NMEAE2601311      | Sonora                              | Banámichi                    | 2        | 2     |
| MMA143205611      | Zacatecas                           | Morelos                      | 1        | 2     |
| MMA143205611      | Zacatecas                           | Zacatecas                    | 2        | 2     |
| PEP100706212      | Chiapas                             | Ostuacán                     | 1        | 2     |
| PEP100706212      | Chiapas                             | Pichucalco                   | 2        | 2     |
| CFEAD1001211      | Durango                             | Durango                      | 1        | 2     |
| CFEAD1001211      | Durango                             | Lerdo                        | 2        | 2     |
| UMEND1900611      | Nuevo León                          | Apodaca                      | 1        | 2     |
| UMEND1900611      | Nuevo León                          | Aramberri                    | 2        | 2     |
| LTM5Y1512111      | México                              | Cuautitlán Izcalli           | 1        | 2     |
| LTM5Y1512111      | México                              | Cuautitlán                   | 2        | 2     |
| DMC7T2903911      | Tlaxcala                            | Xaloztoc                     | 1        | 2     |
| DMC7T2903911      | Tlaxcala                            | Apizaco                      | 2        | 2     |
| PEP102700617      | Tabasco                             | Cunduacán                    | 1        | 2     |
| PEP102700617      | Tabasco                             | Centro                       | 2        | 2     |
| MOFK90400314      | Campeche                            | Campeche                     | 1        | 2     |
| MOFK90400314      | Campeche                            | Carmen                       | 2        | 2     |
| PMIUA3105011      | Yucatán                             | Progreso                     | 1        | 2     |
| PMIUA3105011      | Yucatán                             | Mérida                       | 2        | 2     |
| GOPAY2201611      | Querétaro                           | San Juan del Río             | 1        | 2     |
| GOPAY2201611      | Querétaro                           | Querétaro                    | 2        | 2     |
| AUT1902600005     | Nuevo León                          | Guadalupe                    | 1        | 2     |
| AUT1902600005     | Nuevo León                          | Monterrey                    | 2        | 2     |
| CFEAD2601711      | Sonora                              | Pitiquito                    | 1        | 2     |
| CFEAD2601711      | Sonora                              | Caborca                      | 2        | 2     |
| PEP100501311      | Tamaulipas                          | Reynosa                      | 1        | 2     |
| **PEP100501311**  | **Coahuila de Zaragoza**            | **Hidalgo**                  | **2**    | **2** |
| SIT8A2902211      | Tlaxcala                            | Teolocholco                  | 1        | 2     |
| SIT8A2902211      | Tlaxcala                            | Acuamanala de Miguel Hidalgo | 2        | 2     |
| DDM0400300043     | Tabasco                             | Centla                       | 1        | 2     |
| **DDM0400300043** | **Campeche**                        | **Carmen**                   | **2**    | **2** |
| PGPM90803712      | Chihuahua                           | Chihuahua                    | 1        | 2     |
| PGPM90803712      | Chihuahua                           | Juárez                       | 2        | 2     |
| CIC742300811      | Quintana Roo                        | Cozumel                      | 1        | 2     |
| CIC742300811      | Quintana Roo                        | Solidaridad                  | 2        | 2     |
| PEP103013118      | Veracruz de Ignacio de la Llave     | Poza Rica de Hidalgo         | 1        | 2     |
| PEP103013118      | Veracruz de Ignacio de la Llave     | Cerro Azul                   | 2        | 2     |
| DQU5W1512111      | México                              | Cuautitlán                   | 1        | 2     |
| DQU5W1512111      | México                              | Cuautitlán Izcalli           | 2        | 2     |
| CME5J1102811      | Guanajuato                          | Salvatierra                  | 1        | 2     |
| CME5J1102811      | Guanajuato                          | Guanajuato                   | 2        | 2     |
| PEP100400211      | Campeche                            | Carmen                       | 1        | 2     |
| PEP100400211      | Campeche                            | Campeche                     | 2        | 2     |
| HNAMC1100511      | Guanajuato                          | Apaseo el Grande             | 1        | 2     |
| HNAMC1100511      | Guanajuato                          | Celaya                       | 2        | 2     |
| PEP2701400048     | Tabasco                             | Paraíso                      | 1        | 2     |
| **PEP2701400048** | **Ciudad de México**                | **Benito Juárez**            | **2**    | **2** |
| NCS100400311      | Veracruz de Ignacio de la Llave     | Tuxpan                       | 1        | 2     |
| **NCS100400311**  | **Campeche**                        | **Carmen**                   | **2**    | **2** |
| PMETW0400311      | Campeche                            | Campeche                     | 1        | 2     |
| PMETW0400311      | Campeche                            | Carmen                       | 2        | 2     |
| CME1X1104411      | Guanajuato                          | Celaya                       | 1        | 2     |
| CME1X1104411      | Guanajuato                          | Villagrán                    | 2        | 2     |
| OCI2700400001     | Tabasco                             | Centla                       | 1        | 2     |
| OCI2700400001     | Tabasco                             | Centro                       | 2        | 2     |
| ZME5S1407011      | Jalisco                             | El Salto                     | 1        | 2     |
| ZME5S1407011      | Jalisco                             | Tlajomulco de Zúñiga         | 2        | 2     |
| CFEAD2606111      | Sonora                              | Hermosillo                   | 1        | 2     |
| CFEAD2606111      | Sonora                              | Soyopa                       | 2        | 2     |
| PREM91700611      | Morelos                             | Ayala                        | 1        | 2     |
| PREM91700611      | Morelos                             | Cuautla                      | 2        | 2     |
| PREM91412011      | Jalisco                             | Zapopan                      | 1        | 2     |
| PREM91412011      | Jalisco                             | El Salto                     | 2        | 2     |
| VRALJ1306911      | Hidalgo                             | Pachuca de Soto              | 1        | 2     |
| VRALJ1306911      | Hidalgo                             | Tizayuca                     | 2        | 2     |
| MTEKE0900211      | Ciudad de México                    | Azcapotzalco                 | 1        | 2     |
| MTEKE0900211      | Ciudad de México                    | Gustavo A. Madero            | 2        | 2     |
| BMU2P0502211      | Coahuila de Zaragoza                | Nava                         | 1        | 2     |
| BMU2P0502211      | Coahuila de Zaragoza                | Piedras Negras               | 2        | 2     |
| TIS7T2402811      | San Luis Potosí                     | Villa de Reyes               | 1        | 2     |
| TIS7T2402811      | San Luis Potosí                     | San Luis Potosí              | 2        | 2     |
| AARKE1901911      | Nuevo León                          | Monterrey                    | 1        | 2     |
| AARKE1901911      | Nuevo León                          | San Pedro Garza García       | 2        | 2     |
| RMCMB1512111      | México                              | Cuautitlán                   | 1        | 2     |
| RMCMB1512111      | México                              | Cuautitlán Izcalli           | 2        | 2     |
| OXA8A1505711      | México                              | Tlalnepantla de Baz          | 1        | 2     |
| OXA8A1505711      | México                              | Naucalpan de Juárez          | 2        | 2     |
| GCMBJ300861E      | Veracruz de Ignacio de la Llave     | Xalapa                       | 1        | 2     |
| GCMBJ300861E      | Veracruz de Ignacio de la Llave     | Jalacingo                    | 2        | 2     |
| PEP10270082H      | Tabasco                             | Cárdenas                     | 1        | 2     |
| PEP10270082H      | Tabasco                             | Huimanguillo                 | 2        | 2     |
| PEP1027002AC      | Tabasco                             | Cárdenas                     | 1        | 2     |
| PEP1027002AC      | Tabasco                             | Huimanguillo                 | 2        | 2     |
| PEP103002811      | Veracruz de Ignacio de la Llave     | Veracruz                     | 1        | 2     |
| PEP103002811      | Veracruz de Ignacio de la Llave     | Boca del Río                 | 2        | 2     |
| SAMLJ0101111      | Aguascalientes                      | San Francisco de los Romo    | 1        | 2     |
| SAMLJ0101111      | Aguascalientes                      | Aguascalientes               | 2        | 2     |
| BMUBT0801911      | Jalisco                             | Bolaños                      | 1        | 2     |
| **BMUBT0801911**  | **Chihuahua**                       | **Chihuahua**                | **2**    | **2** |
| PAS9M2803211      | Tamaulipas                          | Reynosa                      | 1        | 2     |
| PAS9M2803211      | Tamaulipas                          | Matamoros                    | 2        | 2     |
| PREN83011514      | Veracruz de Ignacio de la Llave     | Nogales                      | 1        | 2     |
| PREN83011514      | Veracruz de Ignacio de la Llave     | Xalapa                       | 2        | 2     |
| PEP103018112      | Veracruz de Ignacio de la Llave     | Veracruz                     | 1        | 2     |
| PEP103018112      | Veracruz de Ignacio de la Llave     | Boca del Río                 | 2        | 2     |
| CRO691300312      | Hidalgo                             | Actopan                      | 1        | 2     |
| **CRO691300312**  | **Ciudad de México**                | **Coyoacán**                 | **2**    | **2** |
| BMUB31903911      | Nuevo León                          | Monterrey                    | 1        | 2     |
| **BMUB31903911**  | **Jalisco**                         | **Guadalajara**              | **2**    | **2** |
| PEP103013114      | Veracruz de Ignacio de la Llave     | Veracruz                     | 1        | 2     |
| PEP103013114      | Veracruz de Ignacio de la Llave     | Boca del Río                 | 2        | 2     |
| CNL5E2201111      | Querétaro                           | El Marqués                   | 1        | 2     |
| CNL5E2201111      | Querétaro                           | Querétaro                    | 2        | 2     |
| TME9M2201411      | Querétaro                           | San Joaquín                  | 1        | 2     |
| TME9M2201411      | Querétaro                           | Querétaro                    | 2        | 2     |
| CFEAD1000714      | Durango                             | Durango                      | 1        | 2     |
| CFEAD1000714      | Durango                             | Gómez Palacio                | 2        | 2     |
| EDMK92700311      | Campeche                            | Carmen                       | 1        | 2     |
| **EDMK92700311**  | **Tabasco**                         | **Centla**                   | **2**    | **2** |
| PEP10270141K      | Campeche                            | Carmen                       | 1        | 2     |
| **PEP10270141K**  | **Tabasco**                         | **Paraíso**                  | **2**    | **2** |
| CME9I0502711      | Coahuila de Zaragoza                | Ramos Arizpe                 | 1        | 2     |
| CME9I0502711      | Coahuila de Zaragoza                | Saltillo                     | 2        | 2     |
| MPAND1512111      | México                              | Cuautitlán Izcalli           | 1        | 2     |
| MPAND1512111      | México                              | Cuautitlán                   | 2        | 2     |
| EMCZU1901211      | Nuevo León                          | Ciénega de Flores            | 1        | 2     |
| EMCZU1901211      | Nuevo León                          | Monterrey                    | 2        | 2     |
| RBE8V0803716      | Chihuahua                           | Chihuahua                    | 1        | 2     |
| RBE8V0803716      | Chihuahua                           | Juárez                       | 2        | 2     |
| IPCMG3018911      | Veracruz de Ignacio de la Llave     | Tuxpan                       | 1        | 2     |
| **IPCMG3018911**  | **Campeche**                        | **Carmen**                   | **2**    | **2** |
| CMER30802011      | Chihuahua                           | Chínipas                     | 1        | 2     |
| CMER30802011      | Chihuahua                           | Chihuahua                    | 2        | 2     |
| MISUA3003911      | Veracruz de Ignacio de la Llave     | Agua Dulce                   | 1        | 2     |
| MISUA3003911      | Veracruz de Ignacio de la Llave     | Coatzacoalcos                | 2        | 2     |
| GMB121001911      | Durango                             | Otáez                        | 1        | 2     |
| GMB121001911      | Durango                             | Durango                      | 2        | 2     |
| PEP10280321N      | Tamaulipas                          | Mier                         | 1        | 2     |
| PEP10280321N      | Tamaulipas                          | Reynosa                      | 2        | 2     |
| PRO361512111      | México                              | Cuautitlán                   | 1        | 2     |
| PRO361512111      | México                              | Cuautitlán Izcalli           | 2        | 2     |
| AEEBU0900712      | Ciudad de México                    | Gustavo A. Madero            | 1        | 2     |
| AEEBU0900712      | Ciudad de México                    | Iztapalapa                   | 2        | 2     |
| IPAMC3004411      | Veracruz de Ignacio de la Llave     | Córdoba                      | 1        | 2     |
| IPAMC3004411      | Veracruz de Ignacio de la Llave     | Veracruz                     | 2        | 2     |
| FAI9K0502711      | Coahuila de Zaragoza                | Saltillo                     | 1        | 2     |
| FAI9K0502711      | Coahuila de Zaragoza                | Ramos Arizpe                 | 2        | 2     |
| PEPM93017411      | Veracruz de Ignacio de la Llave     | Tierra Blanca                | 1        | 2     |
| PEPM93017411      | Veracruz de Ignacio de la Llave     | Boca del Río                 | 2        | 2     |
| APAKE1901911      | Nuevo León                          | García                       | 1        | 2     |
| APAKE1901911      | Nuevo León                          | San Pedro Garza García       | 2        | 2     |
| IMA7Q1512111      | México                              | Cuautitlán                   | 1        | 2     |
| IMA7Q1512111      | México                              | Cuautitlán Izcalli           | 2        | 2     |
| TMEMD1900611      | Nuevo León                          | Aramberri                    | 1        | 2     |
| TMEMD1900611      | Nuevo León                          | Apodaca                      | 2        | 2     |
| CME2701400018     | Tabasco                             | Paraíso                      | 1        | 2     |
| CME2701400018     | Campeche                            | Carmen                       | 2        | 2     |
| GBW5Y0900711      | Ciudad de México                    | Iztapalapa                   | 1        | 2     |
| GBW5Y0900711      | Ciudad de México                    | Gustavo A. Madero            | 2        | 2     |
| IDPBB1900911      | Nuevo León                          | Monterrey                    | 1        | 2     |
| IDPBB1900911      | Nuevo León                          | Cadereyta Jiménez            | 2        | 2     |
| PRE671307612      | Hidalgo                             | Atitalaquia                  | 1        | 2     |
| PRE671307612      | Hidalgo                             | Tula de Allende              | 2        | 2     |
| UME9M0100111      | Aguascalientes                      | San Francisco de los Romo    | 1        | 2     |
| UME9M0100111      | Aguascalientes                      | Aguascalientes               | 2        | 2     |
| PEP100400214      | Campeche                            | Campeche                     | 1        | 2     |
| PEP100400214      | Campeche                            | Carmen                       | 2        | 2     |
| GSP0400300053     | Campeche                            | Carmen                       | 1        | 2     |
| GSP0400300053     | Campeche                            | Champotón                    | 2        | 2     |
| ANJ5P1409711      | Jalisco                             | San Pedro Tlaquepaque        | 1        | 2     |
| ANJ5P1409711      | Jalisco                             | Tlajomulco de Zúñiga         | 2        | 2     |
| BFO8L1512111      | México                              | Cuautitlán Izcalli           | 1        | 2     |
| BFO8L1512111      | México                              | Cuautitlán                   | 2        | 2     |
| BMS5T0900311      | Ciudad de México                    | Benito Juárez                | 1        | 2     |
| BMS5T0900311      | Ciudad de México                    | Coyoacán                     | 2        | 2     |
| CEIM03004811      | Veracruz de Ignacio de la Llave     | Cosoleacaque                 | 1        | 2     |
| CEIM03004811      | Veracruz de Ignacio de la Llave     | Coatzacoalcos                | 2        | 2     |
| PEP102700612      | Tabasco                             | Centro                       | 1        | 2     |
| PEP102700612      | Tabasco                             | Cunduacán                    | 2        | 2     |
| SMSLU2700411      | Tabasco                             | Centro                       | 1        | 2     |
| SMSLU2700411      | Tabasco                             | Paraíso                      | 2        | 2     |
| SFA521512111      | México                              | Cuautitlán                   | 1        | 2     |
| SFA521512111      | México                              | Cuautitlán Izcalli           | 2        | 2     |
| KOB7N1900111      | Nuevo León                          | Apodaca                      | 1        | 2     |
| KOB7N1900111      | Nuevo León                          | Abasolo                      | 2        | 2     |
| MEX9M1901211      | Nuevo León                          | Ciénega de Flores            | 1        | 2     |
| MEX9M1901211      | Nuevo León                          | Monterrey                    | 2        | 2     |
| TME1F1512111      | México                              | Cuautitlán Izcalli           | 1        | 2     |
| TME1F1512111      | México                              | Cuautitlán                   | 2        | 2     |
| PEA7J0900211      | Ciudad de México                    | Gustavo A. Madero            | 1        | 2     |
| PEA7J0900211      | Ciudad de México                    | Azcapotzalco                 | 2        | 2     |
| MME5Q0502711      | Coahuila de Zaragoza                | Ramos Arizpe                 | 1        | 2     |
| MME5Q0502711      | Coahuila de Zaragoza                | Saltillo                     | 2        | 2     |
| PEP102700218      | Tabasco                             | Huimanguillo                 | 1        | 2     |
| PEP102700218      | Tabasco                             | Cárdenas                     | 2        | 2     |
| P&GZU1512111      | México                              | Cuautitlán Izcalli           | 1        | 2     |
| P&GZU1512111      | México                              | Cuautitlán                   | 2        | 2     |
| LCM9L0900711      | Ciudad de México                    | Azcapotzalco                 | 1        | 2     |
| LCM9L0900711      | Ciudad de México                    | Iztapalapa                   | 2        | 2     |
| CRY5K1104411      | Guanajuato                          | Celaya                       | 1        | 2     |
| CRY5K1104411      | Guanajuato                          | Villagrán                    | 2        | 2     |
| DDM0400300024     | Tabasco                             | Paraíso                      | 1        | 2     |
| **DDM0400300024** | **Campeche**                        | **Carmen**                   | **2**    | **2** |
| CIN6T0503011      | Coahuila de Zaragoza                | Ramos Arizpe                 | 1        | 2     |
| CIN6T0503011      | Coahuila de Zaragoza                | Saltillo                     | 2        | 2     |
| PYT7J0501011      | Coahuila de Zaragoza                | Frontera                     | 1        | 2     |
| PYT7J0501011      | Coahuila de Zaragoza                | Monclova                     | 2        | 2     |
| PFR5Q1512112      | México                              | Cuautitlán                   | 1        | 2     |
| PFR5Q1512112      | México                              | Cuautitlán Izcalli           | 2        | 2     |
| IAI0500400004     | Coahuila de Zaragoza                | Saltillo                     | 1        | 2     |
| IAI0500400004     | Coahuila de Zaragoza                | Arteaga                      | 2        | 2     |
| PEP102700818      | Tabasco                             | Centro                       | 1        | 2     |
| PEP102700818      | Tabasco                             | Huimanguillo                 | 2        | 2     |
| PREM93008511      | Veracruz de Ignacio de la Llave     | Orizaba                      | 1        | 2     |
| PREM93008511      | Veracruz de Ignacio de la Llave     | Ixtaczoquitlán               | 2        | 2     |
| CCO7Q1512111      | México                              | Cuautitlán                   | 1        | 2     |
| CCO7Q1512111      | México                              | Cuautitlán Izcalli           | 2        | 2     |
| FCH742800411      | Tamaulipas                          | El Mante                     | 1        | 2     |
| FCH742800411      | Tamaulipas                          | Antiguo Morelos              | 2        | 2     |
| CIT2M3010211      | Veracruz de Ignacio de la Llave     | Martínez de la Torre         | 1        | 2     |
| CIT2M3010211      | Veracruz de Ignacio de la Llave     | San Rafael                   | 2        | 2     |
| EME7S1904611      | Nuevo León                          | San Nicolás de los Garza     | 1        | 2     |
| EME7S1904611      | Nuevo León                          | Monterrey                    | 2        | 2     |
| PEP3005400002     | Veracruz de Ignacio de la Llave     | Boca del Río                 | 1        | 2     |
| PEP3005400002     | Veracruz de Ignacio de la Llave     | Chacaltianguis               | 2        | 2     |
| PEPM92803811      | Tamaulipas                          | Tampico                      | 1        | 2     |
| PEPM92803811      | Tamaulipas                          | Reynosa                      | 2        | 2     |
| MAL231512111      | México                              | Cuautitlán Izcalli           | 1        | 2     |
| MAL231512111      | México                              | Cuautitlán                   | 2        | 2     |
| MAG5I0502311      | Coahuila de Zaragoza                | Torreón                      | 1        | 2     |
| MAG5I0502311      | Coahuila de Zaragoza                | Ocampo                       | 2        | 2     |
| FMO9G1512111      | México                              | Cuautitlán                   | 1        | 2     |
| FMO9G1512111      | México                              | Cuautitlán Izcalli           | 2        | 2     |
| CFEAD2300521      | Campeche                            | Carmen                       | 1        | 2     |
| **CFEAD2300521**  | **Quintana Roo**                    | **Benito Juárez**            | **2**    | **2** |
| PEPR93002811      | Veracruz de Ignacio de la Llave     | Veracruz                     | 1        | 2     |
| PEPR93002811      | Veracruz de Ignacio de la Llave     | Boca del Río                 | 2        | 2     |
| PEP100704811      | Chiapas                             | Reforma                      | 1        | 2     |
| PEP100704811      | Chiapas                             | Juárez                       | 2        | 2     |
| PEP100400213      | Campeche                            | Carmen                       | 1        | 2     |
| PEP100400213      | Campeche                            | Campeche                     | 2        | 2     |
| FMA910100511      | Aguascalientes                      | Jesús María                  | 1        | 2     |
| FMA910100511      | Aguascalientes                      | Aguascalientes               | 2        | 2     |
| BDM5T1512111      | México                              | Cuautitlán Izcalli           | 1        | 2     |
| BDM5T1512111      | México                              | Cuautitlán                   | 2        | 2     |
