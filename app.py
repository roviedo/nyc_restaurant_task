import os
import sys
from json import dumps

from flask import Flask, request, render_template
from flask_restful import Resource, Api

import connect_to_db
import utils
import tasks


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

        if request.args.get('camis'):
            params['camis'] = request.args['camis']

        if request.args.get('boro'):
            params['boro'] = request.args['boro']

        if request.args.get('limit'):
            params['limit'] = request.args['limit']
        else:
            #TODO: For now max rows, might need to add pagination
            params['limit'] = 1000

        query = utils.build_query(params)

        # Connect to database
        if os.environ.get('env') == 'DEV':
            conn = connect_to_db.connect_to_sqlite3('main.db')
        else:
            conn = connect_to_db.connect_to_postgres()

        cursor = conn.cursor()

        #Perform query and return JSON data
        cursor.execute(
            # e.g. 'SELECT * FROM restaurant where cuisine_description="Thai" and grade in ("A", "B") limit 10'
            query
        )

        restaurants = [utils.build_json(row) for row in cursor.fetchall()]

        return {
            'restaurants': restaurants,
            'count': len(restaurants)
        }


class ETL_Runner(Resource):

    def post(self):
        if os.environ.get('env') == 'DEV':
            tasks.runner()
        else:
            tasks.runner.delay()
        return "created", 201


api.add_resource(Restaurants_Meta, '/restaurants')
api.add_resource(ETL_Runner, '/etl_runner')


#### App endpoints
@app.route('/')
def index():
    #TODO: This endpoint should live in another module or app altogether
    return render_template('index.html')

@app.route('/etl')
def etl():
    #TODO: This endpoint should live in another module or app altogether
    return render_template('etl.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
