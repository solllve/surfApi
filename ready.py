from flask import jsonify

class ReadyAPI():
    def get(self):
        content = jsonify({
            "success": True
        })

        return content
