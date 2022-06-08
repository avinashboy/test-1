from gartner import WebScraperGartner 
from techmeme import WebScraperTechMeme 
from flask import Flask, jsonify
from flask_restful import Resource, Api

URL1 = "https://www.gartner.com/en/conferences/calendar"
URL2 = "https://www.techmeme.com/events"


app = Flask(__name__)
api = Api(app)

# Resource
class Gartner(Resource):
    def get(self):
        data = WebScraperGartner(URL1).start()
        return jsonify(count=len(data),data=data,status=200,success=True)


class TechMeme(Resource):
    def get(self):
        data = WebScraperTechMeme(URL2).start()
        return jsonify(count=len(data),data=data,status=200,success=True)


# API End-points
api.add_resource(Gartner, '/gartner')
api.add_resource(TechMeme, '/techmeme')



if __name__ == '__main__':
    app.run(debug=True)