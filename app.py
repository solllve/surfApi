from flask import Flask
from ready import ReadyAPI

app = Flask(__name__)

print('Running Server At: http://localhost:5000/')
print('-------------')
print('Ready Endpoint: http://localhost:5000/ready')

@app.route('/')
def index():
    return "Nothing to see here"

@app.route('/ready', methods=['GET'])
def readyApi():
    return ReadyAPI().get()
