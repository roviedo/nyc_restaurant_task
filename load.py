import petl as etl
import connect_to_db


def load(table):
    connection = connect_to_db.connect_to_sqlite3('main.db')
    etl.todb(table, connection, 'restaurant')


def main():
    pass


if __name__ == '__main__':
    main()
