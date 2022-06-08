from gartner import WebScraperGartner 
from techmeme import WebScraperTechMeme 
from flask import Flask, jsonify
from flask_restful import Resource, Api
import os, json

URL1 = "https://www.gartner.com/en/conferences/calendar"
URL2 = "https://www.techmeme.com/events"


app = Flask(__name__)
api = Api(app)

# Resource
class Gartner(Resource):
    def get(self):
        if not os.path.exists("./data/gartner.json"):
            data = WebScraperGartner(URL1).start()
            with open("./data/gartner.json", "w") as f:
                f.write(json.dumps(data, indent = 4))
        else:
            data = ""
            with open("./data/gartner.json", "r") as f:
                data = json.loads(f.read())
        return jsonify(status=200,success=True,count=len(data),data=data)


class TechMeme(Resource):
    def get(self):
        if not os.path.exists("./data/techmeme.json"):
            data = WebScraperTechMeme(URL2).start()
            with open("./data/techmeme.json", "w") as f:
                f.write(json.dumps(data, indent = 4))
        else:
            data = ""
            with open("./data/techmeme.json", "r") as f:
                data = json.loads(f.read())
        return jsonify(status=200,success=True,count=len(data),data=data)


class ClearFile(Resource):
    def get(self):
        if os.path.exists("./data/gartner.json"):
            os.remove("./data/gartner.json")
        if os.path.exists("./data/techmeme.json"):
            os.remove("./data/techmeme.json")
        return jsonify(status=200,success=True)


# API End-points
api.add_resource(Gartner, '/gartner')
api.add_resource(TechMeme, '/techmeme')
api.add_resource(ClearFile, '/clear')



if __name__ == '__main__':
    app.run(debug=True)