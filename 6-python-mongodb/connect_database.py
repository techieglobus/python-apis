import pymongo

def connectDatabase(hostname,port):
    database_url = 'mongodb://'+str(hostname)+':'+str(port)+'/'
    mongo_client = pymongo.MongoClient(database_url)
    return mongo_client


# result = connectDatabase('localhost',27017)
# print(result)