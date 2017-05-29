import os
import sys
from json import dumps

from flask import Flask, request, render_template
from flask_restful import Resource, Api

import connect_to_db


app = Flask(__name__)
api = Api(app)


#### API endpoints
class Restaurants_Meta(Resource):

    def get(self):
        params = {}
        if request.args.get('cuisine_description'):
            params['cuisine_description'] = request.args['cuisine_description']

        if request.args.get('min_grade'):
            params['min_grade'] = request.args['min_grade']

        if request.args.get('limit'):
            params['limit'] = request.args['limit']
        else:
            #TODO: For now max rows, might need to add pagination
            params['limit'] = 1000

        #TODO: Build query by urlparams
        query = build_query(params)
        print(query)

        # Connect to database
        if os.environ.get('env') == 'DEV':
            conn = connect_to_db.connect_to_sqlite3('main.db')
        else:
            #TODO: this should be postgres since we are on heroku
            conn = connect_to_db.connect_to_postgres()

        cursor = conn.cursor()

        #Perform query and return JSON data
        print('this query {}'.format(query))
        cursor.execute(
            # 'SELECT * FROM restaurant where cuisine_description="Thai" and grade in ("A", "B") limit 10'
            query
        )

        restaurants = [build_json(row) for row in cursor.fetchall()]

        return {
            'restaurants': restaurants,
            'count': len(restaurants)
        }

api.add_resource(Restaurants_Meta, '/restaurants')


#### App endpoints
@app.route('/')
def index():
    #TODO: This endpoint should live in another module or app altogether
    return render_template('index.html')


#### Helper functions
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

def build_query(params):
    query = 'SELECT * FROM restaurant'
    grades = ("A", "B", "C","D", "E", "F")
    where_clauses = []
    if params.get('min_grade') == 'A':
        where_clauses.append('grade=="A"')
    elif params.get('min_grade'):
        where_clauses.append('grade in {}'.format(grades[0:grades.index(params['min_grade'])+1]))

    if params.get('cuisine_description'):
        where_clauses.append('cuisine_description="%s"' % params['cuisine_description'])


    if where_clauses:
        where_clauses_string = ' AND '.join(where_clauses)
        return '{} where {} limit {}'.format(query, where_clauses_string, params['limit'])
    else:
        return '{} limit {}'.format(query, params['limit'])


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
