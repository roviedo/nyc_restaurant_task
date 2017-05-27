import sqlite3

"""
CAMIS,DBA,BORO,BUILDING,STREET,ZIPCODE,PHONE,CUISINE DESCRIPTION

id,RestaurantName,BORO,BUILDING,STREET,ZIPCODE,PHONE,CUISINE_DESCRIPTION


Inspection Table
id, restaurant_id, INSPECTION DATE,ACTION,VIOLATION CODE,VIOLATION DESCRIPTION,CRITICAL FLAG,SCORE,GRADE,GRADE DATE,RECORD DATE,INSPECTION TYPE
"""

def connect_to_db(db_name):
    conn = sqlite3.connect(db_name)
    return conn

def create_tables(conn):
    c = conn.cursor()
    c.execute(
        '''
        CREATE TABLE restaurant(
          id    INTEGER PRIMARY KEY AUTOINCREMENT,
          camis INTEGER,
          name  TEXT,
          boro TEXT,
          building TEXT,
          street TEXT,
          zipcode INTEGER,
          phone INTEGER,
          cuisine_description TEXT
        );
        '''
    )

    c.execute(
        '''
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
        '''
    )

    conn.commit()

def main():
    conn = connect_to_db('main.db')
    create_tables(conn)

if __name__ == '__main__':
    main()
