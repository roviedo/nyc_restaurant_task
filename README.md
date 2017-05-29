# The NYC Restaurant task using Python, Petl, Flask and Heroku

### About application
#### ETL job that ingests a ~500k rows DOHMH New York City Restaurant Inspection Results data set from [NYC Open Data Link](https://nycopendata.socrata.com/api/views/xx67-kt59/rows.csv?accessType=DOWNLOAD)

#### Schema

```
CREATE TABLE restaurant(
  id    INTEGER PRIMARY KEY AUTOINCREMENT,
  camis INTEGER,
  name  TEXT,
  boro TEXT,
  building INTEGER,
  street TEXT,
  zipcode INTEGER,
  phone INTEGER,
  cuisine_description TEXT,
  inspection_date   TEXT,
  action TEXT,
  violation_code TEXT,
  violation_description TEXT,
  critical_flag TEXT,
  score INTEGER,
  grade TEXT,
  grade_date TEXT,
  record_date TEXT,
  inspection_type INTEGER
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
cd /path/to/nyc_restaurant_task
python setup_db.py
```

### Running ETL application
```
cd /path/to/nyc_restaurant_task
python etl_runner.py
```

### Running Flask application locally
```
cd /path/to/nyc_restaurant_task
python app.py
Then go to browser: http://localhost:5000

API endpoints:
http://localhost:5000/restaurants

query params:
    * cuisine_description (Thai, Mexican, Chinese, etc.)
    * min_grade (A, B, C, D, E, F)
    * limit (default 1000)

e.g. http://localhost:5000/restaurants?cuisine_description=Thai&min_grade=B&limit=10
```

### Running Tests
```
cd /path/to/nyc_restaurant_task
nosetests
```

### Running application in Prod
```
Go to browser:
https://floating-spire-76394.herokuapp.com

API endpoints:
https://floating-spire-76394.herokuapp.com/restaurants
```

### Deploy to Heroku
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
