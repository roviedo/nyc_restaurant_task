import os
import sys
from json import dumps

from flask import Flask, request
from flask_restful import Resource, Api

import connect_to_db


app = Flask(__name__)
api = Api(app)


class Restaurants_Meta(Resource):

    def get(self):
        cuisine_description = request.args.get('cuisine_description')
        grade = request.args.get('min_grade')
        limit = request.args.get('limit', 500)

        #TODO: Build query by urlparams
        query = 'SELECT * FROM restaurant'

        #Connect to databse
        # conn = e.connect()
        # conn = connect_to_db.connect_to_sqlite3('main.db')
        # cursor = conn.cursor()
        #
        # #Perform query and return JSON data
        # cursor.execute(
        #     'SELECT * FROM restaurant where cuisine_description="Thai" and grade in ("A", "B") limit 10'
        # )
        #
        # restaurants = [build_json(row) for row in cursor.fetchall()]
        restaurants = {'hola': 'amigo'}
        return {
            'restaurants': restaurants,
            'count': len(restaurants)
        }

api.add_resource(Restaurants_Meta, '/restaurants')

def build_json(row):
    return {
        'id': row[0],
        'camis': row[1],
        'name': row[2],
        'boro': row[3],
        'building': row[4],
        'street': row[5],
        'zipcode': row[6],
        'phone': row[7],
        'cuisine_description': row[8],
        'inspection_date': row[9],
        'action': row[10],
        'violation_code': row[11],
        'violation_description': row[12],
        'critical_flag': row[13],
        'score': row[14],
        'grade': row[15],
        'grade_date': row[16],
        'record_date': row[17],
        'inspection_type': row[18]
    }


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
