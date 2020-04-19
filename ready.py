from flask import jsonify
import json
import requests

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
