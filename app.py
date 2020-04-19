from flask import Flask
from ready import ReadyAPI
from ready import getSurfSpots
from ready import getSanClemente
from ready import getDanaPoint
from ready import getLagunaBeach

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

@app.route('/dana-point', methods=['GET'])
def getDanaPointInfo():
    return getDanaPoint().get()

@app.route('/laguna-beach', methods=['GET'])
def getLagunaBeachInfo():
    return getLagunaBeach().get()
