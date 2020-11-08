from flask import *
from flask_cors import *

from mongo.MongoDB import *

USERNAME = PASSWORD = "mongo"
DB = "sandboxDB"
COLLECTIONS = {"sandbox": AUTO_INCREMENT}
URL = f"mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.u6lhh.mongodb.net/{DB}?retryWrites=true&w=majority"

mongo = MongoDB(url=URL, database=DB, collections=COLLECTIONS)
sandbox = mongo.collection["sandbox"]

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "<h1>API Sandbox</h1>" \
           "<p> To play around with the APIs, follow the guide below</p>" \
           "<ul>" \
           "<li> /add, POST, (request body required)" \
           "<li> /showAll, GET" \
           "<li> /update/<id>, PUT" \
           "<li> /delete/<id>, DELETE" \
           "</ul>"


@app.route('/add', methods=['POST'])
def add_to_db():
    obj = request.get_json()
    sandbox.add(obj)
    return jsonify(sandbox.find_by_criteria(obj))


@app.route('/showAll', methods=['GET'])
def show_collections():
    return jsonify(sandbox.find_all())


@app.route('/update/<_id>/<k>/<v>', methods=['PUT'])
def update_by_id(_id, k, v):
    sandbox.update_by_id(_id, key=k, value=v)
    return jsonify(sandbox.find_by_id(_id))


@app.route('/delete/<_id>', methods=['DELETE'])
def delete_by_id(_id):
    deleted = sandbox.find_by_id(_id)
    sandbox.remove_by_id(_id)
    return jsonify(deleted)


if __name__ == '__main__':
    CORS(app)
    app.run(debug=True)
