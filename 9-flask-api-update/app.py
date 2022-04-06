from flask import Flask,jsonify,request
import pymongo


def connectDatabase(hostname,port):
    database_url = 'mongodb://'+str(hostname)+':'+str(port)+'/'
    mongo_client = pymongo.MongoClient(database_url)
    return mongo_client

app = Flask(__name__)

@app.route('/user/<name>',methods=['PUT'])
def updateUser(name):
    if (request.method == 'PUT'):
        client = connectDatabase('localhost', 27017)
        db_instance = client['amity']
        coll_instance = db_instance['users']
        a = coll_instance.find_one({"name" : name})
        if a is not None:
            coll_instance.update_one({"name" : name},{"$set" : request.json})
            return jsonify({'message': 'User updated successfully'})
        else:
            return jsonify({'message' : 'User does not exist'})
    else:
        return jsonify({'message' : 'Invalid Method'})


if __name__ == '__main__':
    app.run(debug=True)