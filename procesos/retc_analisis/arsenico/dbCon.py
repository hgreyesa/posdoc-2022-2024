from pymongo import MongoClient
import urllib.parse

def getMongoClientSemarnatReader():
    username = urllib.parse.quote_plus('2023PosdocUASLP-readersemarnat')
    pwd = urllib.parse.quote_plus('e9458f6d391f09ce947843a57f7f1a60ea1fdd18dd3b91189d432b7e29e566f1.')
    uri = 'mongodb://%s:%s@172.17.0.1:26377/semarnat'

    client = MongoClient(uri % (username, pwd))
    return client

def getMongoClientSemarnatWriter():
    username = urllib.parse.quote_plus('2023PosdocUASLP-writersemarnat')
    pwd = urllib.parse.quote_plus('f90e99134248fd422b5ad16a6365f30df1902a0305e5eeedd6bd049ea010e1a5.')
    uri = 'mongodb://%s:%s@172.17.0.1:26377/semarnat'

    client = MongoClient(uri % (username, pwd))
    return client

def getMongoClientReader():
    username = urllib.parse.quote_plus('2023PosdocUASLP-readerdenue')
    pwd = urllib.parse.quote_plus('4ab082bf261e5d8699e8d4a046157c3c5755b7e97a939e20a477c1dc34e13a5b.')
    uri = 'mongodb://%s:%s@172.17.0.1:25377/backupdenue'
    client = MongoClient(uri % (username, pwd))
    return client

def getMongoClientWriter():
    username = urllib.parse.quote_plus('2023PosdocUASLP-writerdenue')
    pwd = urllib.parse.quote_plus('a7ceb40123984d2dfb84e59fb28fb7f67499bf6bd82308c3239ed881e9f8aa45.')
    uri = 'mongodb://%s:%s@172.17.0.1:25377/backupdenue'
    client = MongoClient(uri % (username, pwd))
    #db = client['backupdenue']
    return client

def closeDB(client):
    client.close()

def closeSemarnatDB(client):
    client.close()


def getDbCollectionSemarnat(client, database):
    #logging.info("Se obtiene la conexion a la base de datos: " + database)
    db = client[database]
    return db