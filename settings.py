PROD_POSTRGRES = {
    "host": "test",
    "port": "5000",
    "dbname": "postgres",
    "user": "user",
    "password": "password"
}

REDIS_URL = 'redis://localhost:6379'

# Local settings overrides the above plus any other local variables
try:
    from local_settings import *
except:
    pass
