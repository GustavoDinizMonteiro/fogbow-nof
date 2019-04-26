import os
import nof_services
from json import dumps
from flask_cors import CORS
from dotenv import load_dotenv
from flask import Flask, request
from db import create_member, update_global

load_dotenv()
update_global()

ENV = os.getenv('ENV')
app = Flask(__name__)
CORS(app)

ALL_METHODS = ['POST', 'PUT', 'PATCH', 'DELETE', 'GET']

@app.route('/', defaults={'path': ''}, methods=ALL_METHODS)
@app.route('/<path:path>', methods=ALL_METHODS)
def catch_all(path):
    def extract(resp):
        return resp.text, resp.status_code, {'Content-Type': 'application/json'}

    if request.method == 'POST':
        return extract(nof_services.create(request, path))
    return extract(nof_services.resend(request, path))

if __name__ == '__main__':
    app.run(debug=ENV=='dev')