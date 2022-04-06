from flask import Flask,jsonify,request
import pymongo


def connectDatabase(hostname,port):
    database_url = 'mongodb://'+str(hostname)+':'+str(port)+'/'
    mongo_client = pymongo.MongoClient(database_url)
    return mongo_client

app = Flask(__name__)

@app.route('/user',methods=['POST'])
def createUser():
    if (request.method == 'POST'):
        name = request.json.get('name')
        gender = request.json.get('gender')
        age = request.json.get('age')
        client = connectDatabase('localhost', 27017)
        db_instance = client['amity']
        coll_instance = db_instance['users']
        coll_instance.insert_one(request.json)
        return jsonify({'message' : 'User created successfully'})
    else:
        return jsonify({'message' : 'Invalid Method'})


if __name__ == '__main__':
    app.run(debug=True)