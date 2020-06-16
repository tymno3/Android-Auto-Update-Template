from flask import Flask, request
import json
from tinydb import TinyDB

app = Flask(__name__)
db = TinyDB('db.json')


@app.route('/', methods=['GET'])
def get_app_versions():
    print(f'Request: {request}')
    return json.dumps({"items": db.all()})


if __name__ == '__main__':
    app.run()
