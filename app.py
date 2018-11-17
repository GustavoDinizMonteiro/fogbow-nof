from middleware import resend

from flask import Flask, request

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello(path):
    if request.method == 'POST':
        continue
    return resend(request, path)