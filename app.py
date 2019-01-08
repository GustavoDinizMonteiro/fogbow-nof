import os
import requests
from flask_cors import CORS
from dotenv import load_dotenv
from flask import Flask, request

load_dotenv()

API = os.getenv('PROVIDER_API')
ENV = os.getenv('ENV')

app = Flask(__name__)
CORS(app)

ALL_METHODS = ['POST', 'PUT', 'PATCH', 'DELETE', 'GET']

@app.route('/', defaults={'path': ''}, methods=ALL_METHODS)
@app.route('/<path:path>', methods=ALL_METHODS)
def catch_all(path):
    if request.method == 'POST':
        pass
    resp = resend(request, path)
    return (resp.content, resp.status_code, resp.headers.items())


def resend(request, path):
    # NOTE: send headers crash requests in Postman mock API
    headers = {} if ENV == 'dev' else request.headers
    return requests.request(
        request.method, 
        API+path, 
        data=request.data, 
        headers=headers, 
        allow_redirects=True)

if __name__ == '__main__':
    app.run(debug=ENV=='dev')