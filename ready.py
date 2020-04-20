from flask import jsonify
import json
import re
import urllib
import time
import requests
from flask import jsonify
from bs4 import BeautifulSoup
from scraper import ScrapeAPI

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
        #headers = {
        #    'User-Agent': 'Chrome/[.0-9]*'
        #}
        sanClemente = requests.get("https://api.weather.gov/gridpoints/SGX/44,47/forecast/hourly")
        #tidalSource = requests.get('https://tides.willyweather.com/ca/orange-county/san-clemente-pier.html', headers=headers)
        #content = BeautifulSoup(tidalSource.content, "html.parser")
        #was playing with a website scraper
        #if tidalSource.status_code == 200:
        #    title = content.find('body').text()

        content = jsonify({
            "source": "San Clemente",
            "response": sanClemente.status_code,
            "data": sanClemente.json()
        })
        return content

class getDanaPoint():
    def get(self):
        danaPoint = requests.get("https://api.weather.gov/gridpoints/LOX/170,14/forecast/hourly")
        content = jsonify({
            "source": "Dana Point",
            "response": danaPoint.status_code,
            "data": danaPoint.json()
        })
        return content

class getLagunaBeach():
    def get(self):
        lagunaBeach = requests.get("https://api.weather.gov/gridpoints/SGX/39,53/forecast/hourly")
        content = jsonify({
            "source": "Laguna Beach",
            "response": lagunaBeach.status_code,
            "data": lagunaBeach.json()
        })
        return content
