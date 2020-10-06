from flask import *
from flask_cors import *

# runtime configurations


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "<h1>hello world<h1>"


def main():
    CORS(app)
    app.run(host='0.0.0.0')


main()
