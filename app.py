from flask import *
from flask_cors import *

from mongo.MongoDB import MongoDB

USERNAME = PASSWORD = "mongo"
DB = "sandboxDB"
COLLECTIONS = ["sandbox"]
URL = f"mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.u6lhh.mongodb.net/{DB}?retryWrites=true&w=majority"

mongo = MongoDB(url=URL, database=DB, docs=COLLECTIONS)
sandbox = mongo.collection["sandbox"]

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "<h1>heroku flask app</h1>" \
           "<p> To test mongo db functionalities, open " \
           "Postman and use the following url patterns, with the respective request" \
           "<ul>" \
           "<li> /add, POST" \
           "<li> /showAll, GET" \
           "</ul>"


@app.route('/tutor', methods=['GET'])
def get_tutor():
    return {
        "name": "omruti",
        "fav subjects":
            [
                "research",
                "data science",
                "sql",
                "literature"
            ]
    }


@app.route('/add', methods=['POST'])
def add_to_db():
    obj = request.get_json()
    sandbox.add(obj)
    return obj


@app.route('/showAll', methods=['GET'])
def show_collections():
    return jsonify(sandbox.find_all())


if __name__ == '__main__':
    CORS(app)
    app.debug = True
    app.run()
