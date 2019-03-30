import os
import nof_services
from flask_cors import CORS
from dotenv import load_dotenv
from flask import Flask, request
from db import create_member, update_global

load_dotenv()
update_global(1) # TODO: check how is the default value for this.

ENV = os.getenv('ENV')
app = Flask(__name__)
CORS(app)

ALL_METHODS = ['POST', 'PUT', 'PATCH', 'DELETE', 'GET']

@app.route('/', defaults={'path': ''}, methods=ALL_METHODS)
@app.route('/<path:path>', methods=ALL_METHODS)
def catch_all(path):
    def extract(resp):
        return (resp.content, resp.status_code, resp.headers.items())

    if request.method == 'POST':
        return extract(nof_services.create_local(request, path))
    return extract(nof_services.resend(request, path))

if __name__ == '__main__':
    app.run(debug=ENV=='dev')