from flask import *
from flask_cors import *

# runtime configurations


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "<h1>hello world<h1>"


if __name__ == '__main__':
    CORS(app)
    app.run()
