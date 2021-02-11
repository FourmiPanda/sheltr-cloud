from flask import Flask, request, jsonify
import json
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome to Sheltr cloud ☁️ !'


@app.route('/find')
def find_route():
    return jsonify({})


if __name__ == '__main__':
    app.run()
