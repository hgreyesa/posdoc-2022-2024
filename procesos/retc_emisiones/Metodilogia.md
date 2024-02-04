# Metodología para la generación de la base de datos de las emisiones de sustancias RETC

## Recolección de datos

Los datos fueron adquiridos desde la página del RETC.

## Revisión de las columnas por archivo

Se descargaron los archivos del 2004 al 2023. Cada archivo contiene los detalles de las emisiones registradas en la base de datos del RETC.

Se detecto que existen tres formatos diferentes en los archivos. Cada formato contiene diferente número de atributos (columnas) y en algunos casos un nombre distinto para el mismo atributo. A continuación se listan los atributos para cada formato:

1. Periodo de 16 años comprendido por los periodos de 2006 a 2011 (6 años) y de 2013 a 2022 (10 años)
2. Periodo de 2 años comprendido por los años 2004 y 2005
3. Periodo comprendido por los registros del año 2012

| Formato 1 (2006-2011 y 2013-2022) | Formato 2 (2004-2005) | Formato 3 (2012)   |
| --------------------------------- | --------------------- | ------------------ |
| Anio                              | Anio                  | Anio               |
| NRA                               | NRA                   | NRA                |
| NOMBRE                            | Nombre                | Establecimiento    |
| SECTOR                            | Sector                | Sector             |
| ESTADO                            | Estado                | Entidad Federativa |
| MUNICIPIO                         |                       | Municipio          |
| CAS                               | No. CAS               | CAS                |
| SUSTANCIA                         | Descripción           | Sustancia          |
| UNIDAD                            | Unidad                | Unidad             |
| AIRE                              | Aire                  | Aire               |
| AGUA                              | Agua                  | Agua               |
| SUELO                             | Suelo                 | Suelo              |
| REUTILIZACIÓN                     | Reuso                 | Reutilización      |
| RECICLADO                         | Reciclado             | Reciclado          |
| COPROCESAMIENTO                   | Coprocesamiento       | Coprocesamiento    |
| TRATAMIENTO                       | Tratamiento           | Tratamiento        |
| DISPOSICIÓN FINAL                 | Disposición final     | Disposición Final  |
| ALCANTARILLADO                    | Incineración          | Alcantarillado     |
| INCINERACIÓN                      | Alcantarillado        | Incineración       |
| OTROS                             | Otros                 | Otro               |
|                                   |                       | Grupo Sustancia    |

Para mantener una consistencia en la base de datos, se opto por adicionar las columnas no consideradas en los distintos formatos y colocar como valor por defecto "Atributo no considerado en este año". Adicionalmente se opto por realizar el cambio de nombres de los atributos para mantener una base de datos homogénea.

| Formato 1 (2006-2011 y 2013-2022) | Formato 2 (2004-2005) | Formato 3 (2012)   |
| --------------------------------- | --------------------- | ------------------ |
| anio                              | anio                  | anio               |
| nra                               | nra                   | nra                |
| nombre                            | nombre                | nombre             |
| sector                            | sector                | sector             |
| estado                            | estado                | estado             |
| municipio                         | **municipio**         | municipio          |
| cas                               | cas                   | cas                |
| sustancia                         | sustancia             | sustancia          |
| unidad                            | unidad                | unidad             |
| em_aire                           | em_aire               | em_aire            |
| em_agua                           | em_agua               | em_agua            |
| em_suelo                          | em_suelo              | em_suelo           |
| tr_reutilizacion                  | tr_reutilizacion      | tr_reutilizacion   |
| tr_reciclado                      | tr_reciclado          | tr_reciclado       |
| tr_coprocesamiento                | tr_coprocesamiento    | tr_coprocesamiento |
| tr_tratamiento                    | tr_tratamiento        | tr_tratamiento     |
| tr_dispfinal                      | tr_dispfinal          | tr_dispfinal       |
| tr_alcantarillado                 | tr_alcantarillado     | tr_alcantarillado  |
| tr_incineracion                   | tr_incineracion       | tr_incineracion    |
| tr_otros                          | tr_otros              | tr_otros           |
| **gruposustancia**                | **gruposustancia**    | gruposustancia     |

Se ordenan los nombres de las columnas para hacer el proceso de fusión más sencillo:



Como se puede observar, existen columnas repetidas que se encuentran en la basede datos de emisoras, por tal motivo se decidió remover los siguientes datos:

* nombre
* sector
* estado
* municipio

