# The NYC Restaurant Task
## ETL job that ingests a ~500k rows DOHMH New York City Restaurant Inspection Results data set from [NYC Open Data Link](https://nycopendata.socrata.com/api/views/xx67-kt59/rows.csv?accessType=DOWNLOAD)

### About application

#### Schema

```
CREATE TABLE restaurant(
  id    INTEGER PRIMARY KEY,
  restaurant_name  TEXT,
  boro TEXT,
  building TEXT,
  street TEXT,
  zipcode INTEGER,
  phone INTEGER,
  cuisine_description TEXT
);

CREATE TABLE inspection(
  id     INTEGER,
  inspection_date   TEXT,
  action TEXT,
  violation_code TEXT,
  violation_description TEXT,
  critical_flag TEXT,
  score INTEGER,
  grade TEXT,
  grade_date TEXT,
  record TEXT,
  inspection_restaurant INTEGER,
  FOREIGN KEY(inspection_restaurant) REFERENCES artist(id)
);
```

### System requirements
```
virtualenv
python 3.x

```
### Installation
```
python -m venv nyc_restaurant_task_env
source nyc_restaurant_task_env/bin/activate
pip install -r requirements.txt
cd /path/to/nyc_restaurant_task
```

### Running application
```

```

### Running Tests
```
cd /path/to/nyc_restaurant_task
nosetests
```
