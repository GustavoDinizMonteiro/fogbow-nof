from flask import Flask
from middleware import SimpleMiddleWare
app = Flask(__name__)
# app.wsgi_app = SimpleMiddleWare(app.wsgi_app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello(path):
    return "Hello World!"