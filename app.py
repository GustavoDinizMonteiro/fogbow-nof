from flask_cors import CORS
from middleware import resend
from flask import Flask, request

app = Flask(__name__)
CORS(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello(path):
    if request.method == 'POST':
        pass
    return resend(request, path)

if __name__ == '__main__':
    app.run()