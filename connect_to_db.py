import os

import sqlite3
import psycopg2

import settings


def connect_to_sqlite3(db_name):
    #TODO: get connection by environment too e.g. (local, qa, prod)
    conn = sqlite3.connect(db_name)
    return conn


def connect_to_postgres():
    #TODO: get connection by environment too e.g. (local, qa, prod)
    conn = psycopg2.connect(
        host=settings.PROD_POSTRGRES['host'],
        port=settings.PROD_POSTRGRES['port'],
        dbname=settings.PROD_POSTRGRES['dbname'],
        user=settings.PROD_POSTRGRES['user'],
        password=settings.PROD_POSTRGRES['password']
    )
    return conn


def get_db_by_env(db_name, user=None):
    if os.environ.get('env') == 'DEV':
        return connect_to_sqlite3(db_name)
    else:
        return connect_to_postgres(db_name, user)
