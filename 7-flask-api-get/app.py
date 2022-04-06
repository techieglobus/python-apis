from flask import Flask,jsonify,request
import pymongo


def connectDatabase(hostname,port):
    database_url = 'mongodb://'+str(hostname)+':'+str(port)+'/'
    mongo_client = pymongo.MongoClient(database_url)
    return mongo_client

app = Flask(__name__)

@app.route('/users',methods=['GET'])
def getUsers():
    if (request.method == 'GET'):
        client = connectDatabase('localhost',27017)
        db_instance = client['amity']
        coll_instance = db_instance['users']
        users = []
        for record in coll_instance.find():
            user = {}
            user['name'] = record['name']
            user['gender'] = record['gender']
            users.append(user)
        return jsonify(users)
    else:
        return jsonify({'message' : 'Invalid Method'})

if __name__ == '__main__':
    app.run(debug=True)