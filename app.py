import os
import sys
from json import dumps

from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine

e = create_engine('sqlite:///main.db')

app = Flask(__name__)
api = Api(app)


class Restaurants_Meta(Resource):

    def get(self):
        cuisine_description = request.args.get('cuisine_description')
        grade = request.args.get('min_grade')
        limit = request.args.get('limit', 500)

        #Connect to databse
        conn = e.connect()
        #Perform query and return JSON data
        query = conn.execute(
            'SELECT * FROM restaurant where cuisine_description="Thai" and grade in ("A", "B") limit 10'
        )

        return {'restaurants': [i for i in query.cursor.fetchall()]}

api.add_resource(Restaurants_Meta, '/restaurants')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
