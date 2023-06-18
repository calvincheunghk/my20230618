import sys

!pip install flash

import json
from flask import Flask, jsonify, request


def predict(my_input):
    if my_input == "a":
        my_result = "apple"
    elif my_input == "b":
        my_result = "baby"
    elif my_input == "c":
        my_result = "cat"
    else:
        my_result = "hello"
    
    return {'p': my_result}

application = Flask(__name__)


@application.route('/')
@application.route('/status')
def status():
    return jsonify({'status': 'ok'})

@application.route('/p', methods=['POST'])
def my_prediction():
    data = request.data or '{}'
    body = json.loads(data)
    return jsonify(predict(body))

if __name__ == '__main__'
	application.run()






