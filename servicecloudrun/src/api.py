import sys
from flask import request, jsonify
from flask_expects_json import expects_json
from flask_api import FlaskAPI, status, exceptions
import os

app = FlaskAPI(__name__)


@app.route('/apis/gethello/1.0.0', methods=['GET'])
def get_hello_world():
    """
    Gets a simple Hello World
    """
    try:        
        return "Hello World", status.HTTP_200_OK
    except Exception as e:        
        return {
            CODE: 500,
            MESSAGE: str(e)
        }, status.HTTP_500_INTERNAL_SERVER_ERROR


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
