from flask import *
from flask_cors import *

# runtime configurations


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "<h1>hello world<h1>"


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


if __name__ == '__main__':
    CORS(app)
    app.debug = True
    app.run()
