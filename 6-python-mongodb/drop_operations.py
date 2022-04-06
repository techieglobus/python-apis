from connect_database import connectDatabase


def captureInputs(choice):
    if choice == "1":
        db_name = input("Please enter database name: ")
        data = {
            'db_name': db_name
        }
    elif choice == "2":
        db_name = input("Please enter database name: ")
        collection_name = input("Please enter collection name: ")
        data = {
        'db_name' : db_name,
        'collection_name' : collection_name
        }
    else:
        data = ""
    return data

def dropDatabase(data):
    global client
    print("Connecting to database server")
    client = connectDatabase('localhost',27017)
    print("Dropping database : ",data['db_name'])
    client.drop_database(data['db_name'])

def dropCollection(data):
    global client
    print("Dropping collection : ", data['collection_name'])
    client = connectDatabase('localhost', 27017)
    db_instance = client[data['db_name']]
    coll_instance = db_instance[data['collection_name']]
    coll_instance.drop()

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


choice = input("Please select the operation : 1) Drop Database 2) Drop Collection")
data = captureInputs(choice)
if choice == "1":
    dropDatabase(data)
    listDatabases()
elif choice == "2":
    dropCollection(data)
    databases = listDatabases()
    listCollections(databases)
else:
    print("Invalid Choice")

