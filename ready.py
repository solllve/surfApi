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

        content = jsonify({
            "success": True
        })

        return content
