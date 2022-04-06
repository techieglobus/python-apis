from connect_database import connectDatabase


def captureInputs():
    db_name = input("Please enter database name: ")
    collection_name = input("Please enter collection name: ")
    data = {
        'db_name' : db_name,
        'collection_name' : collection_name
    }
    return data

def createDatabase(data):
    global client
    print("Connecting to database server")
    client = connectDatabase('localhost',27017)
    print("Creating database : ",data['db_name'])
    db_instance = client[data['db_name']]
    return db_instance

def createCollection(db_instance,data):
    print("Creating collection : ", data['collection_name'])
    coll_instance = db_instance[data['collection_name']]
    coll_instance.insert_one({'record':'dummy'})
    return coll_instance

def listDatabases():
    databases = client.list_database_names()
    print("---------------------------- Databases ---------------------------------------")
    for database in databases:
        print(database)
    print("------------------------------------------------------------------------------")
    return databases

def listCollections(databases):
    for database in databases:
        db_instance = client[database]
        collections = db_instance.list_collection_names()
        print("---------------------------- Database ",database," Collections -------------------------------------")
        for collection in collections:
          print(collection)
        print("------------------------------------------------------------------------------")

data = captureInputs()
db_instance = createDatabase(data)
coll_instance = createCollection(db_instance,data)
databases = listDatabases()
listCollections(databases)


