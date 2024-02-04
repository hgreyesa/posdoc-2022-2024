from pymongo import MongoClient
import urllib.parse

def getMongoClientSemarnatReader():
    username = urllib.parse.quote_plus('tuusuarioconpermisosdelectura')
    pwd = urllib.parse.quote_plus('contrasenioadelusuarioconpermisosdelectura.')
    uri = 'mongodb://%s:%s@ipserver:puerto/nombrebasedatos'

    client = MongoClient(uri % (username, pwd))
    return client

def getMongoClientSemarnatWriter():
    username = urllib.parse.quote_plus('2023PosdocUASLP-writersemarnat')
    pwd = urllib.parse.quote_plus('contrasenioadelusuarioconpermisosdeescritura.')
    uri = 'mongodb://%s:%s@ipserver:puerto/nombrebasedatos'

    client = MongoClient(uri % (username, pwd))
    return client

def closeSemarnatDB(client):
    client.close()


def getDbCollectionSemarnat(client, database):
    #logging.info("Se obtiene la conexion a la base de datos: " + database)
    db = client[database]
    return db