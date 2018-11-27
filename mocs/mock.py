from flask_cors import CORS
from flask import Flask, request

app = Flask(__name__)
CORS(app)

bd = {
    1: { id: 'compute-1' }
}

@app.route('/computes/<int:id>', methods=['GET'])
def hello(id):
    return 

if __name__ == '__main__':
    app.run(port=3000)