import requests 

from flask import Flask, request
from json import dumps
from flask import jsonify

app = Flask(__name__)

@app.route('/github/events', methods=['GET'])
def github_timeline():
    return jsonify(requests.get('https://api.github.com/users/ikaradimas/events').json())

if __name__ == '__main__':
    app.run(port='5004')
     