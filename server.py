from flask import Flask
from flask import request
from flask_cors import CORS
from flask_restful import Resource, Api
import time
from werkzeug.serving import WSGIRequestHandler

app = Flask(__name__)
api = Api(app)
CORS(app)

class Test(Resource):
    def get(self, path):
        print(path)
        print(request.headers)
        time.sleep(0.1)
        return {"path":path}, 200


api.add_resource(Test, '/<path>')

if __name__ == '__main__':
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(port=5555, debug=True)