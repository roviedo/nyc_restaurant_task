import os

import celery

import settings
import extract
import transform
import load


app = celery.Celery('etl_runner')
app.conf.update(
    BROKER_URL=os.environ.get('REDIS_URL'),
    CELERY_RESULT_BACKEND=os.environ.get('REDIS_URL')
)


#TODO: This needs to be a periodic task hourly, daily etc. or if it's a manual task then need an UI
@app.task
def runner():
    CSV_URL = 'https://nycopendata.socrata.com/api/views/xx67-kt59/rows.csv?accessType=DOWNLOAD'
    filename = 'DOHMH_New_York_City_Restaurant_Inspection_Results.csv'

    extract_csv = extract.ExtractCSV()
    extract_csv.extract_data_from_source(CSV_URL, filename)
    table = transform.transform(filename)
    load.load(table)
