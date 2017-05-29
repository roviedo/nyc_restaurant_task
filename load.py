import os

import petl as etl
import connect_to_db


def load(table):
    if os.environ.get('env') == 'DEV':
        connection = connect_to_db.connect_to_sqlite3('main.db')
    else:
        #TODO: this should be postgres since we are on heroku
        connection = connect_to_db.connect_to_postgres()

    etl.todb(table, connection, 'restaurant')


def main():
    pass


if __name__ == '__main__':
    main()
