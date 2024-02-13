# Metodología para la generación de la base de datos de las emisoras de sustancias RETC

## Recolección de datos

Los datos fueron adquiridos desde la página del RETC

## Revisión de las columnas por archivo

Se descargaron los archivos del 2004 al 2023. Cada archivo contiene los detalles de las emisoras que reportaron emisiones al registro del RETC.

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

```
2012
Index(['actprincipal', 'actsemarnat', 'anio', 'calle', 'claveambiental',
       'codigopostal', 'colonia', 'descscian', 'entrec1', 'entrec2',
       'establecimiento', 'estado', 'latitudnorte', 'localidad',
       'longitudoeste', 'municipio', 'nra', 'numexterior', 'numinterior',
       'parqueindustrial', 'scian', 'sector', 'subsector', 'utmx', 'utmy'],
      dtype='object')
2004-2005
Index(['actprincipal', 'actsemarnat', 'anio', 'calle', 'claveambiental',
       'codigopostal', 'colonia', 'descscian', 'entrec1', 'entrec2',
       'establecimiento', 'estado', 'latitudnorte', 'localidad',
       'longitudoeste', 'municipio', 'nra', 'numexterior', 'numinterior',
       'parqueindustrial', 'scian', 'sector', 'subsector', 'utmx', 'utmy'],
      dtype='object')
Index(['actprincipal', 'actsemarnat', 'anio', 'calle', 'claveambiental',
       'codigopostal', 'colonia', 'descscian', 'entrec1', 'entrec2',
       'establecimiento', 'estado', 'latitudnorte', 'localidad',
       'longitudoeste', 'municipio', 'nra', 'numexterior', 'numinterior',
       'parqueindustrial', 'scian', 'sector', 'subsector', 'utmx', 'utmy'],
      dtype='object')
2006-2011 y 2013-2022



```

## Proceso de preparación

A continuación se describen los procesos realizados para preparar los datos antes de insertarlos en la base de datos

### Inserción de columnas y ordenamiento de las mismas

Se creo un script en lenguaje Python para atender los requerimientos de cada formato. Se agregaron las columnas pendientes para cada formato y se realizó un ordenamiento por nombre de los atributos para facilitar el proceso de integración. Cada script genera los archivos csv para los años que les corresponden. A continuación se muestran los comandos utilizados:

```bash
#Periodo 2006-2011 y 2013-2023
python3 preparacion_formato1.py
#Periodo 2004-2005
python3 preparacion_formato2.py
#Para el año 2012
python3 preparacion_formato3.py

#Los archivos csv fueron almacenados en out_preparacion/
```



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

### Integración de los datos en un solo csv

```
python3 preparacion_append.py
Las salidas fue guardada en out_append/
```

Después de la integración, se cuenta con **50,908** establecimientos

## Base de datos original

A continuación se procede a realizar la inserción de los registros de los establecimientos en la base de datos. 

### Proceso de inserción

Para insertar los registros integrados de todas las emisoras del periodo 2004-2022 es necesario ejecutar el siguiente comando:

```bash
#Script responsable de leer el archivo integrado, convertir el DataFrame en un diccionario, agregar las columnas faltantes, reemplazar los espacios vacios (NaN) por "" para evitar conflictos
python3 db_insertar_emisoras_final.py
#
```

Este script depende de que exista una base de datos mongo configurada y que los parámetros de configuración sean colocados en el archivo **dbCon.py**.  Como resultado se crea una colección llamada "estab_2024_v4" en la base de datos de mongo que contiene todos los establecimientos.

### Resumen parcial de las emisoras

Como primera etapa de análisis se realiza un conteo de las apariciones de un Número de Registro Ambiental para cada año en el periodo comprendido desde el año 2004 al 2022.  A continuación se muestra el filtro utilizado para generar el archivo *csv* con los NRA y su respectivo conteo.

```sql
[
  {
    $group:
      {
        _id: {
          nra: "$nra",
          anio: "$anio",
        },
        reportes: {
          $sum: 1,
        },
      },
  },
  {
    $project:
      {
        _id: 0,
        nra: "$_id.nra",
        anio: "$_id.anio",
        cantidad_reportes: "$reportes",
      },
  },
  {
    $sort:
      {
        nra: 1,
        anio: 1,
      },
  },
]
```

#### Detección de inconsistencias en el conteo de registros por año

Lo esperado es que una emisoras identificada por un NRA solo cuente con un registro por año. Al consultar la cantidad de registros de establecimientos se detectó que hay dos registros que no cumplen este comportamiento. A los registros que no cumplen con el comportamiento esperado se le considera como una inconsistencia del registro de datos. A continuación de listan los dos casos en los que se puede observar esta situación: 

| nra          | anio | cantidad_reportes |
| ------------ | ---- | ----------------- |
| DMOMA1900611 | 2018 | 2                 |
| MTM7X0803712 | 2018 | 2                 |

### 

|      |      |      |
| ---- | ---- | ---- |
|      |      |      |
|      |      |      |
|      |      |      |
|      |      |      |
|      |      |      |
|      |      |      |
|      |      |      |
|      |      |      |
|      |      |      |
|      |      |      |
|      |      |      |



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

Para modificar el contenido de la base de datos se utilizó la herramienta MongoDB Compass que, mediante una interfaz gráfica, permite filtrar y a actualizar los datos. A continuación se presenta el contenido de los establecimientos después de ser corregidos:

```json
#Inconsistencia 1
#Filtro utilizado
{nra:"QUI5I1903911", $and:[{anio:{$gte:2004}}, {anio:{$lt:2010}}]}
#Establecimientos afecados 4
[{
  "_id": {
    "$oid": "65bec4d7675c397043f153aa"
  },
  "actprincipal": "FABRICACION DE GASES REFRIGERANTES",
  "actsemarnat": "Produccion de gases industriales",
  "anio": 2004,
  "calle": "AV. RUIZ CORTINES PTE",
  "claveambiental": "Atributo no considerado en este año",
  "codigopostal": "64400",
  "colonia": "PEDRO LOZANO",
  "descscian": "Atributo no considerado en este año",
  "entrec1": "CELULOSA",
  "entrec2": "PRIVADA ROBLE",
  "establecimiento": "QUIMOBASICOS S.A.DE C.V.",
  "estado": "NUEVO LEON",
  "latitudnorte": "25º 42' 46.97\"",
  "localidad": "MONTERREY",
  "longitudoeste": "100º 20' 7.29\"",
  "municipio": "Monterrey",
  "nra": "QUI5I1903911",
  "numexterior": "2333",
  "numinterior": "",
  "parqueindustrial": "",
  "scian": "Atributo no considerado en este año",
  "sector": "Quimica",
  "subsector": "Atributo no considerado en este año",
  "utmx": "0.0",
  "utmy": "0.0",
  "dbmod": 1,
  "dbdescmod": "No contenía el símbolo de minutos. Se agrego el símbolo de minutos en los atributos latitud norte y longitud oeste. "
},{
  "_id": {
    "$oid": "65bec4d7675c397043f17105"
  },
  "actprincipal": "FABRICACION DE GASES REFRIGERANTES",
  "actsemarnat": "Atributo no considerado en este año",
  "anio": 2007,
  "calle": "AV. RUIZ CORTINES PTE",
  "claveambiental": "5K",
  "codigopostal": "64400",
  "colonia": "PEDRO LOZANO",
  "descscian": "Fabricación de gases industriales.",
  "entrec1": "Atributo no considerado en este año",
  "entrec2": "Atributo no considerado en este año",
  "establecimiento": "QUIMOBASICOS S.A.DE C.V.",
  "estado": "NUEVO LEON",
  "latitudnorte": "25º 42' 46.97\" ",
  "localidad": "MONTERREY",
  "longitudoeste": "100º 20' 7.29\" ",
  "municipio": "Monterrey",
  "nra": "QUI5I1903911",
  "numexterior": "2333",
  "numinterior": "",
  "parqueindustrial": "",
  "scian": "325120",
  "sector": "Quimica",
  "subsector": "Produccion de gases industriales",
  "utmx": "",
  "utmy": "",
  "dbmod": 1,
  "dbdescmod": "No contenía el símbolo de minutos. Se agrego el símbolo de minutos en los atributos latitud norte y longitud oeste. "
},{
  "_id": {
    "$oid": "65bec4d7675c397043f17a98"
  },
  "actprincipal": "FABRICACION DE GASES REFRIGERANTES",
  "actsemarnat": "Atributo no considerado en este año",
  "anio": 2008,
  "calle": "AV. RUIZ CORTINES PTE",
  "claveambiental": "5K",
  "codigopostal": "64400",
  "colonia": "PEDRO LOZANO",
  "descscian": "Fabricación de gases industriales",
  "entrec1": "Atributo no considerado en este año",
  "entrec2": "Atributo no considerado en este año",
  "establecimiento": "QUIMOBASICOS S.A.DE C.V.",
  "estado": "NUEVO LEON",
  "latitudnorte": "25º 42' 46.97\" ",
  "localidad": "MONTERREY",
  "longitudoeste": "100º 20' 7.29\" ",
  "municipio": "Monterrey",
  "nra": "QUI5I1903911",
  "numexterior": "2333",
  "numinterior": "",
  "parqueindustrial": "",
  "scian": "325120",
  "sector": "Quimica",
  "subsector": "Produccion de gases industriales",
  "utmx": "",
  "utmy": "",
  "dbmod": 1,
  "dbdescmod": "No contenía el símbolo de minutos. Se agrego el símbolo de minutos en los atributos latitud norte y longitud oeste. "
},{
  "_id": {
    "$oid": "65bec4d7675c397043f183d1"
  },
  "actprincipal": "FABRICACION DE GASES REFRIGERANTES",
  "actsemarnat": "Atributo no considerado en este año",
  "anio": 2009,
  "calle": "AV. RUIZ CORTINES PTE",
  "claveambiental": "5K",
  "codigopostal": "64400.0",
  "colonia": "PEDRO LOZANO",
  "descscian": "Fabricación de gases industriales.",
  "entrec1": "Atributo no considerado en este año",
  "entrec2": "Atributo no considerado en este año",
  "establecimiento": "QUIMOBASICOS S.A.DE C.V.",
  "estado": "NUEVO LEON",
  "latitudnorte": "25º 42' 46.97\"",
  "localidad": "MONTERREY",
  "longitudoeste": "100º 20' 7.29\"",
  "municipio": "Monterrey",
  "nra": "QUI5I1903911",
  "numexterior": "2333",
  "numinterior": "",
  "parqueindustrial": "",
  "scian": "325120",
  "sector": "Quimica",
  "subsector": "Produccion de gases industriales",
  "utmx": "",
  "utmy": "",
  "dbmod": 1,
  "dbdescmod": "No contenía el símbolo de minutos. Se agrego el símbolo de minutos en los atributos latitud norte y longitud oeste. "
}]

#Filtro para obtener los registros de la segunda excepción 
{nra:"IVP7X1901211", longitudoeste: /º'/}
[{
  "_id": {
    "$oid": "65bec4d7675c397043f163aa"
  },
  "actprincipal": "METAL MECANICA",
  "actsemarnat": "Atributo no considerado en este año",
  "anio": 2006,
  "calle": "CARRETERA MONTERREY A LAREDO KM 22.5",
  "claveambiental": "7X",
  "codigopostal": "65550",
  "colonia": "SN",
  "descscian": "Fabricación de otros productos metálicos",
  "entrec1": "Atributo no considerado en este año",
  "entrec2": "Atributo no considerado en este año",
  "establecimiento": "INDUSTRIAS MONTERREY S.A DE C.V. PLANTA VARCO PRUDEN",
  "estado": "NUEVO LEON",
  "latitudnorte": "25º52'18.88\"",
  "localidad": "CIENEGA DE FLORES",
  "longitudoeste": "100º13'39.1\"",
  "municipio": "Cienega de Flores",
  "nra": "IVP7X1901211",
  "numexterior": "SN",
  "numinterior": "",
  "parqueindustrial": "CORREDOR INDUSTRIAL CIENEGA DE FLORES",
  "scian": "332999",
  "sector": "Articulos y productos metalicos",
  "subsector": "Fabricacion de articulos y productos metalicos",
  "utmx": "0.0",
  "utmy": "0.0",
  "dbmod": 1,
  "dbdescmod": "Contenía los símbolos de grados y minutos juntos en el atributo longitud oeste. Se removió el símbolo extra. "
},{
  "_id": {
    "$oid": "65bec4d7675c397043f16dcb"
  },
  "actprincipal": "METAL MECANICA",
  "actsemarnat": "Atributo no considerado en este año",
  "anio": 2007,
  "calle": "CARRETERA MONTERREY A LAREDO KM 22.5",
  "claveambiental": "7X",
  "codigopostal": "65550",
  "colonia": "SN",
  "descscian": "Fabricación de otros productos metálicos.",
  "entrec1": "Atributo no considerado en este año",
  "entrec2": "Atributo no considerado en este año",
  "establecimiento": "INDUSTRIAS MONTERREY S.A DE C.V. PLANTA VARCO PRUDEN",
  "estado": "NUEVO LEON",
  "latitudnorte": "25º52'18.88\"",
  "localidad": "CIENEGA DE FLORES",
  "longitudoeste": "100º13'39.1\"",
  "municipio": "Cienega de Flores",
  "nra": "IVP7X1901211",
  "numexterior": "SN",
  "numinterior": "",
  "parqueindustrial": "CORREDOR INDUSTRIAL CIENEGA DE FLORES",
  "scian": "332999",
  "sector": "Articulos y productos metalicos",
  "subsector": "Fabricacion de articulos y productos metalicos",
  "utmx": "0.0",
  "utmy": "0.0",
  "dbmod": 1,
  "dbdescmod": "Contenía los símbolos de grados y minutos juntos en el atributo longitud oeste. Se removió el símbolo extra. "
},{
  "_id": {
    "$oid": "65bec4d7675c397043f17739"
  },
  "actprincipal": "METAL MECANICA",
  "actsemarnat": "Atributo no considerado en este año",
  "anio": 2008,
  "calle": "CARRETERA MONTERREY A LAREDO KM 22.5",
  "claveambiental": "7X",
  "codigopostal": "65550",
  "colonia": "SN",
  "descscian": "Fabricación de otros productos metálicos",
  "entrec1": "Atributo no considerado en este año",
  "entrec2": "Atributo no considerado en este año",
  "establecimiento": "INDUSTRIAS MONTERREY S.A DE C.V. PLANTA VARCO PRUDEN",
  "estado": "NUEVO LEON",
  "latitudnorte": "25º52'18.88\"",
  "localidad": "CIENEGA DE FLORES",
  "longitudoeste": "100º13'39.1\"",
  "municipio": "Cienega de Flores",
  "nra": "IVP7X1901211",
  "numexterior": "SN",
  "numinterior": "",
  "parqueindustrial": "CORREDOR INDUSTRIAL CIENEGA DE FLORES",
  "scian": "332999",
  "sector": "Articulos y productos metalicos",
  "subsector": "Fabricacion de articulos y productos metalicos",
  "utmx": "0.0",
  "utmy": "0.0",
  "dbmod": 1,
  "dbdescmod": "Contenía los símbolos de grados y minutos juntos en el atributo longitud oeste. Se removió el símbolo extra. "
}]



##Filtro para obtener los registros de la tercera excepción 
{_id: ObjectId('65bec4d7675c397043f16772')}
{latitudnorte: /ª/}

{
  "_id": {
    "$oid": "65bec4d7675c397043f16772"
  },
  "actprincipal": "Producción de alambre de cobre y aluminio revestido",
  "actsemarnat": "Atributo no considerado en este año",
  "anio": 2006,
  "calle": "Av. México",
  "claveambiental": "7N",
  "codigopostal": "65550",
  "colonia": "Los Encinitos",
  "descscian": "Fundición y refinación de cobre",
  "entrec1": "Atributo no considerado en este año",
  "entrec2": "Atributo no considerado en este año",
  "establecimiento": "REA MAGNET WIRE TRADING COMPANY DE MÉXICO S.A. DE C.V.",
  "estado": "NUEVO LEON",
  "latitudnorte": "25º42'46.97\"",
  "localidad": "",
  "longitudoeste": "100º20'07.29\"",
  "municipio": "Cienega de Flores",
  "nra": "RMW7N1901211",
  "numexterior": "101 Ote",
  "numinterior": "",
  "parqueindustrial": "Parque Industrial Nacional",
  "scian": "331411",
  "sector": "Metalurgica (incluye la siderurgica)",
  "subsector": "Afinacion y refinacion de cobre",
  "utmx": "369380.0",
  "utmy": "2852095.0",
  "dbmod": 1,
  "dbdescmod": "Contenía el símbolo ª en vez del símbolo de grados en el atributo latitud norte. Se realizó el cambio. "
}
```



### Transformación de coordenadas en formato DMS a formato DD

Una vez corregidos los datos,  se realiza la trasformación de las coordenadas. Para trabajar con los datos fuera de línea, se obtiene un csv con los datos de las coordenadas. A continuación se muestra el filtro usado parra obtener solo los datos requeridos

```
[
  {
    $project:
      {
        latitudnorte: 1,
        longitudoeste: 1,
      },
  },
]
```

Se ejecuta el script de la transformación

```
python3 coor_transform.py
```

El resultado se almacenó en: 

```
/home/reyes/dev/posdoc-2022-2024/procesos/retc_emisoras/funciones/out_dms_dd/coordinates_v3_test2.csv
```

#### Resultado de la transformación

El resumen de la transformación es el siguiente

| Descripción                                                  | Número de establecimientos detectados |
| ------------------------------------------------------------ | :------------------------------------ |
| Establecimientos con coordenadas en formato DD. No requiere transformación (ddformat) | 3697                                  |
| Establecimientos con coordenadas en formato DMS. Requiere transformación (dmsformat) | 46842                                 |
| Establecimientos con coordenadas en formato DMS pero que contenían un valor que no puede ser transformado (dmsdefault) | 369                                   |
| **Total**                                                    | **50908**                             |
