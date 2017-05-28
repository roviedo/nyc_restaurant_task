import sqlite3

def connect_to_sqlite3(db_name):
    #TODO: get connection by environment too e.g. (local, qa, prod)
    conn = sqlite3.connect(db_name)
    return conn
