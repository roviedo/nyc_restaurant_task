# The NYC Restaurant task using Python, Petl, Flask and Heroku

### About application
#### ETL job that ingests a ~500k rows DOHMH New York City Restaurant Inspection Results data set from [NYC Open Data Link](https://nycopendata.socrata.com/api/views/xx67-kt59/rows.csv?accessType=DOWNLOAD)

#### Schema

```
CREATE TABLE restaurant(
     id    SERIAL PRIMARY KEY, #SERIAL in postgres (INTEGER PRIMARY KEY AUTOINCREMENT for sqlite3)
     camis INTEGER,
     name  TEXT,
     boro TEXT,
     building TEXT,
     street TEXT,
     zipcode INTEGER,
     phone BIGINT, # BIGINT for postgres (INTEGER is okay in sqlite3)
     cuisine_description TEXT,
     inspection_date   TEXT,
     action TEXT,
     violation_code TEXT,
     violation_description TEXT,
     critical_flag TEXT,
     score TEXT,
     grade TEXT,
     grade_date TEXT,
     record_date TEXT,
     inspection_type TEXT
);
```

### System requirements
```
virtualenv
python 3.x

```

### If you are running app locally don't forget in terminal shell
```
export env="DEV"
```

### Installation
```
python -m venv nyc_restaurant_task_env
source nyc_restaurant_task_env/bin/activate
pip install -r requirements.txt
cd /path/to/nyc_restaurant_task
```

### Setup Datastore locally
```
# Make sure your environment variable is set
export env="DEV"

cd /path/to/nyc_restaurant_task
python setup_db.py
```

### Running ETL application
* go to http://localhost:5000/etl
* OR for Production: https://floating-spire-76394.herokuapp.com/etl
* Click on "Run Etl" (wait until it finishes)
* Now you can visit the restaurants endpoint, read further below.

#### Locally you can run etl manually if you like.
```
# Make sure your environment variable is set
export env="DEV"

cd /path/to/nyc_restaurant_task
python etl_runner.py
```

### Running Flask application locally
```
cd /path/to/nyc_restaurant_task
python app.py
Then go to browser: http://localhost:5000
```

### Running application in Prod
```
Go to browser:
https://floating-spire-76394.herokuapp.com
```

### API endpoints:
```
GET: /restaurants

query params:
    * cuisine_description (Thai, Mexican, Chinese, etc.)
    * min_grade (A, B, C, D, E, F)
    * limit (default 1000)

e.g. http://localhost:5000/restaurants?cuisine_description=Thai&min_grade=B&limit=10


POST: /etl
empty body and headers at the moment. Need to add the CSV download url to body and access token to header.
```

### Running Tests
```
cd /path/to/nyc_restaurant_task
nosetests
```

### Deploying to Heroku
```
git add .
git commit -m "COMMIT MESSAGE"

# command below only needs to be done first time
heroku create
git push heroku master

heroku open
OR
go to your heroku app link
```
For more info go to [Heroku Getting Started with Python]( https://devcenter.heroku.com/articles/getting-started-with-python)
