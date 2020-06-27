from flask import Flask, request
import json
from tinydb import TinyDB

app = Flask(__name__)
db = TinyDB('db.json')


@app.route("/")
def index():
    return "Homepage"


@app.route('/version/', methods=['GET'])
def get_app_versions():
    # print(f'Request: {request}')
    username = request.args.get('username')
    current_version = request.args.get('current_version')
    desired_version = get_desired_version(username, current_version)
    return json.dumps({"desired_version": desired_version})


def get_desired_version(username, current_version):
    # todo(tding): Actually use username and current version to determine the highest version
    return highest_version()


def highest_version():
    all_versions = [row['version'] for row in db.all()]
    return max(all_versions)


if __name__ == '__main__':
    app.run()
