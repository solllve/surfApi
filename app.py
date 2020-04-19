from flask import Flask
from ready import ReadyAPI
from ready import getSurfSpots
from ready import getSanClemente

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

@app.route('/all', methods=['GET'])
def getSurfSpotInfo():
    return getSurfSpots().get()

@app.route('/san-clemente', methods=['GET'])
def getSanClementeInfo():
    return getSanClemente().get()
