from flask import jsonify
import json
import requests

class prettyJSON():
    def jprint(obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        return text

class ReadyAPI():
    def get(self):
        content = jsonify({
            "success": True
        })
        return content

class getSurfSpots():
    def get(self):
        coastalCa = requests.get("https://api.coastal.ca.gov/access/v1/locations")
        content = jsonify({
            "source": "Coastal California API",
            "response": coastalCa.status_code,
            "data": coastalCa.json()
        })
        return content

class getSanClemente():
    def get(self):
        sanClemente = requests.get("https://api.weather.gov/points/33.43,-117.62")
        content = jsonify({
            "source": "San Clemente",
            "response": sanClemente.status_code,
            "data": sanClemente.json()
        })
        return content
