from connect_database import connectDatabase


def captureInputs():
    db_name = input("Please enter database name: ")
    collection_name = input("Please enter collection name: ")
    data = {
        'db_name' : db_name,
        'collection_name' : collection_name
    }
    return data


def insertDummyData(data):
    print("Inserting data : ", data['collection_name'])
    client = connectDatabase('localhost',27017)
    db_instance = client[data['db_name']]
    coll_instance = db_instance[data['collection_name']]
    coll_instance.insert_many([
        {'name':'John', 'gender': 'Male', 'age' : 32},
        {'name': 'Smith', 'gender': 'Male', 'age': 50},
        {'name': 'Marry', 'gender': 'Female', 'age': 40},
        {'name': 'Maria', 'gender': 'Female', 'age': 36},
        {'name': 'Bob', 'gender': 'Male', 'age': 25},
])
    print(coll_instance.find())
    for row in coll_instance.find():
        print(row)


data = captureInputs()
insertDummyData(data)


