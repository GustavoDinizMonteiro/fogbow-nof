from flask_cors import CORS
from middleware import resend
from flask import Flask, request

app = Flask(__name__)
CORS(app)

ALL_METHODS = ['POST', 'PUT', 'PATCH' 'DELETE', 'GET']

@app.route('/', defaults={'path': ''}, methods=ALL_METHODS)
@app.route('/<path:path>', methods=ALL_METHODS)
def hello(path):
    if request.method == 'POST':
        pass
    return resend(request, path)

if __name__ == '__main__':
    app.run()