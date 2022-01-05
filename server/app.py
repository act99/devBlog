from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin
from pymongo import MongoClient

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

client = MongoClient('localhost', 27017)
db = client.devblogDB



# createPost
@app.route('/api/post', methods=['POST'])
@cross_origin()
def posting():
    print(request.json)
    return 'received'

# readPosts
@app.route('/api/post/<id>', methods=['GET'])
@cross_origin()
def listing():
    listings = list(db.postings.find({}, {'_id': False}))
    return jsonify({'listings': listings})

# readPost
@app.route('/api/post/<id>', methods=['GET'])
@cross_origin()
def getting():
    listings = list(db.postings.find({}, {'_id': False}))
    return jsonify({'listings': listings})

# createPost
@app.route('/api/post/<id>', methods=['GET'])
@cross_origin()
def delete():
    return 'received'

# createPost
@app.route('/api/post/<id>', methods=['PUT'])
@cross_origin()
def update():
    return 'received'





if __name__ == '__main__':
    app.run(port=5000, debug=True)
